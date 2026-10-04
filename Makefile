RUFF_VERSION := 0.15.20

.PHONY: lint format fix run-client

check:
	uvx ruff@$(RUFF_VERSION) check .

format:
	uvx ruff@$(RUFF_VERSION) format .

fix:
	uvx ruff@$(RUFF_VERSION) check . --fix

run-client: 
	uv run python -m homesync.client.main

run-server:
	uv run python -m homesync.server.main