# 架構總覽

## 分層設計

```
Cogs (Discord 指令層)
   ↓
Services (商業邏輯)
   ↓
Repositories (資料存取)
   ↓
Models (SQLAlchemy ORM)
```

- **app/cogs/**：使用者透過 Discord 互動的入口，只負責解析輸入、呼叫 service、回覆訊息。
- **app/services/**：商業邏輯（訂閱判斷、計費、通知等），不直接碰 Discord API 或 SQL。
- **app/database/repositories/**：封裝 SQLAlchemy 查詢，service 層透過 repository 存取資料。
- **app/models/**：ORM 定義，對應資料庫 schema。
- **app/api/**：獨立於 Bot 進程的 FastAPI 管理後台/Webhook 服務，與 Bot 共用 services/database 層。
- **app/jobs/**：APScheduler 排程任務（訂閱狀態檢查、清理、報表）。
- **app/plugins/**：可插拔的擴充指令模組，透過 manifest.json 描述並由 loader 動態載入。
- **app/middlewares/**：FastAPI middleware（rate limit、audit log、錯誤處理、維護模式）。
- **app/workers/**：Redis 佇列 + 背景任務消費者，用於卸載耗時工作。

## 兩個進程

1. `python -m app.main`：啟動 Discord Bot（`app/bot.py`）。
2. `uvicorn app.api.main:app`：啟動管理後台 API，供 Stripe webhook、前端後台呼叫。

兩者共用同一份 `app/database`、`app/models`、`app/services`，透過 `DATABASE_URL` 連到同一個資料庫。
