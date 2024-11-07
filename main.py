import json
import re
import os
from datetime import datetime

def output(data: str, prefix="GENERIC"):
    """Outputs the input data"""
    if isinstance(data, dict) or isinstance(data, list):
        data = f"{json.dumps(data, indent=4)}"
    print(f"[{prefix.upper()}]:", data)

def timestampToDate(timestamp: float) -> str:
    """Converts a timestamp to a date string"""
    date = datetime.fromtimestamp(timestamp)
    return date.strftime("%m/%d/%Y, %H:%M:%S %p")

def pathExists(path: str) -> bool:
    """Returns whether or not a path exists in user's file system"""
    return os.path.exists(path)

def autoHotKeyExists() -> bool:
    """Returns whether or not AutoHotkey exists"""
    return os.path.exists("C:\\Program Files\\AutoHotkey")

def logitechGHubExists() -> bool:
    """Returns whether or not Logitech GHub exists"""
    return os.path.exists("C:\\Program Files\\LGHUB")

def razerSynapseExists() -> bool:
    """Returns whether or not Razer Synapse exists"""
    return os.path.exists("C:\\Program Files (x86)\\Razer\\Synapse3")

def solaraFolderExists() -> bool:
    """Returns whether or not the Solara folder exists"""
    return pathExists("C:\\ProgramData\\Solara")

def waveFolderExists() -> bool:
    """Returns whether or not the Wave folder exists"""
    return pathExists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Wave")

def robloxFolderExists() -> bool:
    """Returns whether or not the Roblox folder exists"""
    return pathExists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox")

def bloxstrapFolderExists() -> bool:
    """Returns whether or not the Bloxstrap folder exists"""
    return pathExists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Bloxstrap")

def bloxstrapTempFolderExists() -> bool:
    """Returns whether or not the Bloxstrap folder exists in 'temp'"""
    return pathExists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\Bloxstrap")

def getLogitechScripts() -> list[dict]:
    """Returns a list of Logitech G Hub scripts"""
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\LGHUB\\scripts"
    try:
        scripts = []
        for scriptId in os.listdir(path):
            scriptPath = f"{path}\\{scriptId}\\script.lua"
            scriptData = ""
            try:
                with open(scriptPath, "r") as file:
                    scriptData = file.read()
            except Exception as err:
                scriptData = f"Failed to read script: '{scriptPath}': {err}"
            scripts.append({
                "script_id": scriptId,
                "script_data": scriptData
            })
        return scripts
    except:
        return []
        

def getBloxstrapReferences(fileName: str) -> list[str]:
    """Returns each line in a Roblox log that references 'Bloxstrap'"""
    try:
        with open(fileName, "r") as file:
            return [line for line in file.readlines() if "bloxstrap" in line.lower()]
    except:
        return []

def isBloxstrapInLogs() -> tuple[list[dict], str]:
    """Returns whether or not Bloxstrap is referenced at all in Roblox logs, and the most recent log"""
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\logs"

    logsWithBloxstrap = []

    for file in sorted(os.listdir(path)):
        if not file.endswith(".log"):
            continue

        logPath = f"{path}\\{file}"
        refs = getBloxstrapReferences(logPath)
        modTime = os.path.getmtime(logPath)
        modifiedDate = timestampToDate(modTime)

        if len(refs) != 0:
            logsWithBloxstrap.append({
                "name": file,
                "path": logPath,
                "date": modifiedDate
            })
            
    return (logsWithBloxstrap, logsWithBloxstrap[-1])

def getUsedAccountsInLogs() -> list[dict]:
    """Returns a list of used accounts in Roblox logs"""
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\logs"
    dataPattern = r'data\((\{.*?\})\)'

    accounts = []

    for fileName in os.listdir(path):
        if not fileName.endswith(".log"):
            continue

        logPath = f"{path}\\{fileName}"
        modTime = os.path.getmtime(logPath)
        modifiedDate = timestampToDate(modTime)

        try:
            with open(logPath, "r") as file:
                match = re.search(dataPattern, file.read())
                if match:
                    data = match.group(1)
                    accounts.append({
                        "log_name": fileName,
                        "log_path": logPath,
                        "account": json.loads(data),
                        "date": modifiedDate
                    })
        except:
            continue

    return accounts

def getBloxstrapFFlags() -> dict:
    """Returns the currently saved Bloxstrap FFlags"""
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Bloxstrap\\Modifications\\ClientSettings\\ClientAppSettings.json"
    try:
        with open(path, "r") as file:
            return json.loads(file.read())
    except Exception as err:
        output(f"Failed to read 'ClientAppSettings' for FFlags: {err}", "ERROR")
        return {}
    
def waitForKeyboardInterrupt():
    try:
        while True:
            pass
    except:
        exit()
    
def main():
    output("PC Checking Tool written by 'Magnet' @ EAU", "INFO")

    print()

    ###### START BLOXSTRAP ######

    output("Checking for Bloxstrap..", "INFO")

    folderExists = bloxstrapFolderExists()
    output(f"Bloxstrap folder exists: {folderExists}")

    tempFolderExists = bloxstrapTempFolderExists()
    output(f"Bloxstrap folder exists (in temp): {tempFolderExists}")

    if folderExists:
        print()

        output("Getting user's saved FFlags from Bloxstrap folder..")
        fflags = getBloxstrapFFlags()
        with open("fflags.json", "w") as file:
            file.write(json.dumps(fflags, indent=4))
        output(f"You can find the FFlags in 'fflags.json'", "INFO")

    robloxExists = robloxFolderExists()
    if robloxExists:
        print()

        output("Getting Bloxstrap references in Roblox logs..")
        logResults, mostRecent = isBloxstrapInLogs()
        output(f"There are {len(logResults)} instances of Bloxstrap in the user's Roblox logs (C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\logs)")
        output(f"The most recent log was at: {mostRecent["date"]}")

    ###### END BLOXSTRAP ######

    print()

    ###### START MACROS ######

    output("Checking for macro usage programs..", "INFO")

    ahkExists = autoHotKeyExists()
    output(f"AutoHotkey exists: {ahkExists}")

    lgHubExists = logitechGHubExists()
    output(f"Logitech GHub exists: {lgHubExists}")

    razerExists = razerSynapseExists()
    output(f"Razer Synapse exists: {razerExists}")
    
    if lgHubExists:
        print()

        output("Getting user's saved Logitech scripts..")
        logitechScripts = getLogitechScripts()
        with open("scripts.json", "w") as file:
            file.write(json.dumps(logitechScripts, indent=4))
        output(f"You can find the list of scripts in 'scripts.json'", "INFO")
        

    ###### END MACROS ######

    print()

    ###### START EXECUTORS ######

    output("Checking for script executors..", "INFO")

    waveExists = waveFolderExists()
    output(f"Wave folder exists: {waveExists}")

    solaraExists = solaraFolderExists()
    output(f"Solara folder exists: {solaraExists}")

    ###### END EXECUTORS ######

    ###### START ACCOUNTS ######

    if robloxExists:
        print()
        
        output("Getting list of used accounts..", "INFO")
        accounts = getUsedAccountsInLogs()
        with open("accounts.json", "w") as file:
            file.write(json.dumps(accounts, indent=4))
        output(f"You can find the list in 'accounts.json'")

    ###### END ACCOUNTS ######

    print()

    output("Press 'CTRL+C' to exit", "INFO")
    waitForKeyboardInterrupt()

if __name__ == "__main__":
    main()
