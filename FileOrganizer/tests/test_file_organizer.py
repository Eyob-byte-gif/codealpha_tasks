
import tempfile
import unittest
from pathlib import Path

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from file_organizer import get_category, organize_folder


class TestFileOrganizer(unittest.TestCase):

    def test_file_categories(self):
        self.assertEqual(get_category(Path("photo.jpg")), "Images")
        self.assertEqual(get_category(Path("notes.pdf")), "Documents")
        self.assertEqual(get_category(Path("song.mp3")), "Audio")
        self.assertEqual(get_category(Path("program.py")), "Code")
        self.assertEqual(get_category(Path("unknown.xyz")), "Others")

    def test_files_are_moved_to_correct_folders(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)

            (folder / "notes.txt").touch()
            (folder / "photo.jpg").touch()
            (folder / "song.mp3").touch()

            organize_folder(folder)

            self.assertTrue((folder / "Documents" / "notes.txt").exists())
            self.assertTrue((folder / "Images" / "photo.jpg").exists())
            self.assertTrue((folder / "Audio" / "song.mp3").exists())

            self.assertFalse((folder / "notes.txt").exists())
            self.assertFalse((folder / "photo.jpg").exists())
            self.assertFalse((folder / "song.mp3").exists())

    def test_invalid_folder_is_handled(self):
        with tempfile.TemporaryDirectory() as temporary:
            missing_folder = Path(temporary) / "does_not_exist"

            organize_folder(missing_folder)


if __name__ == "__main__":
    unittest.main()

