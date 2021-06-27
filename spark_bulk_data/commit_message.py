import sys


def chalk(msg: str, **kwargs):
    text = {
        "red": "\u001b[31;1m",
        "green": "\u001b[32m",
        "blue": "\u001b[34;1m",
        "black": "\u001b[30m",
        "white": "\u001b[37;1m",
    }

    bg = {
        "red": "\u001b[41m",
        "green": "\u001b[42m",
        "blue": "\u001b[44m",
        "black": "\u001b[40m",
        "white": "\u001b[47;1m",
    }

    decorator = {"bold": "\u001b[1m", "underline": "\u001b[4m", "reversed": "\u001b[7m"}

    ret_str: str = msg
    morphed: bool = False
    if kwargs.get("text") in text:
        ret_str: str = f'{text.get(kwargs.get("text"))}{ret_str}'
        morphed = True

    if kwargs.get("bg") in bg:
        ret_str: str = f'{bg.get(kwargs.get("bg"))}{ret_str}'
        morphed = True

    if kwargs.get("decorator") in bg:
        ret_str: str = f'{decorator.get(kwargs.get("decorator"))}{ret_str}'
        morphed = True

    if morphed:
        ret_str = f"{ret_str}\u001b[0m"

    return ret_str


def main() -> int:
    valid_msg: list = [
        "feat",
        "enhance",
        "fix",
        "docs",
        "chore",
        "style",
        "test",
        "refactor",
        "dev",
    ]
    # Retrieve the latest commit before the change
    message_file = sys.argv[1]

    # Use a context manager to check the commit message
    with open(message_file, "r") as commit_msg:
        # read commit
        commit_msg = commit_msg.read()
        # get the prefix before parenthesis
        try:
            if any(
                [
                    (
                        commit_msg.startswith(f"{mandatory}:")
                        or commit_msg.startswith(f"{mandatory}(")
                    )
                    for mandatory in valid_msg
                ]
            ):
                return 0
            else:
                raise ValueError("Invalid Commit Msg Format")
        except ValueError as err:

            print(chalk(err, text="red", decorator="bold"), end="\n")
            stderr_1 = "Examples of Good Commit Messages:"
            print(f'\n{chalk(stderr_1, text="blue", decorator="underline")}')
            """
            Showing good examples of commits
            """

            example_1 = "enhance(core): Adding dags to airflow"
            example_2 = "fix: Spark sql module error fix see issue #241"
            example_3 = "docs(core): Adding additional documentation about the data filtering process"

            print(f'\n\t{chalk(example_1, text="green")}')
            print(f'\n\t{chalk(example_2, text="green")}')
            print(f'\n\t{chalk(example_3, text="green")}')

    return 1


if __name__ == "__main__":
    sys.exit(main())
