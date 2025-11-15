import os

from src.common.config import AppConfig, get_config


def test_from_env_defaults(monkeypatch):
    """AppConfig.from_env should fall back to sensible defaults when env vars are missing."""

    monkeypatch.delenv("FESTUS_ENV", raising=False)
    monkeypatch.delenv("FESTUS_LOG_LEVEL", raising=False)

    cfg = AppConfig.from_env()

    assert cfg.environment == "development"
    assert cfg.log_level == "INFO"


def test_get_config_returns_appconfig(monkeypatch):
    """get_config should return an AppConfig instance using the current environment."""

    monkeypatch.setenv("FESTUS_ENV", "test")
    monkeypatch.setenv("FESTUS_LOG_LEVEL", "DEBUG")

    cfg = get_config()

    assert isinstance(cfg, AppConfig)
    assert cfg.environment == "test"
    assert cfg.log_level == "DEBUG"

