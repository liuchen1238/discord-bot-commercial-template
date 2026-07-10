# Deployment Guide

English | [繁體中文](deployment.md)

## Docker Compose (development / small production)

```bash
docker compose up -d --build
```

This starts four services: `bot`, `api`, `db` (Postgres), and `redis`.

## Kubernetes

Example manifests live in [deploy/kubernetes/](../deploy/kubernetes/), including Deployments/Services for the bot and API, plus ConfigMap/Secret templates. Adjust the image, resource limits, and ingress for your actual cluster.

## systemd (single-machine deployment)

See [deploy/systemd.service](../deploy/systemd.service), suited for running directly on a VM without containers.

```bash
sudo cp deploy/systemd.service /etc/systemd/system/discord-bot.service
sudo systemctl daemon-reload
sudo systemctl enable --now discord-bot
```

## Railway

[deploy/railway/](../deploy/railway/) contains `railway.json`, deployable directly via the Railway CLI or GitHub integration.

## Environment variables

Set up `.env` (based on `.env.example`) before deploying. At minimum you need: `DISCORD_TOKEN`, `DATABASE_URL`, `STRIPE_API_KEY`, `STRIPE_WEBHOOK_SECRET`.
