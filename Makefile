.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

virtualenv:
	python3 -m venv --prompt '|> kreator <| ' venv
	venv/bin/pip install -r requirements-dev.txt
	venv/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source venv/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=kreator \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t kreator:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
