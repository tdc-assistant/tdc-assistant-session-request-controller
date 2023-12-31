from typing import Optional

from ..events import Event
from ..windows import WindowTitle, ControlText, get_first_window

from .base_observer import BaseObserver


class WindowObserver(BaseObserver):
    _window_title: WindowTitle
    _control_text: ControlText
    _event: Event
    _has_clicked: bool

    def __init__(
        self, window_title: WindowTitle, control_text: ControlText, event: Event
    ):
        super().__init__()
        self._window_title = window_title
        self._control_text = control_text
        self._event = event
        self._has_clicked = False

    def _poll(self) -> Optional[Event]:
        if self._has_clicked:
            return None

        optional_window_manager = get_first_window(
            self._window_title, self._control_text
        )

        if optional_window_manager is not None:
            optional_window_manager.click_control(self._control_text)
            self._has_clicked = True

        return None
