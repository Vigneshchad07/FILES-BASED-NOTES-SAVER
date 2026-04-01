import os

NOTES_DIR = "notes"

def initialize():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def get_note_path(title):
    return os.path.join(NOTES_DIR, f"{title}.txt")

def add_note(title, content):
    path = get_note_path(title)
    if os.path.exists(path):
        return False
    with open(path, "w") as file:
        file.write(content)
    return True

def view_note(title):
    path = get_note_path(title)
    if not os.path.exists(path):
        return None
    with open(path, "r") as file:
        return file.read()
