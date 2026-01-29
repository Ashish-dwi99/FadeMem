# FadeMem — Biologically‑Inspired Memory Layer for Agents

FadeMem is a **drop‑in replacement for mem0** that adds biologically‑inspired forgetting, dual‑layer memory (SML/LML), LLM‑guided conflict resolution, and memory fusion. It is designed to be API‑compatible with mem0 while improving long‑term relevance and storage efficiency.

## Research Highlights (FadeMem paper)
- **~45% storage reduction** with adaptive forgetting and consolidation.
- **Improved multi‑hop reasoning and retrieval** on Multi‑Session Chat, LoCoMo, and LTI‑Bench.
- **Dual‑layer memory** with differential decay rates and promotion/demotion logic.

Reference: *FadeMem: Biologically‑Inspired Forgetting for Efficient Agent Memory* (arXiv:2601.18642).

## Key Features
- **mem0‑compatible API** (`Memory`, `AsyncMemory`, `MemoryClient`).
- **Adaptive decay** using access‑modulated exponential forgetting.
- **Conflict resolution** (COMPATIBLE / CONTRADICTORY / SUBSUMES / SUBSUMED).
- **Memory fusion** to consolidate redundant facts into stronger, generalized memories.
- **Strength‑weighted retrieval** (similarity × strength).

## Quickstart (Gemini + Qdrant)

### 1) Install dependencies
```bash
pip install qdrant-client google-generativeai google-genai pydantic
```

### 2) Run Qdrant (local)
```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 3) Set your Gemini API key
```bash
export GEMINI_API_KEY=your_key_here
```

### 4) Use FadeMem
```python
from fadem import Memory

memory = Memory(config={
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "collection_name": "fadem_memories",
            "embedding_model_dims": 768
        }
    },
    "llm": {"provider": "gemini", "config": {"model": "gemini-3-flash-preview"}},
    "embedder": {"provider": "gemini", "config": {"model": "text-embedding-004"}}
})

messages = [
    {"role": "user", "content": "I’m vegetarian and allergic to peanuts."},
    {"role": "assistant", "content": "Got it!"}
]
memory.add(messages, user_id="user_123")

results = memory.search("What are my dietary restrictions?", user_id="user_123")
print(results["results"][0]["memory"])
```

## Claude Code Integration (MCP Server)

FadeMem includes an MCP (Model Context Protocol) server that allows Claude Code to use it as a persistent memory layer.

### 1) Install FadeMem with MCP support

```bash
cd /path/to/fademem
pip install -e ".[mcp,qdrant,gemini]"
# or for OpenAI:
pip install -e ".[mcp,qdrant,openai]"
```

### 2) Configure Claude Code

Add FadeMem to your Claude Code MCP settings. Open your Claude Code config file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following configuration:

```json
{
  "mcpServers": {
    "fadem-memory": {
      "command": "fadem-mcp",
      "env": {
        "GEMINI_API_KEY": "your-gemini-api-key"
      }
    }
  }
}
```

Or if using OpenAI:

```json
{
  "mcpServers": {
    "fadem-memory": {
      "command": "fadem-mcp",
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key"
      }
    }
  }
}
```

### 3) Optional Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FADEM_LLM_MODEL` | `gemini-3-flash-preview` / `gpt-4o-mini` | LLM model for extraction/conflict |
| `FADEM_EMBEDDER_MODEL` | `text-embedding-004` / `text-embedding-3-small` | Embedding model |
| `FADEM_QDRANT_PATH` | `~/.fadem/qdrant` | Local Qdrant storage path |
| `FADEM_COLLECTION` | `fadem_memories` | Qdrant collection name |
| `FADEM_HISTORY_DB` | `~/.fadem/history.db` | SQLite history database path |
| `FADEM_ENABLE_FORGETTING` | `true` | Enable biologically-inspired decay |
| `FADEM_SML_DECAY_RATE` | `0.15` | Short-term memory decay rate |
| `FADEM_LML_DECAY_RATE` | `0.02` | Long-term memory decay rate |

### 4) Available Tools in Claude Code

Once connected, Claude Code will have access to these memory tools:

- **`add_memory`** — Store new facts, preferences, or context
- **`search_memory`** — Recall relevant memories by semantic search
- **`get_all_memories`** — List all stored memories for a user
- **`get_memory`** — Retrieve a specific memory by ID
- **`update_memory`** — Update an existing memory
- **`delete_memory`** — Remove a memory
- **`get_memory_stats`** — View memory statistics
- **`apply_memory_decay`** — Trigger the forgetting algorithm

### 5) Restart Claude Code

After saving the config, restart Claude Code. The FadeMem memory tools will appear in Claude's available tools.

---

## Configuration Notes
- **Embedding dims**: `text-embedding-004` returns 768 dims (default in config).
- **LLM prompts** for extraction, conflict, and fusion live in `fadem/utils/prompts.py`.
- **Decay settings** and thresholds live in `fadem/configs/base.py` under `fadem`.

## Repository Structure
```
fadem/
  memory/       # Memory + AsyncMemory + client
  core/         # decay, conflict, fusion, retrieval
  db/           # SQLite history + metadata
  vector_stores/# Qdrant + in-memory store
  embeddings/   # Gemini/OpenAI/simple embedders
  llms/         # Gemini/OpenAI/mock LLMs
  utils/        # prompts + factories + helpers
```

