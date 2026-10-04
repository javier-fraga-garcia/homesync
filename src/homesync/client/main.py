import pathlib
import asyncio

from homesync.client.watcher import Watcher
from homesync.client.worker import Worker


async def main():

    watch_dir = pathlib.Path.home() / "Escritorio" / "testdir"
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(maxsize=50)
    watcher = Watcher(watch_dir=watch_dir, loop=loop, queue=queue)
    worker_1 = Worker("worker_1", queue)
    worker_2 = Worker("worker_2", queue)
    task_1 = asyncio.create_task(worker_1.run())
    task_2 = asyncio.create_task(worker_2.run())

    try:
        print("Escuchando eventos...")
        watcher.start()
        await asyncio.gather(task_1, task_2)
    except asyncio.CancelledError:
        print("Saliendo del programa y cancelando tareas...")
        watcher.stop()
        task_1.cancel()
        task_2.cancel()
        await asyncio.gather(task_1, task_2, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
