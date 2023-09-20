# Generated by Django 4.2.5 on 2023-09-20 17:26

from django.db import migrations, models
import video_analyzer.models


class Migration(migrations.Migration):
    dependencies = [
        ("video_analyzer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="audio_file",
            field=models.FileField(
                default="audio_example.mp4",
                upload_to=video_analyzer.models.audio_directory_path,
            ),
        ),
    ]