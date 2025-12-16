PYTHON_PATH = ./src

tests:
	@PYTHON_PATH=$(PYTHON_PATH) pytest -v

tests_no_large_triangulation:
	@PYTHON_PATH=$(PYTHON_PATH) pytest -v -k "not test_large_triangulation_performance"

coverage:
	@PYTHON_PATH=$(PYTHON_PATH) coverage run -m pytest
	@PYTHON_PATH=$(PYTHON_PATH) coverage report
	@PYTHON_PATH=$(PYTHON_PATH) coverage html

coverage_no_large_triangulation:
	@PYTHON_PATH=$(PYTHON_PATH) coverage run -m pytest -k "not test_large_triangulation_performance"
	@PYTHON_PATH=$(PYTHON_PATH) coverage report
	@PYTHON_PATH=$(PYTHON_PATH) coverage html

webdoc:
	@PYTHON_PATH=$(PYTHON_PATH) pdoc3 --html --force --output docs src/app

web_service:
	export FLASK_APP=$(PYTHON_PATH)/app/app.py
	@PYTHON_PATH=$(PYTHON_PATH) flask run