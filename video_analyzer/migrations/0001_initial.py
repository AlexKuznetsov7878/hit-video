# Generated by Django 4.2.5 on 2023-09-20 17:25

from django.db import migrations, models
import video_analyzer.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "video_file",
                    models.FileField(
                        default="video_example.mp4",
                        upload_to=video_analyzer.models.video_directory_path,
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("whisper_transcribe", models.TextField(blank=True, null=True)),
                ("whisper_summary", models.TextField(blank=True, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]