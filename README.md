# TypeRacer Automation Bot

This Python script automates the process of playing TypeRacer (https://play.typeracer.com/) using Selenium WebDriver and PyAutoGUI.

## Prerequisites

Before running this script, make sure you have the following installed:

- Python 3.x
- Selenium WebDriver
- PyAutoGUI
- keyboard

You can install the required packages using pip:

```
pip install selenium pyautogui keyboard
```

Additionally, you'll need to have Chrome browser installed and the appropriate ChromeDriver for your Chrome version.

## How it works

1. The script opens a Chrome browser and navigates to TypeRacer.
2. It maximizes the browser window and waits for the page to load.
3. It simulates a keyboard shortcut (Ctrl+Alt+O) to start a new game.
4. The script then locates the text to be typed using Selenium.
5. Finally, it uses PyAutoGUI to automatically type the text with a slight delay between keystrokes.

## Usage

To run the script, simply execute:

```
python main.py
```

## Disclaimer

This script is for educational purposes only. Using automation tools like this in online typing games may violate the terms of service of the website and could result in your account being banned. Use at your own risk.

## Notes

- The typing speed can be adjusted by changing the delay in the `pyautogui.typewrite()` function.
- The script currently closes the browser after completing one game. Modify as needed for continuous play.
- Ensure your internet connection is stable for the best results.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

## License

This project is open source and available under the [MIT License](LICENSE).
