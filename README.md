# Background Remover API

This is a simple Flask-based API to remove background from images using the `rembg` library.  
It accepts an image via POST request and returns the image with the background removed as a transparent PNG.

---

## Features

- Remove background from PNG/JPEG images
- Returns transparent PNG image
- Simple REST API using Flask
- Ready to deploy on Render.com or any other Python-friendly hosting

---

## Requirements

- Python 3.7+
- Flask
- rembg
- Pillow

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/Mohsina45/remove-bg-api.git
cd remove-bg-api
