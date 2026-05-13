# YT-Link-Harvester-

Professional YouTube latest videos harvester using Python and GitHub Actions.

## Features

- Fetch latest 5 YouTube videos
- Extract titles and video IDs
- Save output to TXT
- Professional logging
- Strong error handling
- Modular architecture
- GitHub Actions support
- Extensible structure

---

## Usage

1. Go to GitHub Actions
2. Select workflow:
   `YouTube Latest Videos Fetcher`
3. Click `Run workflow`
4. Enter YouTube channel URL

Example:

```text
https://www.youtube.com/@MrBeast
```

---

## Output

Generated file:

```text
output/latest_videos.txt
```

---

## Project Structure

```text
src/
├── youtube/
├── services/
├── logger.py
├── config.py
├── exceptions.py
└── main.py
```
