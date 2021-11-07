import json, os, psutil, time
from pypresence import Presence

RPC = Presence(client_id="905566829408292925")
RPC.connect()

with open("icons.json") as f:
    icons = json.load(f)

while True:
    with open(os.path.expanduser("~/.cache/.shell-rich-presence"), "r") as f:
        full_commands = [
            line.strip()
            for line in [l for l in f.readlines() if l.strip()]
            if int(line.strip().split()[0]) in psutil.pids()
        ]

    if full_commands:
        full_command = full_commands[-1]
        parts = full_command.split()
        pid = int(parts[0])
        shell = os.path.split(parts[1])[1]
        pwd = parts[2]
        time_ = parts[3]

        extras = 4
        cmd = os.path.split(parts[extras])[1]

        if len(full_command) > extras + 1:
            flags = parts[extras:]
        else:
            flags = []

        icon = {}
        for i in icons:
            if cmd in i["commands"]:
                icon = i
                break
        if not icon:
            icon = {"icon": "console", "name": "Unknown", "commands": [], "docs": None}

        RPC.update(
            details=f"Command: {' '.join(parts[extras:])}",
            state=f"Directory: {pwd}",
            large_image=icon["icon"],
            large_text=icon["name"],
            small_image="console",
            small_text=f"Shell: {shell}",
            start=int(time_),
            buttons=[{"label": "View Documentation", "url": icon["docs"]}]
            if icon["docs"]
            else None,
        )

        time.sleep(15)
    else:
        RPC.clear()
