<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/AI-Memory-purple?style=for-the-badge" alt="AI Memory">
</p>

<h1 align="center">
  <br>
  🧠 FadeMem + EchoMem
  <br>
</h1>

<h3 align="center">
  Biologically-Inspired Memory Layer for AI Agents
</h3>

<p align="center">
  <b>FadeMem</b> brings human-like forgetting & consolidation.<br>
  <b>EchoMem</b> adds multi-modal encoding for stronger retention.<br>
  Together, they create the most advanced memory system for AI agents.
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-claude-code-integration">Claude Code</a> •
  <a href="#-api-reference">API</a> •
  <a href="#-research">Research</a>
</p>

---

## 🎯 Why FadeMem + EchoMem?

Traditional AI memory systems store everything forever. Humans don't work that way—and neither should your AI agents.

| Problem | FadeMem + EchoMem Solution |
|---------|---------------------------|
| Memory bloat over time | **Adaptive forgetting** - irrelevant memories fade naturally |
| All memories treated equal | **Dual-layer system** - important memories get promoted to long-term |
| Conflicting information | **LLM-guided conflict resolution** - newer info updates older |
| Weak retrieval on varied queries | **Multi-modal echo encoding** - multiple retrieval paths per memory |
| Shallow encoding | **Importance-based depth** - critical info gets deeper processing |

---

## ✨ Features

### 🔄 FadeMem — Decay & Consolidation

```
┌─────────────────────────────────────────────────────────┐
│                    FadeMem Layer                        │
├─────────────────────────────────────────────────────────┤
│  📥 Short-term Memory (SML)                             │
│     • Fast decay rate (0.15)                            │
│     • New memories land here                            │
│     • Frequently accessed → promoted                    │
│                    ↓                                    │
│  📦 Long-term Memory (LML)                              │
│     • Slow decay rate (0.02)                            │
│     • Important, consolidated memories                  │
│     • Persists across sessions                          │
└─────────────────────────────────────────────────────────┘
```

- **Adaptive Decay** — Memories fade based on time and access patterns
- **Dual-Layer Architecture** — SML for recent, LML for important
- **Automatic Promotion** — Frequently accessed memories get promoted
- **Conflict Resolution** — LLM detects contradictions and updates
- **Memory Fusion** — Related memories consolidate into stronger ones
- **~45% Storage Reduction** — Compared to store-everything approaches

### 🔊 EchoMem — Encoding & Retrieval

```
Input: "User prefers TypeScript over JavaScript"
                    │
                    ▼
        ┌───────────────────────┐
        │   Echo Processing     │
        │                       │
        │  Depth: MEDIUM        │
        │  (preference keyword) │
        └───────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│                  Stored Memory                          │
├─────────────────────────────────────────────────────────┤
│  raw: "User prefers TypeScript over JavaScript"         │
│  paraphrase: "TypeScript is the user's preferred..."    │
│  keywords: ["typescript", "javascript", "preference"]   │
│  implications: ["values type safety", "modern tooling"] │
│  question_form: "What language does the user prefer?"   │
│  strength: 1.3x (medium depth bonus)                    │
└─────────────────────────────────────────────────────────┘
```

- **Multi-Modal Encoding** — Stores paraphrase, keywords, implications, question form
- **Auto Depth Detection** — Shallow (1.0x) / Medium (1.3x) / Deep (1.6x)
- **Query-Optimized Retrieval** — Question-form embeddings match queries better
- **Echo-Based Re-ranking** — Boosts results matching keywords/implications
- **Re-Echo on Access** — Frequently accessed memories get stronger encoding

### 📊 Echo Depth Levels

| Depth | Trigger | Processing | Strength |
|-------|---------|------------|----------|
| **Shallow** | Generic info | Keywords only (no LLM) | 1.0x |
| **Medium** | Preferences, dates | + Paraphrase | 1.3x |
| **Deep** | Credentials, "important", numbers | + Implications, Q&A | 1.6x |

---

## 🚀 Quick Start

### Installation

```bash
pip install fadem
```

Or install from source:

```bash
git clone https://github.com/yourusername/fademem.git
cd fademem
pip install -e ".[gemini,qdrant]"
```

### Set Your API Key

```bash
export GEMINI_API_KEY="your-api-key"
```

### Basic Usage

```python
from fadem import Memory

# Initialize with defaults (Gemini + Qdrant)
memory = Memory()

# Add memories from conversation
memory.add(
    messages=[
        {"role": "user", "content": "I'm a vegetarian and allergic to peanuts."},
        {"role": "assistant", "content": "Got it!"}
    ],
    user_id="user_123"
)

# Search memories
results = memory.search(
    "What are my dietary restrictions?",
    user_id="user_123"
)

print(results["results"][0]["memory"])
# → "User is vegetarian and allergic to peanuts"
```

### With EchoMem Enabled (Default)

```python
from fadem import Memory
from fadem.configs.base import MemoryConfig, EchoMemConfig

config = MemoryConfig(
    echo=EchoMemConfig(
        enable_echo=True,
        auto_depth=True,           # Auto-detect importance
        use_question_embedding=True # Better query matching
    )
)

memory = Memory(config)

# High-importance memory → DEEP echo (1.6x strength)
memory.add("My API key is sk-abc123", user_id="user_123")

# Preference → MEDIUM echo (1.3x strength)
memory.add("I prefer dark mode", user_id="user_123")

# Generic info → SHALLOW echo (1.0x strength)
memory.add("The weather is nice", user_id="user_123")
```

---

## 🔧 Claude Code Integration

FadeMem works as an MCP server for Claude Code, giving Claude persistent memory across sessions.

### Setup

Add to your Claude Code config (`~/.claude.json`):

