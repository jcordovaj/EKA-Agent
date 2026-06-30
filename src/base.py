from pydantic import BaseModel, Field, UUID4
from datetime import datetime
from typing import Optional, Dict, Any, List, Literal

# DOM 1: Document Management

class Document(BaseModel):
    document_id: UUID4
    filename: str
    binary_hash: str  # Nivel 1
    current_version: int
    manifesto: Dict[str, Any]  # Aquí vive la configuración: parser, política, etc.
    status: Literal["INBOX", "PROCESSING", "READY", "FAILED"]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class DocumentVersion(BaseModel):
    version_id: UUID4
    document_id: UUID4
    version_number: int
    content_hash: str  # Nivel 2
    change_summary: Optional[Dict[str, Any]] = None

# DOM 2: Knowledge Processing

class Chunk(BaseModel):
    chunk_id: UUID4
    version_id: UUID4
    chunk_index: int
    chunk_hash: str  # Nivel 3
    content: str
    context_header: str
    is_active: bool = True

class Embedding(BaseModel):
    embedding_id: UUID4
    chunk_id: UUID4
    embedding_model: str
    vector: List[float] # O el tipo específico de pgvector si usamos una lib

class ChunkLineage(BaseModel):
    lineage_id: UUID4
    old_chunk_id: Optional[UUID4]
    new_chunk_id: UUID4
    change_type: Literal["UNCHANGED", "UPDATED", "CREATED", "DELETED"]

# DOM 3 & 4: Control & Agent

class ProcessingJob(BaseModel):
    job_id: UUID4
    document_id: UUID4
    stage: str
    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED"]
    details: Optional[Dict[str, Any]] = None