# Plugin System

English | [繁體中文](plugin-system.md)

## Structure

Each plugin is a folder under `app/plugins/<plugin_name>/`, containing:

- `manifest.json`: plugin name, version, description, author.
- `plugin.py`: provides `async def setup(bot)`, responsible for attaching the Cog to the bot.
- `commands.py` (optional): the actual command Cog definitions.

See [app/plugins/example_plugin/](../app/plugins/example_plugin/) for a reference implementation.

## Loading flow

`load_plugins(bot)` in `app/plugins/loader.py` scans `app/plugins/*/manifest.json`, dynamically imports the corresponding `plugin.py`, and calls `setup(bot)`, while also registering the plugin's info into the `PluginRegistry` in `app/plugins/registry.py`.

## Adding a plugin

1. Copy the `example_plugin/` folder and rename it.
2. Update `name`/`version`/`description` in `manifest.json`.
3. Write your command Cog in `commands.py`.
4. Call `add_cog` inside `setup()` in `plugin.py`.

No changes to `app/bot.py` are needed — the loader automatically discovers new plugins.
