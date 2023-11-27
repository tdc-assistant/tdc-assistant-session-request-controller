from typing import List
from observers import BaseObserver, WindowObserver
from windows import WindowTitle, ControlText
from events import Event

terminating_events: List[Event] = ["accept-session-request"]


class Controller:
    _observers: List[BaseObserver]
    _should_terminate: bool

    def __init__(self, observers: List[BaseObserver]):
        self._observers = observers
        self._should_terminate = False

    def run(self) -> None:
        for observer in self._observers:
            event = observer.poll()
            if event in terminating_events:
                self._should_terminate = True

    def should_terminate(self) -> bool:
        return self._should_terminate


new_session_alert_observer = WindowObserver(
    WindowTitle.CLASSROOM, ControlText.I_AM_HERE, "new-session-alert"
)

accept_session_request_observer = WindowObserver(
    WindowTitle.CLASSROOM, ControlText.ACCEPT, "accept-session-request"
)

controller = Controller([new_session_alert_observer, accept_session_request_observer])
