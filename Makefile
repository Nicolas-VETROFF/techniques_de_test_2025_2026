PYTHON_PATH = ./src

tests:
	@PYTHON_PATH=$(PYTHON_PATH) pytest -v

minitests:
	@PYTHON_PATH=$(PYTHON_PATH) pytest -v -k "not test_large_triangulation_performance"

coverage:
	@PYTHON_PATH=$(PYTHON_PATH) coverage run -m pytest
	@PYTHON_PATH=$(PYTHON_PATH) coverage report
	@PYTHON_PATH=$(PYTHON_PATH) coverage html

minicoverage:
	@PYTHON_PATH=$(PYTHON_PATH) coverage run -m pytest -k "not test_large_triangulation_performance"
	@PYTHON_PATH=$(PYTHON_PATH) coverage report
	@PYTHON_PATH=$(PYTHON_PATH) coverage html

doc:
	@PYTHON_PATH=$(PYTHON_PATH) pdoc3 --html --force --output docs src/app

web:
	export FLASK_APP=$(PYTHON_PATH)/app/app.py
	@PYTHON_PATH=$(PYTHON_PATH) flask run

ruff:
	@ruff check