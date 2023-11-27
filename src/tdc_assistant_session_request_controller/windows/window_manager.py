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

    def _is_control_property_match(
        self,
        control: Any,
        property_type: str,
        property_value: str,
    ) -> bool:
        return control.get_properties().get(property_type) == property_value

    def _find_control_by_property(
        self, property_type: str, property_value: str
    ) -> Optional[Any]:
        for control in self._pywinauto_window.descendants():
            if self._is_control_property_match(control, property_type, property_value):
                return control
        return None

    def click_control(self, control_text: ControlText) -> None:
        optional_control = self._find_control(control_text)

        if optional_control is not None:
            optional_control.click()

    def has_control(self, control_text: ControlText) -> bool:
        return self._find_control(control_text) is not None

    def has_control_by_property(self, property_type: str, property_value: str) -> bool:
        return self._find_control_by_property(property_type, property_value) is not None
