# Prompt: 程式碼審查檢查清單

[English](code-review.en.md) | 繁體中文

用途：審查一個 PR 或一段 diff 是否符合本專案架構慣例。

```
請審查這份 diff，檢查以下項目：

1. 分層是否正確：cog 不應直接操作資料庫或呼叫第三方 SDK；service 不應直接處理 discord.Interaction。
2. 方案限制的指令是否使用了 require_plan()，而不是自行判斷。
3. 資料庫變更是否有對應的 alembic migration。
4. 是否有新增未使用的抽象、過度設計、或多餘的錯誤處理（trust internal guarantees）。
5. 是否有安全疑慮：webhook 簽章驗證、SQL injection、密鑰是否寫死在程式碼裡。
6. 是否補上對應測試。

請列出具體檔案與行號的問題，並標註嚴重程度。
```
