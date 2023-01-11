from abc import ABC, abstractmethod
from typing import Union


class BusinessException(Exception, ABC):

    @property
    @abstractmethod
    def status_code(self) -> int:
        pass

    @property
    @abstractmethod
    def payload(self) -> Union[str, dict]:
        pass
