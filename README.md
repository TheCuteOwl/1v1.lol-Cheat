# 1v1.LOL Cheat Memory Editor

## Overview
1v1.LOL Cheat Memory Editor is a Python-based application using Tkinter and Pymem for memory editing in the game 1v1.LOL. It allows users to enable various cheats like Infinite Ammo, Infinite Health, Infinite Build, Infinite Money, and Infinite Shield.

## Features
- **Infinite Ammo:** Unlimited ammunition for your weapons.
- **Infinite Health:** Maintain maximum health throughout the game.
- **Infinite Build:** Build structures without any limitations.
- **Infinite Money:** Get unlimited in-game currency.
- **Infinite Shield (Glitched):** A special cheat for infinite shield with a glitch.

## Usage
1. Run the application by executing the `MemoryEditorGUI.py` script.
2. Check the desired cheats you want to enable.
3. Click the "Toggle Editing" button to activate the selected cheats.

## Game Detection
- The application continuously checks for the presence of the game process (`1v1_LOL.exe`).
- When the game is detected, the editing features become available.
- If the game is not launched, the application waits for its launch and displays a "Start the game!" message.

## Dependencies
- Python 3.x
- Tkinter (included in standard Python distribution)
- Pymem library (install using `pip install pymem`)

## How to Run
1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Run the `MemoryEditorGUI.py` script.

```bash
python MemoryEditorGUI.py
```

Disclaimer
Use this application responsibly and consider the game's terms of service. Cheating in online games may result in consequences, including account bans.

Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.

License
This project is licensed under the MIT License.
