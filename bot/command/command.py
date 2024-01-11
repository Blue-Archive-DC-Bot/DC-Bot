from abc import ABC, abstractclassmethod
from typing import Optional, List
from discord import File


class Command(ABC):
    @abstractclassmethod
    def command_usage():
        pass

    @abstractclassmethod
    def handle_command(command_details: Optional[str]) -> tuple[str, List[File]]:
        pass
