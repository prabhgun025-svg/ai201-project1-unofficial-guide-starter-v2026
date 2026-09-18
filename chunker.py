
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in week 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents into chunks. ⚠️ REPLACE THE BODY OF THIS IN MILESTONE 3.

    Strategy:
    - Markdown files (city_guides): Split on ## headers — each section is its own chunk
    - Posts with reply markers (advice_threads): Split on '--- reply' patterns
    - Short posts (campus_life): Keep as one chunk per document
    
    Rationale:
    - The 800-char fixed size cuts through logical section boundaries (headers, replies)
    - City guides are structured around "## Getting there", "## Where to stay" etc.
    - Advice threads have independent replies that should be separate chunks
    - Campus life posts are ~300 chars and coherent — one per chunk
    - Eliminates tiny "trash" chunks (2-24 chars) from uneven divisions
    
    Produced by: chunker.py::split_documents
    """
    chunks: list[Chunk] = []
    
    for doc in documents:
        text = doc.text
        doc_chunks = []
        
        # Check if this is a markdown file (city_guides)
        if doc.source.endswith('.md'):
            # Split on markdown headers (##)
            # Include the header with its content
            parts = text.split('## ')
            
            if parts[0].strip():  # If there's content before the first ##
                doc_chunks.append(parts[0].strip())
            
            for part in parts[1:]:
                chunk_text = '## ' + part.strip()
                if chunk_text.strip():
                    doc_chunks.append(chunk_text)
        
        # Check for reply markers (advice_threads)
        elif '--- reply' in text:
            # Split on the reply marker pattern
            # Don't include bare thread header before first reply
            parts = text.split('--- reply')
            
            for part in parts[1:]:
                chunk_text = ('--- reply' + part).strip()
                if chunk_text.strip():
                    doc_chunks.append(chunk_text)
        
        # For other documents (campus_life style or plain advice_threads without replies)
        else:
            # Skip bare thread headers (lines starting with "THREAD:")
            # They're just questions without answers
            lines = text.split('\n')
            filtered_lines = []
            for line in lines:
                if not line.strip().startswith('THREAD:'):
                    filtered_lines.append(line)
            
            # Rejoin and split on paragraph breaks
            text = '\n'.join(filtered_lines)
            paragraphs = text.split('\n\n')
            for para in paragraphs:
                para = para.strip()
                if para:  # Only add non-empty paragraphs
                    doc_chunks.append(para)
        
        # Convert chunks to Chunk objects
        for index, chunk_text in enumerate(doc_chunks):
            # Only include chunks that have meaningful content (more than 20 chars)
            if len(chunk_text) > 20:
                chunks.append(
                    Chunk(
                        text=chunk_text,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::split_documents",
                    )
                )
    
    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))

