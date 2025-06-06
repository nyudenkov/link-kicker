#!/bin/sh
uv run pybabel extract --input-dirs=. -o locales/link_kicker.pot
uv run pybabel update -d locales -D link_kicker -i locales/link_kicker.pot