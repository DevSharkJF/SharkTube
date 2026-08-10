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

def best_format(formats, target_height, ffmpeg_available):
    if ffmpeg_available:
        return f'bestvideo[height<={target_height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={target_height}][ext=mp4]/best'
    else:
        return f'best[height<={target_height}][ext=mp4]/best[ext=mp4]/best'

def download_video(url, preferred_quality=None, output_path='downloads'):
    try:
        ffmpeg_available = check_ffmpeg()
        if not ffmpeg_available:
            print("\nAviso: o FFmpeg não está instalado. Algumas opções de alta qualidade podem estar limitadas.")
            print("O script selecionará automaticamente o melhor formato compatível disponível.")
            print("Para habilitar todas as opções de qualidade, instale o FFmpeg e adicione-o ao PATH do sistema.")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_opts = {
            'progress': [progress],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'verbose': False
        }

        print("Buscando informações do vídeo")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            print(f"\nTítulo do Vídeo: {info.get('title', 'Unknown')}")
            duration = int(info.get('duration', 0))
            print(f"Duração: {duration // 60}:{duration %60:02d}")

            formats = info.get('formats', [])
            quality_set = set()

            for formated in formats:
                height = formated.get('height')
                if height and (ffmpeg_available or formated.get('acodec') != 'none'):
                    quality_set.add(f"{height}p")

            quality_list = sorted(quality_set, key=lambda x: int(x.replace('p', '')))

            print("\n Qualidades Disponíveis:")
            for i, quality in enumerate(quality_list, 1):
                print(f"{i}. {quality}")

            if not preferred_quality or preferred_quality not in quality_set:
                print("\n Selecione uma das qualidades disponíveis nas opções:")
                while True:
                    try:
                        choice = int(input("Digite o número da sua escolha: "))
                        if 1 <= choice <= len(quality_list):
                            preferred_quality = quality_list[choice-1]
                            break
                        else: print("Escolha Inválida. Tente Novamente")
                    except ValueError:
                        print("Selecione um número válido")

            height = int(preferred_quality.replace('p', ''))
            ydl_opts['format'] = best_format(formats, height, ffmpeg_available)

            print(f"\n Download do vídeo em: {preferred_quality}...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("\nO Vídeo foi baixado com sucesso")

    except Exception as error:
        print(f"\nOcorreu um erro: {str(error)}")
        print("\nDicas para solução de problemas:")
        print("1. Verifique sua conexão com a internet")
        print("2. Verifique se a URL do vídeo está correta e acessível")
        print("3. Tente atualizar o yt-dlp: `pip install --upgrade yt-dlp`")
        print("4. Certifique-se de que o vídeo não seja privado ou tenha restrição de idade")
        print("5. Se quiser acesso a todas as opções de qualidade, execute `choco install FFmpeg`")

if __name__ == "__main__":
    video_url = input("Link do Vídeo no YouTube: ")
    preferred_quality = input("Digite a qualidade desejada (ex.: 720p) ou pressione Enter para ver as opções disponíveis: ").strip()
    
    download_video(video_url, preferred_quality)