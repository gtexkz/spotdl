---

# spotdl by gtexkz

Meow
Uses [spotdl](https://github.com/spotDL/spotify-downloader)

---

## Dependencies

* Python 3.8+
* [spotdl](https://github.com/spotDL/spotify-downloader)
* ffmpeg

### Installing dependencies

```
pip install spotdl
spotdl --download-ffmpeg

```

---

## Installation

```
git clone https://github.com/gtexkz/spotdl.git
cd spotdl

```

---

## Usage

```
python spotdlg.py

```

```
======================================================
  Spotify Downloader  (by @gtex_kz / @gtexkz)
  Supports: tracks, albums, playlists
  Enter 'q' to exit
======================================================

Spotify URL: https://open.spotify.com/track/...

```

To exit, enter `q` or press Enter on an empty line.

### Terminal

```
python spotdlg.py [URL] [options]

```

#### Arguments

| Argument | Description |
| --- | --- |
| `url` | Spotify track, album, or playlist link (optional) |
| `-f`, `--format` | Audio format: `mp3`, `flac`, `ogg`, `opus`, `m4a`, `wav` (default: `mp3`) |
| `-b`, `--bitrate` | Bitrate: `128`, `192`, `256`, `320k` (default: `320k`) |
| `-o`, `--output` | Folder to save files (default: `./downloads`) |

---

## Examples

```
# Download a track in MP3 320kbps (default)
python spotdlg.py https://open.spotify.com/track/7ERdnb81djUvyq9bdu0it4?si=bfd27aef1ef24a38

# Download an album in FLAC
python spotdlg.py https://open.spotify.com/album/... -f flac

# Download a playlist to ~/Music folder with 192kbps bitrate
python spotdlg.py https://open.spotify.com/playlist/... -b 192 -o ~/Music

# Interactive mode
python spotdlg.py

```

---

## File Structure

Files are saved using the following template:

```
<output>/
└── Artist - Title.mp3

```

---

## Supported Links

| Type | Example |
| --- | --- |
| Track | `https://open.spotify.com/track/...` |
| Album | `https://open.spotify.com/album/...` |
| Playlist | `https://open.spotify.com/playlist/...` |
| Artist | `https://open.spotify.com/artist/...` |

---
