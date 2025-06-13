import os
import shutil
from pathlib import Path
from fileorganizer.rules import FILE_TYPE_MAP


def organize_files(folder_path, dry_run=False):
    folder_path = Path(folder_path).expanduser()
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder {folder_path} does not exist")

    for file in folder_path.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            destination_folder = FILE_TYPE_MAP.get(ext, "Others")
            target_dir = folder_path / destination_folder
            target_dir.mkdir(exist_ok=True)

            if dry_run:
                print(f"[Dry Run] Would move {file.name} to {destination_folder}/")
            else:
                shutil.move(str(file), str(target_dir / file.name))
                print(f"Moved {file.name} to {destination_folder}/")