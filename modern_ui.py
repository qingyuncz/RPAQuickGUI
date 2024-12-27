from PyQt6.QtGui import QColor, QFont

class UIStyles:
    @staticmethod
    def modern():
        """现代风格"""
        return {
            'window': """
                QWidget {
                    background-color: #2d2d2d;
                    color: #ffffff;
                    font-family: Segoe UI;
                    font-size: 12px;
                }
            """,
            'button': """
                QPushButton {
                    background-color: #4CAF50;
                    color: #ffffff;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """,
            'input': """
                QLineEdit {
                    background-color: #ffffff;
                    color: #000000;
                    border: 1px solid #cccccc;
                    border-radius: 3px;
                    padding: 5px;
                }
            """,
            'label': """
                QLabel {
                    color: #ffffff;
                }
            """
        }

    @staticmethod
    def light():
        """浅色风格"""
        return {
            'window': """
                QWidget {
                    background-color: #f5f5f5;
                    color: #333333;
                    font-family: Arial;
                    font-size: 12px;
                }
            """,
            'button': """
                QPushButton {
                    background-color: #2196F3;
                    color: #ffffff;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #1e88e5;
                }
            """,
            'input': """
                QLineEdit {
                    background-color: #ffffff;
                    color: #000000;
                    border: 1px solid #cccccc;
                    border-radius: 3px;
                    padding: 5px;
                }
            """,
            'label': """
                QLabel {
                    color: #333333;
                }
            """
        }

    @staticmethod
    def dark():
        """深色风格"""
        return {
            'window': """
                QWidget {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    font-family: Consolas;
                    font-size: 12px;
                }
            """,
            'button': """
                QPushButton {
                    background-color: #607D8B;
                    color: #ffffff;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #546E7A;
                }
            """,
            'input': """
                QLineEdit {
                    background-color: #2d2d2d;
                    color: #ffffff;
                    border: 1px solid #444444;
                    border-radius: 3px;
                    padding: 5px;
                }
            """,
            'label': """
                QLabel {
                    color: #ffffff;
                }
            """
        }
