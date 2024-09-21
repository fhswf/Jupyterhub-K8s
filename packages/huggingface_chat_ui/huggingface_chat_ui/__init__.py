import os


def run_chat_ui():
    return {
        "command": "xdg-open localhost:9123",
        "timeout": 300,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "HF Chat",
            "icon_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons", "huggingface.svg" ),
        }
    }
