# 部署指南

## Docker Compose（開發/小型正式環境）

```bash
docker compose up -d --build
```

會啟動四個服務：`bot`、`api`、`db` (Postgres)、`redis`。

## Kubernetes

範例 manifests 放在 [deploy/kubernetes/](../deploy/kubernetes/)，包含 Bot / API 的 Deployment、Service，以及 ConfigMap/Secret 範本。依實際叢集調整 image、資源限制與 ingress。

## systemd（單機部署）

參考 [deploy/systemd.service](../deploy/systemd.service)，適合直接跑在一台 VM 上、不用容器的情境。

```bash
sudo cp deploy/systemd.service /etc/systemd/system/discord-bot.service
sudo systemctl daemon-reload
sudo systemctl enable --now discord-bot
```

## Railway

[deploy/railway/](../deploy/railway/) 內含 `railway.json`，可直接用 Railway CLI 或 GitHub 整合部署。

## 環境變數

部署前務必設定 `.env`（參考 `.env.example`），至少需要：`DISCORD_TOKEN`、`DATABASE_URL`、`STRIPE_API_KEY`、`STRIPE_WEBHOOK_SECRET`。
