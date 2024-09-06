import os
import shutil
from typing import List

def resolve_env(s:str) -> str:
    [s := s.replace("$"+k, v) for k, v in dict(os.environ).items()]
    return s

def resolve_envs(ss:List[str]) -> List[str]:
    return list(map(resolve_env, ss))

def start():
    def launch_control_gui(port):
        executable = "py_cmd_launcher_gui"
        cmd = [
            executable,
            "--port=" + str(port),
        ]
        print("launching app", cmd)
        return cmd

    return {
        "command": launch_control_gui,
        "timeout": 300,
        "new_browser_tab": False,
        "launcher_entry": {
            "title": "Sidecar Control GUI",
        }
    }
    