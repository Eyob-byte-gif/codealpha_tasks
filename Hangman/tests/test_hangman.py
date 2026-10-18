
import unittest
from unittest.mock import patch

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hangman


class TestHangman(unittest.TestCase):

    @patch("builtins.input", side_effect=["P", "Y", "T", "H", "O", "N"])
    @patch("random.choice", return_value="PYTHON")
    def test_player_can_win(self, mock_choice, mock_input):
        with patch("builtins.print") as mock_print:
            hangman.play_game()

        output = " ".join(
            str(call) for call in mock_print.call_args_list
        )
        self.assertIn("Congratulations!", output)

    @patch("builtins.input", side_effect=["1", "P", "P", "Y", "T", "H", "O", "N"])
    @patch("random.choice", return_value="PYTHON")
    def test_invalid_and_repeated_guesses(self, mock_choice, mock_input):
        with patch("builtins.print") as mock_print:
            hangman.play_game()

        output = " ".join(
            str(call) for call in mock_print.call_args_list
        )
        self.assertIn("Invalid guess!", output)
        self.assertIn("already guessed", output)


if __name__ == "__main__":
    unittest.main()

