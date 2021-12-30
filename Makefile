PYTHON = python3

.PHONY: clean
clean:
	rm -rf docs/*

.PHONY: build
build: clean
	make -j 2 run-trials run-experiments
	$(PYTHON) src/build_index_html.py

.PHONY: run-trials
run-trials:
	$(PYTHON) src/run_trials.py

.PHONY: run-experiments
run-experiments:
	$(PYTHON) src/run_experiments.py

.PHONY: build-index-html
build-index-html:
	$(PYTHON) src/build_index_html.py

