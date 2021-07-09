pip:
	pip3 install -r requirements/requirements.txt

venv:
	python3 -m venv venv
	source venv/bin/activate

pre-commit:
	pip3 install requirements/requirements.txt
	pre-commit install

py-format: pre-commit
	pre-commit run black --all-files
