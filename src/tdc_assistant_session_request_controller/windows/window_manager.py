from typing import Any, Optional

from .control_texts import ControlText


def _control_has_text(control: Any, control_text: ControlText) -> bool:
    return (
        len(control.texts()) > 0
        and isinstance(control.texts()[0], str)
        and control.texts()[0].startswith(control_text.value)
    )


class WindowManager:
    _pywinauto_window: Any

    def __init__(self, pywinauto_window: Any):
        self._pywinauto_window = pywinauto_window

    def _find_control(self, control_text: ControlText) -> Optional[Any]:
        for control in self._pywinauto_window.descendants():
            if _control_has_text(control, control_text):
                return control

        return None

    def click_control(self, control_text: ControlText) -> None:
        optional_control = self._find_control(control_text)

        if optional_control is not None:
            optional_control.click()

    def has_control(self, control_text: ControlText) -> bool:
        return self._find_control(control_text) is not None
