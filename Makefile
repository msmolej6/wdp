PYTHON := python3.6

.PHONY: help
help:
	@echo "Available commands"
	@echo " make run <list_number> <task_number>"
	@echo "Example"
	@echo " make run lista6 zadanie6"

.PHONY: run
run:
	@$(PYTHON) -m src.$(word 2,$(MAKECMDGOALS)).$(word 3,$(MAKECMDGOALS))

%:
	@:
