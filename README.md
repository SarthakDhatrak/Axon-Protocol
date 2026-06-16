<div align="center">
  <img src="axon-dashboard/public/favicon.svg" width="80" alt="Axon Logo"/>
  <h1>Axon Protocol</h1>
  <p><strong>The open-source coordination backend for building, auditing, and scaling multi-agent AI fleets.</strong></p>
</div>

<br/>

<div align="center">
  <img src="axon-demo/demo.gif" alt="Axon Twin Agents Coordination Demo" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
</div>

<br/>

## 🚀 One-Command Install

Get started instantly with our Python SDK:

```bash
pip install axon-protocol
```

Or deploy the local development server and UI dashboard with zero configuration:

```bash
npm install -g axon-protocol-server
axon dev
```

---

## ⚡ Why Axon Protocol? (Axon vs. Traditional DBs)

When building autonomous AI agents, standard databases aren't enough. Agents face race conditions, need semantic memory, and require auditable reasoning chains. 

| Capability | Traditional DB (e.g., PostgreSQL) | Axon Protocol |
|------------|-----------------------------------|---------------|
| **Memory** | Raw rows & columns | Built-in Vector Memory & Semantic Search |
| **Coordination** | Standard transactions | Distributed Agent Locks (prevent race conditions) |
| **Auditability** | Access logs | Cryptographic Reasoning Receipts (Chained) |
| **Messaging** | Pub/Sub overhead | Native P2P Agent Messaging |
| **Visibility** | Requires custom dashboards | Real-time WebSockets & Built-in Developer UI |

---

## ✨ Core Features

- 🧠 **Persistent Semantic Memory**: Agents can store and semantically search memories using native vector embeddings.
- 🚦 **Distributed Locks**: High-performance concurrency control. Prevent two agents from writing to the same file or hitting the same API simultaneously.
- 📜 **Reasoning Receipts**: Cryptographically chained logs of what your agents did, why they did it, and what the outcome was.
- 💬 **Peer-to-Peer Messaging**: Let agents talk to each other and coordinate via decentralized topics.
- 🛠️ **Universal Integrations**: Native support for **LangChain**, **CrewAI**, and an **MCP Server** for Claude Desktop.
- 🖥️ **Real-Time Dashboard**: Watch your agent fleets think, coordinate, and act live from a beautiful glassmorphism web console.

---

## 📚 Quick Start

### 1. Initialize the Client

```python
import asyncio
from axon import AxonClient

client = AxonClient(api_key="your-api-key", base_url="http://localhost:8000")
```

### 2. Prevent Race Conditions

```python
async def safe_db_write():
    # If another agent holds 'db-write', this waits safely
    lock = await client.locks.acquire("db-write", timeout=30)
    if lock:
        try:
            print("Safely writing to database...")
        finally:
            await client.locks.release("db-write")
```

### 3. Store and Search Memory

```python
# Store a memory
await client.memory.store("User prefers concise, bulleted responses.", scope="project")

# Retrieve semantically relevant memories
memories = await client.memory.search("What is the preferred output format?")
print(memories[0].content) # "User prefers concise, bulleted responses."
```

---

## 🤝 Community & Support

Developed by **Zuggu Group**. 

We are fully open-source (MIT License). If you're building multi-agent systems and need enterprise support or managed cloud hosting, reach out to us at [hello@zuggu.tech](mailto:hello@zuggu.tech).
