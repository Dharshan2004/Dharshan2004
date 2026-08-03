# Kannan Priyadharshan (Dharshan)

**AI Engineer · Agentic Infrastructure**  
CS @ Nanyang Technological University · Expected 2029  
AI Engineer @ Cyber Sierra

---

### What I'm building

- **Agent infrastructure @ Cyber Sierra** — the internal platform that lets the product team query production codebases in natural language and run packaged agent skills to surface edge cases hidden in the code. Retrieval is agentic rather than a pre-built index, so nothing goes stale on commit. Most of this lives in private repos — happy to walk through it.
- **Contributing to LiteLLM** — [PR #31076](https://github.com/BerriAI/litellm/pull/31076) merged upstream; working through progressively larger issues in the same area.
- **Cursor for PMs** — early validation. Interviewing product managers to find the one workflow worth eliminating.

---

### What I care about

I build agent systems that run against production code and real users: retrieval that has to be correct, guardrails that have to hold, and evaluation that tells you when they don't. Right now that means agent infrastructure at Cyber Sierra, an AI-powered GRC platform in Singapore — an internal codebase-querying platform, and a customer-facing knowledge base that assembles product guides with code-cited evidence, gates publication behind automated misleading-content checks, and answers users through a chat agent constrained to disclaim or refuse rather than speculate. Refusing well turned out to be harder than answering well.

Before that: high-throughput data pipelines at eLife (AWS SQS, gRPC, Kubernetes), ETL infrastructure at Netvirta (AWS EKS, 100k+ SKU onboarding), and a document ingestion pipeline for Skills@CCDS — PDF classification via OpenAI embeddings, schema-constrained LLM extraction with Zod validation, and human-in-the-loop verification before profile commit.

At core, I'm a problem solver. The domain matters less than the depth — I started in low-latency market infrastructure, and the same instincts (determinism, isolation, measuring the thing rather than guessing at it) are what I now bring to agents.

---

### Stack

```
Agentic     LLM Orchestration · Multi-Agent Systems · Agentic RAG · Semantic Retrieval · Eval Frameworks
Languages   Python · TypeScript · Go · C++
Backend     FastAPI · gRPC · HTTP/3 · WebSockets · Redis · PostgreSQL
Cloud       AWS (EKS, SQS) · Kubernetes · Docker · Terraform
ML          OpenAI Embeddings · LangChain · Qdrant · pgvector · GenAI pipelines
```

---

### Open source

| Contribution | What it does |
|---|---|
| [**LiteLLM #31076**](https://github.com/BerriAI/litellm/pull/31076) — *merged* | Centralised the OpenAI → Anthropic usage translation so prompt-cache token counts survive every response path in the Anthropic messages adapter. Cache hits were being dropped from usage reporting, which quietly breaks cost accounting for anyone billing on cached tokens. |

---

### Projects

| Project | What it does | Stack |
|---------|-------------|-------|
| [shopee-live-producer](https://github.com/Dharshan2004/shopee-live-producer) | Live-commerce agent that acts as a **producer, not a chatbot** — classifies each buyer comment and decides whether to auto-answer, escalate to the host, flag policy risk, or stay silent. A grounding gate blocks any reply not backed by product-fact IDs above a confidence threshold; host-confirmed answers extend session memory without overwriting the seeded catalogue. 🥉 Sea × OpenAI Codex Regional Hackathon 2026. | Next.js · LangChain DeepAgents · OpenAI · Supabase Realtime |
| [wayfinder](https://github.com/Dharshan2004/wayfinder) | AI career navigation engine. Extracts skills from a résumé, diffs them against target-role requirements via pgvector semantic search, and generates a 4-week upskilling roadmap where every task links to a discovered resource. Top 13 / 100+ teams at NTU Techfest 2026. | Next.js · pgvector · OpenAI |
| [pollpulse-tn](https://github.com/Dharshan2004/pollpulse-tn) | Real-time NLP sentiment pipeline for Tamil Nadu 2026 election forecasting. Aggregates and classifies social signals to surface swing-district indicators. | Python · NLP · Supabase |
| [trace-zero](https://github.com/Dharshan2004/trace-zero) | Real-time execution simulator on nanosecond-accurate orderbook capture. Every strategy runs in its own isolated exchange instance so one lane's price impact can't contaminate another; monotonic clocks as the authoritative timing source; WebSocket streaming to a live front end. The domain is optimal execution — the engineering is deterministic replay and state isolation. | Python · FastAPI · Next.js · NumPy |

<details>
<summary><b>Earlier work</b></summary>

| Project | What it does | Stack |
|---------|-------------|-------|
| [market-replay](https://github.com/Dharshan2004/market-replay) | Nanosecond-accurate top-of-book capture & replay. Monotonic clock timestamps as the authoritative timing source, pluggable handler system, JSONL storage with file rotation. | Python · WebSocket · Binance |
| [capm-portfolio-optimizer](https://github.com/Dharshan2004/capm-portfolio-optimizer) | Beta estimation via linear regression + Markowitz MVO + Monte Carlo simulation across 10,000 weight combinations. | Python · NumPy · SciPy |

</details>

---

### Currently reading

- Andrej Karpathy — How LLMs Work (building from first principles)
- Nassim Taleb — *Antifragile*
- Bhagavad Gita Chapter 14 — on the three modes of nature

---

### Beyond the terminal

Head of Technology (Backend) for NTU CCDS TOP'26 — leading 7 backend engineers on a platform for 900 incoming students. Director of the Quantitative Finance Academy at NTU — curriculum on market microstructure and ML in finance for 80+ members. Varsity cricket. Long-term goal: a coffee estate in Kodaikanal.

---

📍 Singapore → Hong Kong (HKU exchange, Jan 2027) · **Open to Summer 2027 roles**

🌐 [kpriyadharshan.dev](https://kpriyadharshan.dev) &nbsp;·&nbsp; 💼 [linkedin.com/in/kpriyadharshan](https://linkedin.com/in/kpriyadharshan) &nbsp;·&nbsp; 📧 [kpd2204@gmail.com](mailto:kpd2204@gmail.com)
