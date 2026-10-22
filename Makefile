.PHONY: test pdf check

test:
	python3 scripts/validate.py

pdf: test
	python3 scripts/build_pdfs.py

check: test
	python3 scripts/build_pdfs.py --check
