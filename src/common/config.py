"""Central configuration loader for the Festus CCDI project.

This module is intentionally lightweight and uses only the standard library so
it can be imported without additional dependencies. It can later be migrated
to pydantic-based settings if desired.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class AppConfig:
    """Application configuration.

    Add fields here as the codebase grows. Values are loaded from environment
    variables with sensible defaults for local development.
    """

    environment: str = "development"
    log_level: str = "INFO"
    # Example: database_url: Optional[str] = None

    @classmethod
    def from_env(cls) -> "AppConfig":
        """Construct configuration from environment variables."""

        return cls(
            environment=os.getenv("FESTUS_ENV", "development"),
            log_level=os.getenv("FESTUS_LOG_LEVEL", "INFO"),
            # database_url=os.getenv("FESTUS_DATABASE_URL"),
        )


def get_config() -> AppConfig:
    """Return the current application configuration.

    In small scripts, calling :func:`get_config` directly is sufficient. In
    larger applications, you may wish to create a single global instance and
    pass it explicitly where needed.
    """

    return AppConfig.from_env()

