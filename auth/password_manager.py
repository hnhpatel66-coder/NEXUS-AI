import bcrypt


class PasswordManager:
    """
    Professional Password Manager
    -----------------------------
    • Hash Password
    • Verify Password
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Convert plain password into secure bcrypt hash.
        """

        salt = bcrypt.gensalt(rounds=12)

        hashed = bcrypt.hashpw(
            password.encode("utf-8"),
            salt
        )

        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(
        password: str,
        hashed_password: str
    ) -> bool:
        """
        Verify user password.
        """

        try:

            return bcrypt.checkpw(
                password.encode("utf-8"),
                hashed_password.encode("utf-8")
            )

        except Exception:

            return False