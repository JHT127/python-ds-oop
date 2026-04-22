
from abc import ABC, abstractmethod
from typing import Optional

class Reservable(ABC):
    @abstractmethod
    def reserve(self, user_id):
        pass

    @abstractmethod
    def cancel_reservation(self, user_id):
        pass

    @property
    @abstractmethod
    def is_reserved(self):
        pass

    @property
    @abstractmethod
    def reserved_by(self) -> Optional[str]:
        pass