import os
from datetime import datetime

FOLDER = os.path.expanduser(input("Folder: ").strip())
NEWEST_FIRST = False
entries = []

def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def collect_entries():
    for name in os.listdir(FOLDER):
        path = os.path.join(FOLDER, name)
        if not os.path.isfile(path):
            continue
        try:
            stat = os.stat(path)
        except OSError:
            continue
        entries.append((name, stat.st_mtime, stat.st_ctime))
    entries.sort(key=lambda entry: entry[1], reverse=NEWEST_FIRST)

def print_entries():
    width = max((len(name) for name, _, _ in entries), default=4)
    print(f"{'Name':<{width}}  {'Modified':<19}  {'Changed':<19}")
    for name, modified, changed in entries:
        print(f"{name:<{width}}  {format_time(modified)}  {format_time(changed)}")

def main():
    if not os.path.isdir(FOLDER):
        print(f"Not a folder: {FOLDER}")
        return
    collect_entries()
    print_entries()

if __name__ == "__main__":
    main()
