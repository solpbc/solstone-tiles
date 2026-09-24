# solstone for Tiles

A [Tiles](https://tiles.run) plugin for [solstone](https://solstone.app) that lets the agent in Tiles search and read your journal, on the computer where your journal lives.

The plugin is three small files: `plugin.json`, an `mcp.json` that points at your journal's local address, `http://127.0.0.1:7659/mcp`, and one skill, `solstone-memory`, that teaches the model how to use the journal's tools. There is no key to paste. You connect Tiles on your journal's own page, and you choose what the agent may see there. You can change that or disconnect the agent at any time in your journal's agents app.

## Status

Early. No journal release serves this address yet; the plugin works once one does. It also needs a Tiles build with plugin support (the canary channel today).

## Install

```
tiles plugin install https://github.com/solpbc/solstone-tiles/releases/download/v0.1.0/solstone-tiles-0.1.0.zip
```

Restart Tiles, then type `/mcp-auth solstone__journal` in the chat. Your browser opens your journal's page. Enter the pairing code from your journal's agents app and choose what Tiles may see.

## Build

```
make install   # checks for python3 and zip
make ci        # checks the plugin files
make zip       # writes dist/solstone-tiles-<version>.zip
```

## License

AGPL-3.0-only. See [`LICENSE`](LICENSE).
