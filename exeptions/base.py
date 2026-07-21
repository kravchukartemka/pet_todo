class AppException(Exception):
    """Базовое исключение приложения."""

    status_code: int = 400
    detail: str = "Application error"

    def __init__(self, detail: str | None = None):
        if detail:
            self.detail = detail