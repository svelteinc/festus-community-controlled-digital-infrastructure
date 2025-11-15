"""Shared logging configuration for the Festus CCDI project."""

from __future__ import annotations

import logging
from typing import Optional


def configure_logging(level: str = "INFO") -> None:
    """Configure root logging for the application.

    This sets a basic formatting convention suitable for both local
    development and simple containerized deployments.

    Unlike :func:`logging.basicConfig`, this function will update the root
    logger level even if handlers have already been configured (for example
    by a test runner or framework).
    """

    target_level = getattr(logging, level.upper(), logging.INFO)
    root_logger = logging.getLogger()
    root_logger.setLevel(target_level)

    if not root_logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        )
        root_logger.addHandler(handler)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Get a logger instance with the given name.

    If *name* is ``None``, the root logger is returned.
    """

    return logging.getLogger(name)

