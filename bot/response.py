from command import get_command_response


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

    command, detail = parse_content(content)
    return get_command_response(command, detail)
