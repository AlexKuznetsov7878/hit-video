from django.shortcuts import render, HttpResponse
from .forms import CreateVideo
from .models import Video
import os
import openai
from django.utils.text import slugify
from moviepy.editor import *
from django.core.files import File
# Setting the API key
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")


def homepage(request):
    return render(request, "homepage.html")


def video_create(request):
    if request.method == "POST":
        form = CreateVideo(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)

            # Generating unique slug
            name = profile.name
            slug = slugify(name)
            suffix = 1
            while Video.objects.filter(slug=slug).exists():
                suffix += 1
                slug = f'{slugify(name)}-{suffix}'
            profile.slug = slug

            # Save the model instance to save files to the filesystem
            profile.save()

            # Check if the file exists before processing
            if os.path.exists(profile.video_file.path):
                absolute_path = os.path.abspath(profile.video_file.path)
                video = VideoFileClip(absolute_path)

                audio_path = profile.video_file.path.replace('.mp4', '.mp3')
                video.audio.write_audiofile(audio_path, codec='mp3')

                audio_relative_path = audio_path.split('media/')[-1]
                profile.audio_file = audio_relative_path
                audio_file_path = open(audio_path, "rb")
                ######## Original language ###############3
                audio_english = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio_file_path
                )
                whisper_response_original = audio_english['text']
                profile.whisper_transcribe = whisper_response_original
                prompt = 'Create a simple clear summary from the next text in bullets, keep the summary in the original text language:\n'
                prompt += f'"{whisper_response_original}"'
                completions = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                           messages=[{"role": "user", "content": prompt}])
                response_original_summary = completions["choices"][0]["message"]["content"]
                profile.whisper_summary = response_original_summary
                ##############################################
                ######### Translation ##########################
                audio_file_path = open(audio_path, "rb")
                audio_english = openai.Audio.translate(
                    model="whisper-1",
                    file=audio_file_path
                )
                whisper_response_translate = audio_english['text']
                profile.whisper_transcribe_translate = whisper_response_translate
                prompt = 'Create a simple clear summary from the next text in bullets:\n'
                prompt += f'"{whisper_response_translate}"'
                completions = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                           messages=[{"role": "user", "content": prompt}])
                response_translate_summary = completions["choices"][0]["message"]["content"]
                profile.whisper_summary_translate = response_translate_summary
                #########################################
                profile.save()

                return render(request, "video_analyzer_results.html",
                        {"whisper_response_original":whisper_response_original,
                               "response_original_summary":response_original_summary,
                               "whisper_response_translate":whisper_response_translate,
                                "response_translate_summary": response_translate_summary})
            else:
                return HttpResponse(f"File not found at {profile.video_file.path}")

        print(form.errors)

    else:
        form = CreateVideo()

    return render(request, "video_analyzer.html", {"form": form})
