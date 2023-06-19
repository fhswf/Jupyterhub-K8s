import os
import shutil

def setup_vscode():
    def _get_vscode_cmd(port):
        executable = "code-server"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find code-server in PATH")
        
        # Start vscode in CODE_WORKINGDIR env variable if set
        # If not, start in 'current directory', which is $REPO_DIR in mybinder
        # but /home/jovyan (or equivalent) in JupyterHubs
        working_dir = os.getenv("CODE_WORKINGDIR", ".")
        extensions_dir = os.getenv("CODE_EXTENSIONSDIR", None)
        user_data_dir = os.getenv("CODE_USERDATADIR", None)
        extra_args = os.getenv("CODE_ARGS", None)
        
        cmd = [
            executable,
            "--auth",
            "none",
            "--disable-telemetry",
            "--port=" + str(port),
        ]

        if extensions_dir:
            cmd += ["--extensions-dir", extensions_dir]
        if user_data_dir:
            cmd += ["--user-data-dir", user_data_dir]
        if extra_args:
            cmd.extend(extra_args.split(":"))

        cmd.append(working_dir)
        return cmd

    return {
        "command": _get_vscode_cmd,
        "timeout": 300,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "VS Code",
            "icon_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons", "vscode.svg" ),
        }
    }