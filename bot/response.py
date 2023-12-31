import command as handler


def clean_command_details(detail):
    return " ".join(detail.split())


def parse_content(content):
    content = content.lower()
    splitted = content.split(" ", 1)

    command = splitted[0]
    if len(splitted) == 1:
        detail = None
    else:
        detail = splitted[1]

    return command, detail


def get_response(content):
    """
    Returns message content, list of files to send
    """
    DEFAULT_RESPONSE = ("Invalid Command", [])

    command, detail = parse_content(content)

    match command:
        case "char":
            if detail is None:
                return DEFAULT_RESPONSE
            return handler.handle_char_command(detail)
        case "banner":
            return handler.handle_banner_command()
        case _:
            return DEFAULT_RESPONSE
