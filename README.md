# EAU PC-Checker
Checks the user's PC for common Roblox cheating utilities (script executors, AHK, Bloxstrap, etc..)

- Release Usage Tutorial: https://files.catbox.moe/5dczws.mp4
- Source Usage Tutorial: https://files.catbox.moe/4qv8rf.mp4
- Building Tutorial: https://files.catbox.moe/dh3qu1.mp4

# Usage
### Running from releases - useful for distributing to users you want to check
1. Download the latest `pc-checker.exe` from the [releases page](https://github.com/6ce/eau-pc-checker/releases/)
2. Move it to it's own folder (**OPTIONAL**)
3. Run the `pc-checker.exe` file

### Running from source - useful for testing/modifying codebase
1. Install [Python](https://python.org) from the web
2. Install the [repository](https://github.com/6ce/eau-pc-checker/archive/refs/heads/main.zip) to a ZIP
3. Extract it to it's own folder
4. Open the folder in `cmd`
5. Run the command `python main.py`

# Building
1. Follow [usage steps](https://github.com/6ce/eau-pc-checker/blob/main/README.md#usage) up to step 4
2. Run the command `pip install pyinstaller`
3. Once finished, run the command `pyinstaller --onefile main.py`
4. Once finished, open 'dist' folder
5. You can now use `main.exe` to run the program

# Features
- Checks if Bloxstrap folder exists
  - Saves user's FFlags to a JSON file
  - Gets references of Bloxstrap in logs (times the user used it when playing Roblox)
- Checks for macro usage programs:
  - AutoHotkey
  - Logitech G Hub
    - Saves G Hub LUA scripts to a JSON file
  - Razer Synapse
- Checks for script executors
  - Solara
  - Wave
- Gets & saves list of used Roblox accounts

# Contact
- You can contact me on these socials for suggestions/bugs:
  - Telegram: @hanukkahween

# Disclaimer
It is possible for users to bypass this by reading the source code and taking actions to prevent detection
