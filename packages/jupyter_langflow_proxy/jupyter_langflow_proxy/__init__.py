import os
import shutil
from typing import List

def resolve_env(s:str) -> str:
    [s := s.replace("$"+k, v) for k, v in dict(os.environ).items()]
    return s

def resolve_envs(ss:List[str]) -> List[str]:
    return list(map(resolve_env, ss))

def run_langflow():
    def _get_langflow_cmd(port):
            
        # Start vscode in CODE_WORKINGDIR env variable if set
        # If not, start in 'current directory', which is $REPO_DIR in mybinder
        # but /home/jovyan (or equivalent) in JupyterHubs
        working_dir = os.getenv("CODE_WORKINGDIR", ".")
        extensions_dir = os.getenv("CODE_EXTENSIONSDIR", None)
        user_data_dir = os.getenv("CODE_USERDATADIR", None)
        extra_args = os.getenv("CODE_ARGS", None)
        cmd = [
            "python", "-m", "langflow", "run", "--host", "0.0.0.0", "--port", str(port),
        ]

        if extra_args:
            cmd.extend(resolve_envs(extra_args.split(":")))

        print("launching langflow server", cmd)
        return cmd

    return {
        "command": _get_langflow_cmd,
        "timeout": 300,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "Langflow",
            "icon_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons", "langflow-icon-black-transparent.svg" ),
        }
    }