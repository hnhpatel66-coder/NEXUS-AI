import re


class ChatParser:
    """
    Parse AI response into text and code blocks.

    Returns:
    [
        {
            "type": "text",
            "content": "Hello World"
        },
        {
            "type": "code",
            "language": "python",
            "content": "print('Hello')"
        }
    ]
    """

    @staticmethod
    def parse(text: str):

        if not text:
            return []

        blocks = []

        pattern = r"```(\w+)?\n(.*?)```"

        matches = list(
            re.finditer(
                pattern,
                text,
                re.DOTALL
            )
        )

        last_end = 0

        for match in matches:

            # -------------------------
            # TEXT BEFORE CODE
            # -------------------------

            before = text[last_end:match.start()]

            if before.strip():

                blocks.append({
                    "type": "text",
                    "content": before.strip()
                })

            # -------------------------
            # CODE BLOCK
            # -------------------------

            language = match.group(1)

            if not language:
                language = "text"

            code = match.group(2).rstrip()

            blocks.append({
                "type": "code",
                "language": language,
                "content": code
            })

            last_end = match.end()

        # -------------------------
        # REMAINING TEXT
        # -------------------------

        remaining = text[last_end:]

        if remaining.strip():

            blocks.append({
                "type": "text",
                "content": remaining.strip()
            })

        return blocks

    @staticmethod
    def has_code(text: str):

        return "```" in text

    @staticmethod
    def extract_code(text: str):

        pattern = r"```(\w+)?\n(.*?)```"

        matches = re.findall(
            pattern,
            text,
            re.DOTALL
        )

        result = []

        for language, code in matches:

            if language == "":
                language = "text"

            result.append({
                "language": language,
                "code": code.rstrip()
            })

        return result

    @staticmethod
    def remove_code(text: str):

        pattern = r"```(\w+)?\n.*?```"

        return re.sub(
            pattern,
            "",
            text,
            flags=re.DOTALL
        ).strip()