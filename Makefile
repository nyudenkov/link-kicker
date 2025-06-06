default:help
py := uv run python

help:
	@echo "USAGE"
	@echo "  make <commands>"
	@echo ""
	@echo "AVAILABLE COMMANDS"
	@echo "  run		Start a bot"
	@echo "  black		Run black"
	@echo "  isort		Run isort"
	@echo "  lint		Run black and isort"


# ========
# Commands
# ========

run:
	$(py) -m main

black:
	$(py) -m black .

isort:
	$(py) -m isort .


lint: black isort