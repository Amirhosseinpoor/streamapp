import os
import subprocess
from celery import shared_task
from .models import VideoModels


@shared_task
def convert_to_hls(video_id):
    video = VideoModels.objects.get(id=video_id)
    input_file = video.video_file.path

    # Create a unique output directory for each video
    video_title_safe = "".join(
        x if x.isalnum() else "_" for x in video.title)  # Replace special characters with underscores
    output_dir = os.path.join(os.path.dirname(input_file), 'output', video_title_safe)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # FFmpeg command to create HLS playlist and segments
    command = f"ffmpeg -i {input_file} -hls_time 10 -hls_playlist_type vod {output_dir}/output.m3u8"
    subprocess.run(command, shell=True)

    video.hls_ready = True
    video.save()