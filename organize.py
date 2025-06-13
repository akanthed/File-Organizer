from fileorganizer.core import organize_files
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        organize_files(sys.argv[1])
    else:
        print("Usage: python organize.py <directory_path>")
