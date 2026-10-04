import asyncio

from homesync.shared.models import Event


class Worker:
    def __init__(self, worker_id: str, queue: asyncio.Queue):
        self.worker_id = worker_id
        self.queue = queue

    async def run(self):
        while True:
            ev: Event = await self.queue.get()

            print(f"{self.worker_id} - proceso evento: {ev}")
            self.queue.task_done()
