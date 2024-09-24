from huggingface_hub import snapshot_download
import os

model_id = os.environ.get("MODEL", None)
model_folder = os.environ.get("MODEL_DIR", "/models")
os.makedirs(model_folder, exist_ok=True)

if model_folder is None:
    print("INFO: Using default model dir: /models")

if model_id is None:
    print("WARNING: Not all envs where specified, can not download anything")
else:
    snapshot_download(repo_id=model_id, local_dir=os.path.join(model_folder, model_id), local_dir_use_symlinks=False, revision="main")
    