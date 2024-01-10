from .char_command import CharCommand
from .banner_command import BannerCommand
from .boss_command import BossCommand
from typing import Optional, List
from discord import File


def get_command_response(command: str, detail: Optional[str]) -> tuple[str, List[int]]:
    DEFAULT_RESPONSE = ("Invalid Command", [])

    match command:
        case "char":
            return CharCommand.handle_command(detail)
        case "banner":
            return BannerCommand.handle_command(detail)
        case "boss":
            return BossCommand.handle_command(detail)
        case _:
            return DEFAULT_RESPONSE
