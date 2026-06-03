#!/usr/bin/env python3

import sys
import os
import subprocess
import argparse
import re


def check_spotdl():
    try:
        result = subprocess.run(
            ["spotdl", "--version"],
            capture_output=True, text=True
        )
        print(f"[OK] spotdl {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("[ERROR] spotdl не найден.")
        print("    Установи: pip install spotdl")
        print("    Затем:    spotdl --download-ffmpeg   (если нет ffmpeg)")
        return False


def is_spotify_url(url: str) -> bool:
    return bool(re.search(r"open\.spotify\.com/(track|album|playlist|artist)/", url))


def download(url: str, audio_format: str, output_dir: str, bitrate: str):
    os.makedirs(output_dir, exist_ok=True)

    # Шаблон имени файла
    output_template = os.path.join(output_dir, "{artist} - {title}.{output-ext}")

    cmd = [
        "spotdl",
        "download", url,
        "--format",   audio_format,
        "--bitrate",  bitrate,
        "--output",   output_template,
        "--print-errors",
    ]

    print(f"\nПоиск и загрузка: {url}")
    print(f"    Формат: {audio_format.upper()} @ {bitrate}kbps → {output_dir}\n")

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print(f"\n[OK] Готово! Файл сохранён в: {output_dir}")
    else:
        print(f"\n[WARNING] Завершилось с кодом {result.returncode}")


def interactive_mode(audio_format: str, output_dir: str, bitrate: str):
    print("=" * 54)
    print("  Spotify Downloader  (by @gtex_kz / @gtexkz)")
    print("  Поддерживает: треки, альбомы, плейлисты")
    print("  Введи 'q' для выхода")
    print("=" * 54)

    while True:
        url = input("\nСсылка на Spotify: ").strip()
        if url.lower() in ("q", "quit", "exit", ""):
            print("chao!")
            break
        if not is_spotify_url(url):
            print("[WARNING] Похоже это не Spotify-ссылка. Попробуй ещё раз.")
            continue
        download(url, audio_format, output_dir, bitrate)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Скачивает треки/альбомы/плейлисты из Spotify",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=(
            "Примеры:\n"
            "  python spotify_downloader.py\n"
            "  python spotify_downloader.py https://open.spotify.com/track/...\n"
            "  python spotify_downloader.py https://open.spotify.com/playlist/... -f flac\n"
        ),
    )
    parser.add_argument("url", nargs="?",
                        help="Spotify-ссылка (трек / альбом / плейлист)")
    parser.add_argument("-f", "--format", default="mp3",
                        choices=["mp3", "flac", "ogg", "opus", "m4a", "wav"],
                        help="Формат аудио (по умолч. mp3)")
    parser.add_argument("-b", "--bitrate", default="320k",
                        choices=["128", "192", "256", "320k"],
                        help="Битрейт в kbps (по умолч. 320k)")
    parser.add_argument("-o", "--output", default="downloads",
                        help="Папка для сохранения (по умолч. ./downloads)")
    return parser.parse_args()


def main():
    args = parse_args()

    if not check_spotdl():
        sys.exit(1)

    if args.url:
        if not is_spotify_url(args.url):
            sys.exit("[ERROR] Это не Spotify-ссылка.")
        download(args.url, args.format, args.output, args.bitrate)
    else:
        interactive_mode(args.format, args.output, args.bitrate)


if __name__ == "__main__":
    main()
