import time
from pathlib import Path
import watchdog.events as ev
from watchdog.observers import Observer

from models import Event, EventType


class Handler(ev.FileSystemEventHandler):
    @staticmethod
    def on_any_event(event: ev.FileSystemEvent):

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


class Watcher:
    def __init__(self, watch_dir: Path):
        self.watch_dir = watch_dir
        self.observer = Observer()

    def run(self):

        handler = Handler()
        self.observer.schedule(handler, self.watch_dir, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()

        self.observer.join()
