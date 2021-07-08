release:
	-mkdir -p release/
	zip -r release/russian-stressmark.ankiaddon *.py manifest.json icons/

.PHONY: release
