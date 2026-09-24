# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 sol pbc

VERSION := $(shell python3 -c 'import json; print(json.load(open("plugin.json"))["version"])')
ZIP := dist/solstone-tiles-$(VERSION).zip
FILES := plugin.json mcp.json skills/solstone-memory/SKILL.md LICENSE

.PHONY: install test ci format clean zip

install:
	@command -v python3 >/dev/null || { echo "python3 is required"; exit 1; }
	@command -v zip >/dev/null || { echo "zip is required"; exit 1; }

test:
	python3 scripts/check.py

ci: test

format:
	@echo "nothing to format"

zip: test
	mkdir -p dist
	rm -f $(ZIP)
	zip -X -q $(ZIP) $(FILES)
	@echo $(ZIP)

clean:
	rm -rf dist
