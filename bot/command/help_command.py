from .command import Command
from .boss_command import BossCommand
from .char_command import CharCommand
from .banner_command import BannerCommand


class HelpCommand(Command):
    COMMAND_SIGNATURE = "help"

    @staticmethod
    def command_usage():
        usage = (
            "Usage: !help [Commands]\n"
            "Find detailed information about a specific command usage.\n"
            "List of available commands:\n"
            f"1. {BossCommand.COMMAND_SIGNATURE}\n"
            f"2. {CharCommand.COMMAND_SIGNATURE}\n"
            f"3. {BannerCommand.COMMAND_SIGNATURE}\n"
        )
        return usage

    @staticmethod
    def handle_command(detail):
        match detail:
            case None:
                return HelpCommand.command_usage(), []
            case BossCommand.COMMAND_SIGNATURE:
                return BossCommand.command_usage(), []
            case CharCommand.COMMAND_SIGNATURE:
                return CharCommand.command_usage(), []
            case BannerCommand.COMMAND_SIGNATURE:
                return BannerCommand.command_usage(), []
            case HelpCommand.COMMAND_SIGNATURE:
                return 'Simply type "help" for help command usage'
            case _:
                return "Not A Valid Command", []
