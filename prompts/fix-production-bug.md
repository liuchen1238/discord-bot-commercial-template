# Prompt: 修復正式環境 Bug

用途：標準化修 bug 的流程，避免 AI agent 亂改範圍外的程式碼。

```
正式環境出現以下問題：<描述錯誤現象、log、reproduce 步驟>

請依序：
1. 先只讀程式碼定位問題根因，不要急著改。app/cogs -> app/services -> app/database/repositories 是主要資料流向。
2. 找到根因後，用最小範圍的修改處理，不要順便重構無關程式碼。
3. 補上一個能重現此 bug 的測試（tests/），確認修復後測試通過。
4. 如果是資料庫資料不一致造成的問題，評估是否需要一次性的資料修復 script（放在 scripts/），而不是改 migration 歷史。
5. 說明這個 bug 的根因與修復方式，不需要額外加註解在程式碼裡解釋「做了什麼」。
```
