PYTHON_PATH = ./src

tests:
	@PYTHON_PATH=$(PYTHON_PATH) pytest -v

tests_no_performance:
	@PYTHON_PATH=$(PYTHON_PATH) pytest -v -k "not test_large_triangulation_performance"