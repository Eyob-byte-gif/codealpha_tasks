
from pathlib import Path
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c"],
}


def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_folder(folder):
    folder = Path(folder).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("Error: folder does not exist.")
        return

    moved = 0

    for item in list(folder.iterdir()):
        if not item.is_file() or item.name == "file_organizer.py":
            continue

        category = get_category(item)
        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / item.name

        # Avoid overwriting files with the same name.
        if destination.exists():
            print(f"Skipped duplicate: {item.name}")
            continue

        try:
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/")
            moved += 1
        except OSError as error:
            print(f"Could not move {item.name}: {error}")

    print(f"\nFinished! Organized {moved} file(s).")


def main():
    print("=== FILE ORGANIZER ===")
    print("Use a test folder first.")
    folder = input("Folder path to organize: ").strip()

    if not folder:
        print("No folder entered.")
        return

    organize_folder(folder)


if __name__ == "__main__":
    main()

