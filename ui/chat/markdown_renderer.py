import re


class MarkdownRenderer:

    @staticmethod
    def render(text: str) -> str:

        if not text:
            return ""

        # =========================
        # BOLD **text**
        # =========================
        text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)

        # =========================
        # ITALIC *text*
        # =========================
        text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", text)

        # =========================
        # INLINE CODE `code`
        # =========================
        text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)

        # =========================
        # HEADINGS #, ##, ###
        # =========================
        text = re.sub(r"^### (.*)", r"<h3>\1</h3>", text, flags=re.M)
        text = re.sub(r"^## (.*)", r"<h2>\1</h2>", text, flags=re.M)
        text = re.sub(r"^# (.*)", r"<h1>\1</h1>", text, flags=re.M)

        # =========================
        # QUOTES
        # =========================
        text = re.sub(r"> (.*)", r"<blockquote>\1</blockquote>", text)

        # =========================
        # LINKS [text](url)
        # =========================
        text = re.sub(
            r"\[(.*?)\]\((.*?)\)",
            r'<a href="\2">\1</a>',
            text
        )

        # =========================
        # LINE BREAKS
        # =========================
        text = text.replace("\n", "<br>")

        # =========================
        # FINAL WRAP STYLE
        # =========================
        return f"""
        <div style="
            font-size:14px;
            line-height:1.6;
            color:white;
        ">
            {text}
        </div>
        """