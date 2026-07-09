# 計費系統

## 流程

1. 使用者在 Discord 執行 `/upgrade`（[app/cogs/billing.py](../app/cogs/billing.py)）。
2. `BillingService.create_checkout_session` 呼叫 Stripe 建立 Checkout Session，回傳付款連結。
3. 使用者完成付款後，Stripe 觸發 `checkout.session.completed` webhook，打到 `POST /webhooks/stripe`（[app/api/routes/webhooks.py](../app/api/routes/webhooks.py)）。
4. Webhook handler 呼叫 `SubscriptionService.activate`，把該 guild 的訂閱狀態寫入資料庫。
5. 之後任何指令透過 `PermissionService.has_plan()`（[app/core/permissions.py](../app/core/permissions.py) 的 `require_plan` decorator）判斷該 guild 是否有權限使用進階功能。

## 方案（Plan）

預設方案定義在 [scripts/seed_data.py](../scripts/seed_data.py)：`free` / `pro` / `enterprise`，各自有 `features` JSON 欄位描述可用功能與限制。

## 取消訂閱

Stripe 的 `customer.subscription.deleted` 事件會觸發 `SubscriptionService.cancel`，將訂閱狀態設為 `cancelled`，該 guild 會被視為回到 Free 方案。
