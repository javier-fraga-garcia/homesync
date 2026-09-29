import pathlib
from watcher import Watcher


def main():
    watch_dir = pathlib.Path.home() / "Escritorio" / "testdir"
    watcher = Watcher(watch_dir=watch_dir)
    watcher.run()


if __name__ == "__main__":
    main()
