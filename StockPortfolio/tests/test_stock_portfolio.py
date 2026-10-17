
import json
import os
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import stock_portfolio


class TestStockPortfolio(unittest.TestCase):

    def test_add_stock(self):
        portfolio = {}
        answers = ["AAPL", "Apple", "3", "1000", "2500"]

        with patch("builtins.input", side_effect=answers):
            with patch("builtins.print"):
                with patch.object(stock_portfolio, "save_portfolio"):
                    stock_portfolio.add_stock(portfolio)

        self.assertEqual(portfolio["AAPL"]["shares"], 3)
        self.assertEqual(portfolio["AAPL"]["purchase_price"], 1000)
        self.assertEqual(portfolio["AAPL"]["current_price"], 2500)

    def test_portfolio_calculations(self):
        portfolio = {
            "AAPL": {
                "name": "Apple",
                "shares": 3,
                "purchase_price": 1000,
                "current_price": 2500
            }
        }

        output = StringIO()
        with redirect_stdout(output):
            stock_portfolio.view_portfolio(portfolio)

        result = output.getvalue()
        self.assertIn("Invested: $3000.00", result)
        self.assertIn("Current value: $7500.00", result)
        self.assertIn("Profit/Loss: $+4500.00", result)

    def test_save_and_load_portfolio(self):
        portfolio = {
            "AAPL": {
                "name": "Apple",
                "shares": 3,
                "purchase_price": 1000,
                "current_price": 2500
            }
        }

        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "portfolio.json")

            with patch.object(stock_portfolio, "DATA_FILE", path):
                stock_portfolio.save_portfolio(portfolio)
                loaded = stock_portfolio.load_portfolio()

        self.assertEqual(loaded, portfolio)


if __name__ == "__main__":
    unittest.main()

