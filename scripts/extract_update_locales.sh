#!/bin/sh
pybabel extract --input-dirs=. -o locales/link_kicker.pot
pybabel update -d locales -D link_kicker -i locales/link_kicker.pot