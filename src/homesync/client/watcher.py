from pathlib import Path
import asyncio
import watchdog.events as ev
from watchdog.observers import Observer

from homesync.shared.event import Event, EventType


class Handler(ev.FileSystemEventHandler):
    def __init__(self, loop: asyncio.BaseEventLoop, queue: asyncio.Queue):
        self.loop = loop
        self.queue = queue

    def on_any_event(self, event: ev.FileSystemEvent):
        if event.is_directory:
            return

        if (
            event.event_type == ev.EVENT_TYPE_CREATED
            or event.event_type == ev.EVENT_TYPE_MODIFIED
        ):
            e = Event(
                src_path=event.src_path, event_type=EventType.MODIFIED, dest_path=None
            )
        elif event.event_type == ev.EVENT_TYPE_DELETED:
            e = Event(
                src_path=event.src_path, event_type=EventType.DELETED, dest_path=None
            )
        elif event.event_type == ev.EVENT_TYPE_MOVED:
            e = Event(
                src_path=event.src_path,
                event_type=EventType.MOVED,
                dest_path=event.dest_path,
            )
        else:
            return

        self.loop.call_soon_threadsafe(self.queue.put_nowait, e)


class Watcher:
    def __init__(
        self, watch_dir: Path, loop: asyncio.BaseEventLoop, queue: asyncio.Queue
    ):
        self.watch_dir = watch_dir
        self.observer = Observer()
        self.loop = loop
        self.queue = queue

    def start(self):
        handler = Handler(loop=self.loop, queue=self.queue)
        self.observer.schedule(handler, self.watch_dir, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()
