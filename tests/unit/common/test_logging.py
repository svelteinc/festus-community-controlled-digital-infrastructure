import logging

from src.common.logging import configure_logging, get_logger


def test_configure_logging_sets_level():
    """configure_logging should set the root logger level based on the provided string."""

    configure_logging(level="DEBUG")
    root_logger = logging.getLogger()

    assert root_logger.level == logging.DEBUG


def test_get_logger_returns_logger_instance():
    """get_logger should return a Logger instance for the given name."""

    logger = get_logger("festus.test")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "festus.test"

