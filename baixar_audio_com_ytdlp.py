import yt_dlp

def baixar_audio(url):
    print("⏬ Baixando o áudio com yt-dlp...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audios/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("✅ Áudio baixado com sucesso!")

def main():
    url = input("🔗 Cole a URL do vídeo do YouTube: ").strip()
    baixar_audio(url)

if __name__ == "__main__":
    main()
