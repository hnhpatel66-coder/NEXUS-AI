import html
import re


class MarkdownRenderer:
    """
    Lightweight Markdown → HTML Renderer
    Supports:
    - Headings
    - Bold
    - Italic
    - Inline Code
    - Code Blocks
    - Bullet Lists
    - Number Lists
    - Block Quotes
    - Horizontal Rule
    - Links
    """

    @staticmethod
    def render(text: str) -> str:

        if not text:
            return ""

        # Escape HTML
        text = html.escape(text)

        # --------------------------------
        # CODE BLOCKS
        # --------------------------------

        code_blocks = []

        def replace_code(match):

            language = match.group(1) or "text"

            code = match.group(2)

            placeholder = f"__CODEBLOCK_{len(code_blocks)}__"

            code_blocks.append(
                f"""
                <div style="
                    background:#0B1220;
                    border:1px solid #334155;
                    border-radius:12px;
                    margin:12px 0;
                ">

                    <div style="
                        background:#111827;
                        color:#60A5FA;
                        padding:8px 12px;
                        font-weight:bold;
                        border-bottom:1px solid #334155;
                    ">
                    {language.upper()}
                    </div>

                    <pre style="
                        color:#E5E7EB;
                        padding:14px;
                        margin:0;
                        white-space:pre-wrap;
                        font-family:Consolas;
                    ">{code}</pre>

                </div>
                """
            )

            return placeholder

        text = re.sub(
            r"```(\w+)?\n(.*?)```",
            replace_code,
            text,
            flags=re.DOTALL,
        )

        # --------------------------------
        # HEADINGS
        # --------------------------------

        text = re.sub(
            r"^###### (.*)$",
            r"<h6>\1</h6>",
            text,
            flags=re.MULTILINE,
        )

        text = re.sub(
            r"^##### (.*)$",
            r"<h5>\1</h5>",
            text,
            flags=re.MULTILINE,
        )

        text = re.sub(
            r"^#### (.*)$",
            r"<h4>\1</h4>",
            text,
            flags=re.MULTILINE,
        )

        text = re.sub(
            r"^### (.*)$",
            r"<h3>\1</h3>",
            text,
            flags=re.MULTILINE,
        )

        text = re.sub(
            r"^## (.*)$",
            r"<h2>\1</h2>",
            text,
            flags=re.MULTILINE,
        )

        text = re.sub(
            r"^# (.*)$",
            r"<h1>\1</h1>",
            text,
            flags=re.MULTILINE,
        )

        # --------------------------------
        # BOLD
        # --------------------------------

        text = re.sub(
            r"\*\*(.*?)\*\*",
            r"<b>\1</b>",
            text,
        )

        # --------------------------------
        # ITALIC
        # --------------------------------

        text = re.sub(
            r"\*(.*?)\*",
            r"<i>\1</i>",
            text,
        )

        # --------------------------------
        # INLINE CODE
        # --------------------------------

        text = re.sub(
            r"`(.*?)`",
            r"""
            <code style="
                background:#1E293B;
                color:#60A5FA;
                padding:2px 5px;
                border-radius:5px;
            ">\1</code>
            """,
            text,
        )

        # --------------------------------
        # LINKS
        # --------------------------------

        text = re.sub(
            r"\[(.*?)\]\((.*?)\)",
            r'<a href="\2">\1</a>',
            text,
        )

        # --------------------------------
        # BLOCKQUOTE
        # --------------------------------

        text = re.sub(
            r"^> (.*)$",
            r"""
            <blockquote style="
                border-left:4px solid #3B82F6;
                padding-left:10px;
                color:#CBD5E1;
            ">\1</blockquote>
            """,
            text,
            flags=re.MULTILINE,
        )

        # --------------------------------
        # HORIZONTAL LINE
        # --------------------------------

        text = re.sub(
            r"^---$",
            "<hr>",
            text,
            flags=re.MULTILINE,
        )

        # --------------------------------
        # BULLET LIST
        # --------------------------------

        text = re.sub(
            r"^- (.*)$",
            r"• \1",
            text,
            flags=re.MULTILINE,
        )

        # --------------------------------
        # NUMBER LIST
        # --------------------------------

        text = re.sub(
            r"^\d+\.\s(.*)$",
            r"• \1",
            text,
            flags=re.MULTILINE,
        )

        # --------------------------------
        # NEW LINES
        # --------------------------------

        text = text.replace("\n", "<br>")

        # --------------------------------
        # RESTORE CODE BLOCKS
        # --------------------------------

        for i, block in enumerate(code_blocks):

            text = text.replace(
                f"__CODEBLOCK_{i}__",
                block,
            )

        return text

    @staticmethod
    def plain(text: str):

        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
        text = re.sub(r"\*(.*?)\*", r"\1", text)
        text = re.sub(r"`(.*?)`", r"\1", text)

        return text