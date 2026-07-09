# Prompt: 新增外掛

用途：以外掛（plugin）形式新增一組獨立的指令，不動到核心程式碼。

```
我要新增一個外掛叫 <plugin_name>，功能是：<描述>

請依照 app/plugins/example_plugin/ 的結構：
1. 建立 app/plugins/<plugin_name>/manifest.json（name/version/description/author）。
2. 建立 commands.py，定義 discord.py Cog 與所需的 slash commands。
3. 建立 plugin.py，提供 async def setup(bot) 掛載 Cog。
4. 不需要修改 app/plugins/loader.py，它會自動掃描新外掛。
5. 補上簡單測試（如適用）。
```
