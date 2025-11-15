# Configuration

This directory stores configuration files and environment templates for the Festus CCDI project.

Guidelines:
- Store secrets only in untracked `.env` files, never in version control.
- Provide `.template` variants (e.g., `festus.env.template`) to document required variables.
- Centralize config loading in `src/common/config.py`.

