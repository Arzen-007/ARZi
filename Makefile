lint:
	ruff check --select E,F,W,B,C4,I --ignore E402,E501,E712,B904,B905,I001 --exclude=ARZi/uploads ARZi/ migrations/ tests/
	isort --profile=black --check-only --skip=ARZi/uploads --skip-glob **/node_modules ARZi/ tests/
	yarn --cwd ARZi/themes/admin lint
	black --check --diff --exclude=ARZi/uploads --exclude=node_modules .
	prettier --check 'ARZi/themes/*/assets/**/*'
	prettier --check '**/*.md'

format:
	isort --profile=black --skip=ARZi/uploads --skip-glob **/node_modules ARZi/ tests/
	black --exclude=ARZi/uploads --exclude=node_modules .
	prettier --write 'ARZi/themes/**/assets/**/*'
	prettier --write '**/*.md'

test:
	pytest -rf --cov=ARZi --cov-context=test --cov-report=xml \
		--ignore-glob="**/node_modules/" \
		--ignore=node_modules/ \
		-W ignore::sqlalchemy.exc.SADeprecationWarning \
		-W ignore::sqlalchemy.exc.SAWarning \
		-n auto
	bandit -r ARZi -x ARZi/uploads --skip B105,B322
	pipdeptree

coverage:
	coverage html --show-contexts

serve:
	python serve.py

shell:
	python manage.py shell

translations-init:
	# make translations-init lang=af
	pybabel init -i messages.pot -d ARZi/translations -l $(lang)

translations-extract:
	pybabel extract -F babel.cfg -k lazy_gettext -k _l -o messages.pot .

translations-update:
	pybabel update --ignore-obsolete -i messages.pot -d ARZi/translations

translations-compile:
	pybabel compile -f -d ARZi/translations

translations-lint:
	dennis-cmd lint ARZi/translations
