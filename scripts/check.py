#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 sol pbc
"""Check the plugin files against what the Tiles plugin loader accepts."""

import json
import re
import sys

PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
PLUGIN_KEYS = {
    "$schema", "name", "version", "description", "homepage",
    "repository", "license", "keywords", "author", "extensions",
}
URL = "http://127.0.0.1:7659/mcp"

failures = []


def check(condition, message):
    if not condition:
        failures.append(message)


plugin = json.load(open("plugin.json"))
check(plugin.get("$schema") == PLUGIN_SCHEMA, "plugin.json must use the 1.0.0 schema")
check(set(plugin) <= PLUGIN_KEYS, f"plugin.json has unknown keys: {sorted(set(plugin) - PLUGIN_KEYS)}")
check(re.fullmatch(r"[a-z0-9-]+", plugin.get("name", "")) is not None, "plugin name must be lowercase")

mcp = json.load(open("mcp.json"))
check(mcp.get("$schema") == MCP_SCHEMA, "mcp.json must use the 1.0.0 schema")
servers = mcp.get("mcpServers", {})
check(list(servers) == ["journal"], "mcp.json must define exactly one server, journal")
journal = servers.get("journal", {})
check(journal.get("type") == "streamable-http", "journal must be streamable-http")
check(journal.get("url") == URL, f"journal url must be {URL}")
# Any header turns off the client's OAuth sign-in.
check("headers" not in journal, "journal must not set headers")
check(set(journal) <= {"type", "url"}, "journal may set only type and url")

skill = open("skills/solstone-memory/SKILL.md").read()
check(skill.startswith("---\nname: solstone-memory\n"), "skill frontmatter must name solstone-memory")
check(f"/mcp-auth {plugin.get('name')}__journal" in skill, "skill must name the sign-in command for this plugin name")

if failures:
    for failure in failures:
        print(f"FAIL {failure}")
    sys.exit(1)
print("plugin files ok")
