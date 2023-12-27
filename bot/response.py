import command as handler


def clean_command_details(detail):
    return " ".join(detail.split())


def get_response(content):
    """
    Returns message content, list of files to send
    """
    DEFAULT_RESPONSE = ("Invalid Command", [])

    content = content.lower()
    splitted = content.split(" ", 1)
    if len(splitted) < 2:
        return DEFAULT_RESPONSE

    command, detail = splitted
    detail = clean_command_details(detail)

    match command:
        case "char":
            return handler.handle_char_command(detail)
        case _:
            return DEFAULT_RESPONSE
