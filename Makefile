.PHONY: default

default:
	@echo "Commands:"
	@echo " make clean # Clean all byte compiled files"
	@echo " make start # Start the script"

isvirtualenv:
	@if [ -z "$(VIRTUAL_ENV)" ]; then echo "ERROR: Not in a virtualenv." 1>&2; exit 1; fi

install: isvirtualenv
	pip install -r requirements.txt

start: isvirtualenv
	$(VIRTUAL_ENV)/bin/python stockrobo.py

clean: isvirtualenv
	find . -name "*.pyc" -exec rm -f '{}' \;