default:help
py := uv run python
ruff := uv run ruff

help:
	@echo "USAGE"
	@echo "  make <commands>"
	@echo ""
	@echo "AVAILABLE COMMANDS"
	@echo "  run		Start a bot"
	@echo "  format		Run ruff format"
	@echo "  check		Run ruff check"
	@echo "  lint		Run ruff check and format"


# ========
# Commands
# ========

run:
	$(py) -m main

format:
	$(ruff) format .

check:
	$(ruff) check .

lint: check format