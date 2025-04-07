import logging
import sys
from typing import Optional


def setup_logging(
    level: str = "INFO",
    log_format: Optional[str] = None,
    date_format: Optional[str] = None,
) -> None:
    """
    Setup logging configuration

    Args:
        level (str, optional): Logging level. Defaults to "INFO".
        log_format (Optional[str], optional): Log format. Defaults to None.
        date_format (Optional[str], optional): Date format. Defaults to None.
    """
    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    if date_format is None:
        date_format = "%Y-%m-%d %H:%M:%S"

    # Convert string level to logging level
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level}")

    # Configure root logger
    logging.basicConfig(
        level=numeric_level, format=log_format, datefmt=date_format, stream=sys.stdout
    )
