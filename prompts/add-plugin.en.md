# Prompt: Add a plugin

English | [繁體中文](add-plugin.md)

Purpose: add a standalone set of commands as a plugin, without touching core code.

```
I want to add a plugin called <plugin_name>, which does: <description>

Please follow the structure of app/plugins/example_plugin/:
1. Create app/plugins/<plugin_name>/manifest.json (name/version/description/author).
2. Create commands.py, defining a discord.py Cog with the needed slash commands.
3. Create plugin.py, providing async def setup(bot) to attach the Cog.
4. No need to modify app/plugins/loader.py — it auto-discovers new plugins.
5. Add basic tests if applicable.
```
