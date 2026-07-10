# Discord Bot Commercial Template

[English](README.en.md) | 繁體中文

一個可直接拿來當作**商業化 Discord Bot** 起點的專案模板，內建：

- Discord.py Cog 架構 + 分層 Service/Repository 設計
- 訂閱制計費（Stripe）與方案／功能旗標
- FastAPI 管理後台 API（webhook、guild/user 管理）
- Alembic 資料庫遷移、SQLAlchemy 非同步 ORM
- 排程任務（訂閱檢查、清理、報表）
- 外掛（Plugin）系統，方便擴充指令
- Docker / Docker Compose / Kubernetes / systemd 部署範例
- GitHub Actions CI（test / lint / deploy）

> ⚠️ 本專案為**模板骨架**，商業邏輯（金流串接細節、風控、真實資料庫遷移內容等）需依實際需求補完，勿直接上線使用。

## 快速開始

```bash
cp .env.example .env
pip install -r requirements.txt
python -m app.main
```

## 目錄結構

詳見 [docs/architecture.md](docs/architecture.md)。

## 授權

MIT License，詳見 [LICENSE](LICENSE)。
