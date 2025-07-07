# Reference Window
A windows photo reference program for artist.

## About
Reference Window provide artist with a window per photo reference.
Reference Window will only support multiple windows you won't be able to add multiples photos to a single window. The idea of this limitation is it's like sticking photos to a white board and organizing them.

## Features
- 🖱️ Drag and Drop Photos into windows of each photos. Supports local and online photos
- 🔍 Always on the top windows(Main app and References windows)
- 🔍 Zoom and panning of photos

## To be added features
- Transparency slider
- Click through window toggle

## Installation
Install Python (3.12.9 Recommended) and it's required libraries(TkinterDnD2, Pillow)
```bash
#Clone Repo
git clone https://github.com/iroarish/Reference-Window.git

#Go to Project Folder
cd reference-window

#(Optional) Python Virtual Environment
python -m venv venv
venv/Scripts/activate #For windows

# Install Required Libraries: tkinterdnd2, pillow
pip install -r requirements.txt

# Run the app
python main.py
```
