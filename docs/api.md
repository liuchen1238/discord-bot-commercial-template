# 管理後台 API

啟動：

```bash
uvicorn app.api.main:app --reload
```

## 端點

| Method | Path | 說明 |
| --- | --- | --- |
| GET | `/health` | 健康檢查 |
| GET | `/guilds/{guild_id}` | 查詢單一 guild 資料 |
| GET | `/users/{discord_id}` | 查詢/建立使用者資料 |
| POST | `/billing/checkout` | 建立 Stripe Checkout Session |
| POST | `/webhooks/stripe` | Stripe webhook 接收端點 |

## Middleware

依序套用（見 [app/api/main.py](../app/api/main.py)）：

1. `ErrorHandlerMiddleware`：統一錯誤格式。
2. `MaintenanceMiddleware`：維護模式時擋掉非 `/health` 請求。
3. `RateLimitMiddleware`：每 IP 每分鐘請求數限制。

Schema 定義在 [app/api/schemas/](../app/api/schemas/)，皆為 Pydantic model。
