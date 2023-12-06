from typing import List
from .observers import BaseObserver, WindowObserver, ClassroomOpenObserver
from .windows import WindowTitle, ControlText
from .events import Event

terminating_events: List[Event] = ["classroom-open"]


class Controller:
    _observers: List[BaseObserver]
    _should_terminate: bool

    def __init__(self):
        self._observers = []
        self._should_terminate = False

    def add_observer(self, observer: BaseObserver):
        self._observers.append(observer)

    def run(self) -> None:
        for observer in self._observers:
            event = observer.poll()
            if event in terminating_events:
                self._should_terminate = True

    def should_terminate(self) -> bool:
        return self._should_terminate


controller = Controller()

controller.add_observer(
    WindowObserver(WindowTitle.CLASSROOM, ControlText.I_AM_HERE, "new-session-alert")
)

controller.add_observer(
    WindowObserver(WindowTitle.CLASSROOM, ControlText.ACCEPT, "accept-session-request")
)

controller.add_observer(ClassroomOpenObserver())
