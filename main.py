import json, os
from pypresence import Presence

RPC = Presence(client_id="905566829408292925")
RPC.connect()

with open("icons.json") as f:
    icons = json.load(f)

while True:
    with open(os.path.expanduser("~/.cache/.shell-rich-presence"), "r") as f:
        full_commands = [line.strip() for line in f.readlines()]
    if full_commands:
        full_command = full_commands[-1]
        parts = full_command.split()
        pid = int(parts[0])
        shell = os.path.split(parts[1])[1]
        pwd = parts[2]

        extras = 3
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
            icon = {"icon": "console", "name": "Unknown", "commands": []}

        RPC.update(
            details=f"Command: {' '.join(parts[extras:])}",
            state=f"Directory: {pwd}",
            large_image=icon["icon"],
            large_text=icon["name"],
            small_image="console",
            small_text=shell,
        )
    else:
        RPC.clear()
