import argparse
from .core import organize_files

def main():
    parser = argparse.ArgumentParser(description="Automatically organize files in a folder by type.")
    parser.add_argument("path", help="Path to the folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview file moves without applying them")
    args = parser.parse_args()

    try:
        organize_files(args.path, dry_run=args.dry_run)
    except Exception as e:
        print(f"Error: {e}")