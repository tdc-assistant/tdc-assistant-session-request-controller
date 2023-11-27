from typing import List, Optional

from pywinauto import Desktop  # type: ignore

from .control_texts import ControlText
from .window_titles import WindowTitle, window_titles
from .window_manager import WindowManager


def get_all_windows(
    window_titles_to_filter: list[WindowTitle] = window_titles,
    control_text: Optional[ControlText] = None,
) -> List[WindowManager]:
    windows = Desktop(backend="uia").windows()

    result: list[WindowManager] = []

    for w in windows:
        for t in window_titles_to_filter:
            if t.value.lower() in w.window_text().lower():
                wm = WindowManager(w)
                if control_text is None or wm.has_control(control_text):
                    result.append(wm)
                    break

    return result
