# Generated by Django 4.2.3 on 2023-09-20 18:23

from django.db import migrations, models
import video_analyzer.models


class Migration(migrations.Migration):

    dependencies = [
        ('video_analyzer', '0002_video_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='audio_file',
            field=models.FileField(blank=True, default='audio_example.mp4', null=True, upload_to=video_analyzer.models.audio_directory_path),
        ),
    ]