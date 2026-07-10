# 外掛（Plugin）系統

[English](plugin-system.en.md) | 繁體中文

## 結構

每個外掛是 `app/plugins/<plugin_name>/` 底下的一個資料夾，包含：

- `manifest.json`：外掛名稱、版本、描述、作者。
- `plugin.py`：提供 `async def setup(bot)`，負責把 Cog 掛進 bot。
- `commands.py`（可選）：實際的指令 Cog 定義。

參考範例：[app/plugins/example_plugin/](../app/plugins/example_plugin/)。

## 載入流程

`app/plugins/loader.py` 的 `load_plugins(bot)` 會掃描 `app/plugins/*/manifest.json`，動態 import 對應的 `plugin.py` 並呼叫 `setup(bot)`，同時把外掛資訊註冊進 `app/plugins/registry.py` 的 `PluginRegistry`。

## 新增外掛

1. 複製 `example_plugin/` 資料夾並改名。
2. 修改 `manifest.json` 的 `name`/`version`/`description`。
3. 在 `commands.py` 撰寫指令 Cog。
4. 在 `plugin.py` 的 `setup()` 內 `add_cog`。

不需要修改 `app/bot.py`，loader 會自動掃描到新外掛。
