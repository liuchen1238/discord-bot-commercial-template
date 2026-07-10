# Prompt: 新增付費方案功能

[English](add-commercial-feature.en.md) | 繁體中文

用途：新增一個只有特定訂閱方案（Pro/Enterprise）才能使用的功能。

```
我要新增一個指令 /<command_name>，只有 <plan> 以上的方案才能用。

需求：
1. 在 app/cogs/<相關cog>.py 新增指令，使用 app.core.permissions.require_plan("<plan>") decorator 包住。
2. 商業邏輯寫在對應的 app/services/*.py，不要寫在 cog 裡。
3. 若需要新資料表/欄位，修改 app/models/，並產生 alembic migration。
4. 補上 tests/test_services/ 或 tests/test_commands/ 的測試。
5. 更新 docs/billing.md 如果影響到方案功能描述。
```
