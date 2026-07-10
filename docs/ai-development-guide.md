# AI 輔助開發指南

[English](ai-development-guide.en.md) | 繁體中文

本專案設計為方便 AI coding agent（如 Claude Code）協作開發。`prompts/` 目錄下有幾個常用任務的提示詞範本：

- [prompts/add-commercial-feature.md](../prompts/add-commercial-feature.md)：新增一個需要付費方案才能使用的功能。
- [prompts/add-plugin.md](../prompts/add-plugin.md)：新增一個外掛。
- [prompts/fix-production-bug.md](../prompts/fix-production-bug.md)：修復正式環境 bug 的標準流程。
- [prompts/code-review.md](../prompts/code-review.md)：程式碼審查檢查清單。

## 給 AI agent 的專案慣例

- 指令邏輯只放在 `app/cogs/`，商業邏輯一律下沉到 `app/services/`，資料庫存取一律經過 `app/database/repositories/`。
- 新增資料庫欄位/表格：先改 `app/models/`，再用 `alembic revision --autogenerate` 產生遷移檔，不要手動寫 SQL。
- 需要方案限制的指令，使用 `app/core/permissions.py` 的 `require_plan()` decorator，不要在 cog 裡自己判斷 plan。
- 新增外部服務串接，放在 `app/integrations/`，service 層呼叫 integration，不要讓 cog 直接呼叫第三方 SDK。
- 修改後請執行 `pytest` 與 `ruff check .`。
