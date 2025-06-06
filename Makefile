default:help
py := uv run python

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
	$(py) -m ruff format .

check:
	$(py) -m ruff check .

lint: check format