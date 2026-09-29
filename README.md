# solstone for Tiles

A [Tiles](https://tiles.run) plugin for [solstone](https://solstone.app) that lets the agent in Tiles search and read your journal, on the computer where your journal lives.

The plugin is three small files: `plugin.json`, an `mcp.json` that points at your journal's local address, `http://127.0.0.1:7659/mcp`, and one skill, `solstone-memory`, that teaches the model how to use the journal's tools. There is no key to paste. You connect Tiles on your journal's own page, and you choose what the agent may see there. You can change that or disconnect the agent at any time in your journal's agents app.

## Status

Works with journal 2.0.24 and later, on the computer where your journal lives. It needs a Tiles build with plugin support (the canary channel today).

## Install

```
tiles plugin install https://github.com/solpbc/solstone-tiles/releases/download/v0.1.0/solstone-tiles-0.1.0.zip
```

## Connect Tiles to your journal

1. In your journal, open agents › connect an agent and make a pairing code. If it asks where this agent is, choose "on this computer". If it isn't offered, turn on agents on this computer in the agents app first. The code works once and lasts 10 minutes, and your journal lets an agent start connecting only while a code is open.
2. In the Tiles chat, type `/mcp-auth solstone__journal`. Your browser opens your journal's page.
3. Choose your whole journal or only some facets, and at least one kind of material. Then enter the code and connect.

If the Tiles chat stays on "Processing..." after you connect, quit Tiles and open it again. The connection is kept.

## Build

```
make install   # checks for python3 and zip
make ci        # checks the plugin files
make zip       # writes dist/solstone-tiles-<version>.zip
```

## License

AGPL-3.0-only. See [`LICENSE`](LICENSE).