```json
{
  "mcpServers": {
    "fadem-memory": {
      "command": "python",
      "args": ["-m", "fadem.mcp_server"],
      "env": {
        "GEMINI_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Available Tools

| Tool | Description |
|------|-------------|
| `add_memory` | Store a new memory |
| `search_memory` | Find relevant memories |
| `get_all_memories` | List all stored memories |
| `get_memory` | Get a specific memory by ID |
| `update_memory` | Update memory content |
| `delete_memory` | Remove a memory |
| `get_memory_stats` | Get storage statistics |
| `apply_memory_decay` | Run decay algorithm |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         Your AI Agent                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FadeMem + EchoMem                            │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                     EchoMem Layer                         │  │
│  │         (Encoding & Retrieval Enhancement)                │  │
│  │                                                           │  │
│  │  • Multi-modal echo encoding                              │  │
│  │  • Importance-based depth selection                       │  │
│  │  • Query-optimized embeddings                             │  │
│  │  • Echo-based search re-ranking                           │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                     FadeMem Layer                         │  │
│  │           (Decay & Consolidation Engine)                  │  │
│  │                                                           │  │
│  │  • Dual-layer memory (SML/LML)                            │  │
│  │  • Adaptive strength decay                                │  │
│  │  • Conflict resolution & fusion                           │  │
│  │  • Promotion/demotion logic                               │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │   Embedder   │  │     LLM      │  │    Vector Store      │  │
│  │   (Gemini/   │  │  (Gemini/    │  │  (Qdrant/In-memory)  │  │
│  │   OpenAI)    │  │   OpenAI)    │  │                      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📖 API Reference

### Memory Class

```python
from fadem import Memory

memory = Memory(config=None)  # Uses defaults if no config
```

#### `add(messages, user_id, **kwargs)`

Add memories from messages or raw text.

```python
# From conversation
memory.add(
    messages=[{"role": "user", "content": "I love Python"}],
    user_id="user_123",
    categories=["preferences"],
    echo_depth="deep"  # Override auto-detection
)

# From raw text
memory.add("User's birthday is March 15", user_id="user_123")
```

#### `search(query, user_id, **kwargs)`

Search for relevant memories.

```python
results = memory.search(
    query="What programming language?",
    user_id="user_123",
    limit=10,
    min_strength=0.1,
    use_echo_rerank=True  # Use echo metadata for better ranking
)
```

#### `apply_decay(scope=None)`

Run the forgetting algorithm.

```python
result = memory.apply_decay(scope={"user_id": "user_123"})
# {"decayed": 5, "forgotten": 2, "promoted": 1}
```

#### `get_stats(user_id=None)`

Get memory statistics including echo info.

```python
stats = memory.get_stats(user_id="user_123")
# {
#   "total": 42,
#   "sml_count": 30,
#   "lml_count": 12,
#   "avg_strength": 0.73,
#   "echo_stats": {"shallow": 15, "medium": 20, "deep": 7}
# }
```

---

## ⚙️ Configuration

### Full Configuration Example

```python
from fadem.configs.base import (
    MemoryConfig,
    VectorStoreConfig,
    LLMConfig,
    EmbedderConfig,
    FadeMemConfig,
    EchoMemConfig,
)

config = MemoryConfig(
    # Vector store
    vector_store=VectorStoreConfig(
        provider="qdrant",  # or "memory" for in-memory
        config={
            "host": "localhost",
            "port": 6333,
            "collection_name": "my_memories",
        }
    ),

    # LLM for extraction & conflict resolution
    llm=LLMConfig(
        provider="gemini",  # or "openai"
        config={
            "model": "gemini-2.0-flash",
            "temperature": 0.1,
        }
    ),

    # Embeddings
    embedder=EmbedderConfig(
        provider="gemini",
        config={"model": "gemini-embedding-001"}
    ),
    embedding_model_dims=3072,

    # FadeMem settings
    fadem=FadeMemConfig(
        enable_forgetting=True,
        sml_decay_rate=0.15,
        lml_decay_rate=0.02,
        promotion_access_threshold=3,
        forgetting_threshold=0.1,
        conflict_similarity_threshold=0.85,
    ),

    # EchoMem settings
    echo=EchoMemConfig(
        enable_echo=True,
        auto_depth=True,
        default_depth="medium",
        use_question_embedding=True,
        shallow_multiplier=1.0,
        medium_multiplier=1.3,
        deep_multiplier=1.6,
    ),
)

memory = Memory(config)
```

---

## 📚 Research

FadeMem is based on the paper:

> **FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory**
>
> arXiv:2601.18642

### Key Results

| Metric | Improvement |
|--------|-------------|
| Storage Reduction | ~45% |
| Multi-hop Reasoning | +12% accuracy |
| Retrieval Precision | +8% on LTI-Bench |

### Biological Inspiration

FadeMem mimics human memory processes:

- **Ebbinghaus Forgetting Curve** → Exponential decay
- **Spaced Repetition** → Access boosts strength
- **Sleep Consolidation** → SML → LML promotion
- **Interference Theory** → Conflict resolution

EchoMem mimics human encoding:

- **Production Effect** → Saying/echoing improves retention
- **Elaborative Encoding** → Deeper processing = stronger memory
- **Multiple Retrieval Cues** → More paths to recall

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

```bash
# Clone the repo
git clone https://github.com/yourusername/fademem.git
cd fademem

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  <b>Built with 🧠 for smarter AI agents</b>
</p>

<p align="center">
  <a href="https://github.com/yourusername/fademem">GitHub</a> •
  <a href="https://github.com/yourusername/fademem/issues">Issues</a> •
  <a href="https://twitter.com/yourusername">Twitter</a>
</p>
