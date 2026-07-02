from sqlalchemy import Column, String, Integer, JSON, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID, JSONB, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class DocumentORM(Base):
    __tablename__ = 'documents'
    document_id = Column(UUID(as_uuid=True), primary_key=True)
    filename = Column(String, nullable=False)
    binary_hash = Column(String, nullable=False)
    current_version = Column(Integer, default=1)
    manifesto = Column(JSONB)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ChunkORM(Base):
    __tablename__ = 'chunks'
    chunk_id = Column(UUID(as_uuid=True), primary_key=True)
    version_id = Column(UUID(as_uuid=True))
    chunk_index = Column(Integer)
    chunk_hash = Column(String)
    content = Column(String)
    context_header = Column(String)
    is_active = Column(Boolean, default=True)

class EmbeddingORM(Base):
    __tablename__ = 'embeddings'
    embedding_id = Column(UUID(as_uuid=True), primary_key=True)
    chunk_id = Column(UUID(as_uuid=True), ForeignKey('chunks.chunk_id'))
    embedding_model = Column(String)
    # 1536 size std de modelos como text-embedding-3-small
    vector = Column(Vector(1536))