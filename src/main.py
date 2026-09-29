import pathlib
import asyncio

from watcher import Watcher


async def main():
    watch_dir = pathlib.Path.home() / "Escritorio" / "testdir"
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(maxsize=50)
    watcher = Watcher(watch_dir=watch_dir, loop=loop, queue=queue)
    watcher.start()


if __name__ == "__main__":
    asyncio.run(main())
