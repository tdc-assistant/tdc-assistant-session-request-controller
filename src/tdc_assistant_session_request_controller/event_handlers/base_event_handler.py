import abc

from events import Event
from logger import Logger


class BaseEventHandler(metaclass=abc.ABCMeta):
    _logger: Logger

    def __init__(self):
        self._logger = Logger(self)

    @abc.abstractmethod
    def _handle(self, event: Event) -> None:
        pass

    def handle(self, event: Event) -> None:
        start = self._logger.log("Started")
        result = self._handle(event)
        end = self._logger.log("Finished")
        self._logger.log_elapsed_time(start, end)
        return result
