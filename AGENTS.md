# AGENTS.md

A Tiles plugin for the solstone journal: `plugin.json`, `mcp.json`, and one skill under `skills/solstone-memory/`. There is no code beyond `scripts/check.py`, which checks the files against what the Tiles plugin loader accepts.

## Rules for changing this repo

The loader rules below were read from the Tiles source at canary `5dd3afc`. Re-check them when Tiles changes.

- `mcp.json` holds one server, `journal`, with `type` and `url` only. Never add `headers`: any header turns off the client's OAuth sign-in. Never put a variable or placeholder in the URL: the loader rejects it.
- The URL is `http://127.0.0.1:7659/mcp`, the journal's fixed local address. Plain `http` is accepted only for a loopback host.
- Both manifests use the Agent Plugins 1.0.0 schema. A 1.1.0 plugin's servers are not started.
- The plugin name decides the sign-in command (`/mcp-auth <name>__journal`). If you rename the plugin, update the skill and README in the same change; `make ci` checks the skill.
- The skill must never tell the model to send journal content to a web search or any other tool outside the journal.
- Keep the skill short and concrete. It is read by small local models.

## Done means

`make ci` passes, and `make zip` produces an archive that `tiles plugin install` accepts.

## Never

- Push a release or tag without operator approval.
- Add analytics, telemetry or any network call beyond the journal's loopback address.
