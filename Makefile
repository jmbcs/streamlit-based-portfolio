include .env
.PHONY: help
SHELL := /bin/bash
current_branch := $(shell git rev-parse --abbrev-ref HEAD)

help: ## Show this help
	@echo -e "\033[33mCommands\033[0m"
	@awk -F ':.*?## ' '/^[a-zA-Z0-9_-.]+:.*?##/ {printf "\033[36m- %-30s\033[0m| %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: ## Clean repo
	@find . -type d \( -name "__pycache__" -o -name ".mypy_cache" -o -name ".pytest_cache" -o -name ".coverage" -o -name "*.egg-info" -o -name ".tox" -o -name ".venv" -o -name "build" -o -name "dist" \) -exec rm -rf {} +

run:
	@streamlit run portfolio/__main__.py