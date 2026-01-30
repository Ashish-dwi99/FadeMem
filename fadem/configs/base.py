import os
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class VectorStoreConfig(BaseModel):
    provider: str = Field(default="qdrant")
    config: Dict[str, Any] = Field(
        default_factory=lambda: {
            "path": os.path.join(os.path.expanduser("~"), ".fadem", "qdrant"),
            "collection_name": "fadem_memories",
        }
    )


class LLMConfig(BaseModel):
    provider: str = Field(default="gemini")
    config: Dict[str, Any] = Field(
        default_factory=lambda: {
            "model": "gemini-2.0-flash",
            "temperature": 0.1,
            "max_tokens": 1024,
        }
    )


class EmbedderConfig(BaseModel):
    provider: str = Field(default="gemini")
    config: Dict[str, Any] = Field(default_factory=lambda: {"model": "gemini-embedding-001"})


class GraphStoreConfig(BaseModel):
    provider: Optional[str] = Field(default=None)
    config: Optional[Dict[str, Any]] = Field(default=None)


class EchoMemConfig(BaseModel):
    """Configuration for EchoMem multi-modal encoding."""
    enable_echo: bool = True
    auto_depth: bool = True  # Auto-detect echo depth based on content importance
    default_depth: str = "medium"  # shallow, medium, deep
    reecho_on_access: bool = False  # Re-process on retrieval (expensive but strengthening)
    reecho_threshold: int = 3  # Re-echo after N accesses
    # Strength multipliers for each depth
    shallow_multiplier: float = 1.0
    medium_multiplier: float = 1.3
    deep_multiplier: float = 1.6
    # Use question_form embedding for primary vector (better query matching)
    use_question_embedding: bool = True


class FadeMemConfig(BaseModel):
    enable_forgetting: bool = True
    sml_decay_rate: float = 0.15
    lml_decay_rate: float = 0.02
    access_dampening_factor: float = 0.5
    promotion_access_threshold: int = 3
    promotion_strength_threshold: float = 0.7
    forgetting_threshold: float = 0.1
    conflict_similarity_threshold: float = 0.85
    fusion_similarity_threshold: float = 0.90
    enable_fusion: bool = True
    use_tombstone_deletion: bool = True


class MemoryConfig(BaseModel):
    vector_store: VectorStoreConfig = Field(default_factory=VectorStoreConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    embedder: EmbedderConfig = Field(default_factory=EmbedderConfig)
    graph_store: GraphStoreConfig = Field(default_factory=GraphStoreConfig)
    history_db_path: str = Field(
        default_factory=lambda: os.path.join(os.path.expanduser("~"), ".fadem", "history.db")
    )
    collection_name: str = "fadem_memories"
    embedding_model_dims: int = 3072  # gemini-embedding-001 default dimensions
    version: str = "v1.2"  # Updated for EchoMem
    custom_fact_extraction_prompt: Optional[str] = None
    custom_conflict_prompt: Optional[str] = None
    custom_fusion_prompt: Optional[str] = None
    custom_echo_prompt: Optional[str] = None
    fadem: FadeMemConfig = Field(default_factory=FadeMemConfig)
    echo: EchoMemConfig = Field(default_factory=EchoMemConfig)
