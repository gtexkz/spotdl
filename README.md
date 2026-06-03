# spotdl by gtexkz

Meow
Используется [spotdl](https://github.com/spotDL/spotify-downloader)

---

## Зависимости

- Python 3.8+
- [spotdl](https://github.com/spotDL/spotify-downloader)
- ffmpeg

### Установка зависимостей

```
pip install spotdl
spotdl --download-ffmpeg
```

---

## Установка

```
git clone https://github.com/gtexkz/spotdl.git
cd spotdl
```

---

## Использование


```
python spotdlg.py
```

```
======================================================
  Spotify Downloader  (by @gtex_kz / @gtexkz)
  Поддерживает: треки, альбомы, плейлисты
  Введи 'q' для выхода
======================================================

Ссылка на Spotify: https://open.spotify.com/track/...
```

Для выхода введи `q`, или нажми Enter на пустой строке.

### Терминал

```
python spotdlg.py [URL] [опции]
```

#### Аргументы

| Аргумент | Описание |
|---|---|
| `url` | Ссылка на трек, альбом или плейлист Spotify (необязательный) |
| `-f`, `--format` | Формат аудио: `mp3`, `flac`, `ogg`, `opus`, `m4a`, `wav` (по умолчанию: `mp3`) |
| `-b`, `--bitrate` | Битрейт: `128`, `192`, `256`, `320k` (по умолчанию: `320k`) |
| `-o`, `--output` | Папка для сохранения файлов (по умолчанию: `./downloads`) |

---

## Примеры

```
# Скачать трек в MP3 320kbps (по умолчанию)
python spotdlg.py https://open.spotify.com/track/7ERdnb81djUvyq9bdu0it4?si=bfd27aef1ef24a38

# Скачать альбом в FLAC
python spotdlg.py https://open.spotify.com/album/... -f flac

# Скачать плейлист в папку ~/Music с битрейтом 192kbps
python spotdlg.py https://open.spotify.com/playlist/... -b 192 -o ~/Music

# Интерактивный режим
python spotdlg.py
```

---

## Структура файлов

Файлы сохраняются по шаблону:

```
<output>/
└── Исполнитель - Название.mp3
```

---

## Поддерживаемые ссылки

| Тип | Пример |
|---|---|
| Трек | `https://open.spotify.com/track/...` |
| Альбом | `https://open.spotify.com/album/...` |
| Плейлист | `https://open.spotify.com/playlist/...` |
| Артист | `https://open.spotify.com/artist/...` |

---
