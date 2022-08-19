# Link Kicker

<a href="https://www.producthunt.com/posts/link-kicker-bot?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-link&#0045;kicker&#0045;bot" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=356346&theme=light" alt="Link&#0032;Kicker&#0032;Bot - Bot&#0032;that&#0032;can&#0032;help&#0032;you&#0032;remember&#0032;about&#0032;your&#0032;abandoned&#0032;articles | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

Do you have a problem with just forgetting to read the articles you've saved links to like me? 
This bot was created to solve this problem.

➡ [Start using a bot](https://t.me/link_kicker_bot)

## Installation and local launch
1. Clone this repo: `git clone https://github.com/nyudenkov/link-kicker`
2. Create `.env` with `cp .env.example .env` and fill it out
3. Create `commands.yaml` with `cp commands.yaml.example commands.yaml` and change command descriptions if you want
4. Install [poetry](https://python-poetry.org/) on your machine (or just `pip install poetry` in env)
5. Run `poetry install` in the root folder for requirements installing
6. Run `sh scripts/compile_locales.sh` in the root folder for compiling locales
7. Run `aerich upgrade` in the root folder for running migrations
8. Run `make run`
