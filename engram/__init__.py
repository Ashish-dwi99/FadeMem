"""FadeMem package exports.

FadeMem: Biologically-inspired memory for AI agents
- FadeMem: Dual-layer (SML/LML) with natural decay
- EchoMem: Multi-modal encoding for stronger retention
- CategoryMem: Dynamic hierarchical category organization
"""

from fadem.memory.main import Memory
from fadem.memory.client import MemoryClient
from fadem.memory.async_memory import AsyncMemory
from fadem.core.category import CategoryProcessor, Category, CategoryType, CategoryMatch
from fadem.core.echo import EchoProcessor, EchoDepth, EchoResult
from fadem.configs.base import MemoryConfig, FadeMemConfig, EchoMemConfig, CategoryMemConfig

__version__ = "0.1.3"  # CategoryMem release
__all__ = [
    # Main classes
    "Memory",
    "MemoryClient",
    "AsyncMemory",
    # CategoryMem
    "CategoryProcessor",
    "Category",
    "CategoryType",
    "CategoryMatch",
    # EchoMem
    "EchoProcessor",
    "EchoDepth",
    "EchoResult",
    # Config
    "MemoryConfig",
    "FadeMemConfig",
    "EchoMemConfig",
    "CategoryMemConfig",
]
