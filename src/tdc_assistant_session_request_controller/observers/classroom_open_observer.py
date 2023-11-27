from typing import Optional

from ..events import Event
from ..windows import WindowTitle, get_first_window

from .base_observer import BaseObserver


class ClassroomOpenObserver(BaseObserver):
    _event: Event

    def __init__(self):
        super().__init__()

    def _poll(self) -> Optional[Event]:
        optional_window_manager = get_first_window(WindowTitle.CLASSROOM)

        if optional_window_manager is not None:
            if optional_window_manager.has_control_by_property(
                "automation_id", "txtChatLog"
            ):
                return "classroom-open"

        return None
