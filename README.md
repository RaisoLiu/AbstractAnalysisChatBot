# AbstractAnalysisChatBot
AbstractAnalysisChatBot 是一個利用 AI 聊天機器人 (基於 OpenAI 的 GPT-3) 來分析學術論文摘要的工具，並自動生成分析結果的 HackMD 筆記。

## 功能
1. 自動提取論文的關鍵信息，包括：欲解決的問題、使用的方法、最終成果、關鍵字。
2. 利用 GPT-3 機器人提供智能解析。
3. 自動生成包含所有問題答案的 HackMD 筆記。

## 如何使用
### 安裝
確保你的 Python 環境已經安裝了所有必要的依賴，如 OpenAI 的 GPT-3 SDK、PyHackMD SDK。

### 使用
```python
from paper import PaperAnalyzer

analyzer = PaperAnalyzer(chatgpt_api_token='YOUR_CHATGPT_API_TOKEN', hackmd_api_token='YOUR_HACKMD_API_TOKEN')

title = "您的論文標題"
abstract = "您的論文摘要"

link = analyzer.analyze_abstract(title, abstract)

print(link)
```
### 結果
執行程式後，你將會得到一個 HackMD 的筆記連結，該筆記包含所有問題答案。

example: https://hackmd.io/@raiso/B1ItKAtrn
