from typing import Optional

import abc

from logger import Logger
from events import Event


class BaseObserver:
    _logger: Logger

    def __init__(self):
        self._logger = Logger(self)

    @abc.abstractmethod
    def _poll(self) -> Optional[Event]:
        pass

    def poll(self) -> Optional[Event]:
        start = self._logger.log("Started")
        result = self._poll()
        end = self._logger.log("Finished")
        self._logger.log_elapsed_time(start, end)
        return result
