
#! YouTube Video Downloader

from yt_dlp import YoutubeDL

def get_best_video_formats(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forcejson': True,
        'simulate': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if info is None:
            raise ValueError("Failed to retrieve video information.")
        formats = info.get('formats', [])

        best_by_resolution = {}
        for f in formats:
            if f.get('vcodec') != 'none' and f.get('acodec') == 'none':  # Video-only
                height = f.get('height')
                if not height:
                    continue

                # Handle filesize as a float (convert if it's a string), otherwise set to "?"
                size = f.get('filesize') or f.get('filesize_approx')
                if size is None or size == "?" or isinstance(size, str):
                    continue  # Skip formats with unknown size

                # Convert size to MB
                size = round(size / 1024 / 1024, 2)

                resolution = f'{height}p'
                # Keep only the best format per resolution based on file size
                if resolution not in best_by_resolution or size > best_by_resolution[resolution]['filesize']:
                    best_by_resolution[resolution] = {
                        'format_id': f['format_id'],
                        'resolution': resolution,
                        'filesize': size
                    }

        return info['title'], info['duration'], list(best_by_resolution.values())

def main():
    print("🎬 === YouTube Downloader (Simplified AV) === 🎬")
    url = input("🔗 Enter the YouTube video URL: ").strip()

    try:
        title, duration, video_formats = get_best_video_formats(url)

        # Convert duration from seconds to a more readable format (HH:MM:SS)
        hours, remainder = divmod(duration, 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_str = f"{hours:02}:{minutes:02}:{seconds:02}"

        print(f"\n📌 Title: \033[1m{title}\033[0m ({duration_str})")
        print("\n🎥 Best Available Video Formats (auto-merged with audio):\n")
        print("No. | Resolution | Size     ")
        print("----|------------|----------|")
        for idx, f in enumerate(video_formats):
            print(f"{idx + 1:>3} | {f['resolution']:<10} | {str(f['filesize']) + 'MB':<8}")

        choice = int(input("\n👉 Choose your desired format number: "))
        selected_format = video_formats[choice - 1]

        ydl_opts = {
            'format': f"{selected_format['format_id']}+bestaudio",
            'merge_output_format': 'mp4',
            'outtmpl': r'C:\Users\92321\OneDrive\Desktop\%(title)s.%(ext)s',
        }

        print(f"\n⬇️  Downloading \033[1m{title}\033[0m in \033[1m{selected_format['resolution']}\033[0m...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ \033[1mDownload complete!\033[0m")

    except Exception as e:
        print(f"\n❌ \033[91mError:\033[0m {e}")

if __name__ == "__main__":
    main()
    