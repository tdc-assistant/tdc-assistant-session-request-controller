from typing import Optional

from .control_texts import ControlText
from .get_all_windows import get_all_windows
from .window_manager import WindowManager
from .window_titles import WindowTitle
from .control_texts import ControlText


def get_first_window(
    window_title: WindowTitle, control_text: Optional[ControlText] = None
) -> Optional[WindowManager]:
    windows = (
        get_all_windows()
        if window_title is None
        else get_all_windows([window_title], control_text)
    )

    if len(windows) == 0:
        return None

    return windows[0]
