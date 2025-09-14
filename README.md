# 🎬 YouTube Video Downloader (yt-dlp Based)

A simple and efficient **YouTube Video Downloader** built with `yt-dlp`.  
It lists the **best available video-only formats** (sorted by resolution), merges them with the best available audio,  
and downloads them as **MP4** directly to your local system.

---

## ✨ Features

- 🔍 **Fetches video metadata** (title, duration, formats)
- 🎥 **Lists best available video formats** by resolution and file size
- 🎧 **Auto-merges video & audio** into a single MP4 file
- 💾 **Saves with proper filename** in the selected output folder
- ❌ **Skips unknown sizes** for cleaner and more reliable results
- 🖥️ **User-friendly console interface** with formatted output

---

## 🖼 Example Output

🎬 === YouTube Downloader (Simplified AV) === 🎬
🔗 Enter the YouTube video URL: https://www.youtube.com/watch?v=abc123

📌 Title: Funny Cats Compilation (00:05:32)

🎥 Best Available Video Formats (auto-merged with audio):

No. | Resolution | Size     
----|------------|----------
  1 | 1080p      | 65.32MB
  2 | 720p       | 32.11MB
  3 | 480p       | 15.02MB

👉 Choose your desired format number: 1

⬇️  Downloading Funny Cats Compilation in 1080p...
✅ Download complete!

## 📦 Requirements

Python 3.8+
yt-dlp (pip install yt-dlp)

## 👨‍💻 Author

Muneeb Ali
📧 muneeb00ali@gmail.com
