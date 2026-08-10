import yt_dlp
import os
import sys
from datetime import datetime
import subprocess

def check_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True)
        return True
    except FileExistsError:
        return False

def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"

def progress(down):
    if down['status'] == 'BAIXANDO':
        downloaded = down.get('download_bytes', 0)
        total = down.get('total_bytes', 0) or down.get('total_bytes_estimate', 0)

        if total:
            percentage = (downloaded / total) * 100
            speed = down.get('speed', 0)
            speed_str = format_size(speed) + '/s' if speed else 'N/A'

            time = down.get('time', None)
            time_str = str(datetime.fromtimestamp(time).strftime('%M:%S')) if time else 'N/A'

            progress = f"\nProgress: {percentage:.1}% | Speed: {speed_str} | TIME: {time_str}"
            sys.stdout.write(progress)
            sys.stdout.flush()