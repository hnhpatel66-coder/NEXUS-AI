import re


class ChatParser:

    @staticmethod
    def parse(text: str):

        blocks = []

        pattern = r"```(\w+)?\n(.*?)```"

        last_end = 0

        for match in re.finditer(pattern, text, re.DOTALL):

            start, end = match.span()

            # Text Before Code
            before = text[last_end:start].strip()

            if before:
                blocks.append({
                    "type": "text",
                    "content": before
                })

            language = match.group(1)

            if language is None:
                language = "Code"

            code = match.group(2)

            blocks.append({
                "type": "code",
                "language": language,
                "content": code
            })

            last_end = end

        # Remaining Text

        remaining = text[last_end:].strip()

        if remaining:

            blocks.append({
                "type": "text",
                "content": remaining
            })

        return blocks