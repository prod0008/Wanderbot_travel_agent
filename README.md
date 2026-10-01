# 🤖 WanderBot — AI Travel Concierge

> An intelligent travel assistant built with the **Strands Agents SDK** and deployed on **Amazon Bedrock AgentCore**.

WanderBot is Horizon Travel's AI-powered travel concierge that answers pre-trip questions about baggage, check-in, cabin classes, and cancellation policies — while handling real-time calculations for costs, tips, totals, and currency estimates using a built-in calculator tool.

---

## ✨ Features

- 🧮 **Built-in Calculator Tool** — Accurately computes flight costs, hotel totals, baggage fees, and cabin upgrades without LLM hallucination.
- 🧠 **Amazon Nova 2 Lite** — Powered by AWS's latest foundational model for fast, travel-focused responses.
- 🚀 **Cloud-Native Deployment** — Deployed to Amazon Bedrock AgentCore Runtime for scalable, production-ready inference.
- 🔄 **Local Development Loop** — Iterate instantly with `agentcore dev` before shipping to the cloud.
- 📦 **Structured Outputs** — Pydantic-validated JSON responses for reliable downstream UI integration (implemented in advanced modules).

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Agent Framework** | Strands Agents SDK (`strands-agents`) |
| **Built-in Tools** | Strands Tools (`strands-agents-tools`) |
| **Runtime** | Amazon Bedrock AgentCore (`bedrock-agentcore`) |
| **Foundational Model** | Amazon Nova 2 Lite (`us.amazon.nova-2-lite-v1:0`) |
| **Data Validation** | Pydantic v2 |
| **Language** | Python 3.12 |
| **Cloud Provider** | AWS |

---

## 📂 Project Structure

```text
wanderbot-ai-travel-concierge/
├── app.py                  # Main entrypoint (BedrockAgentCoreApp + Strands Agent)
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── screenshots/            # Demo screenshots
│   ├── local_test.png
│   └── cloud_deploy.png
└── README.md               # This file
