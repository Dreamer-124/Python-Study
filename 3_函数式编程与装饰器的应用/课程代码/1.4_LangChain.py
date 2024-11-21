# cache.py
@lru_cache(maxsize=CASSANDRA_SEMANTIC_CACHE_EMBEDDING_CACHE_SIZE)
def _cache_embedding(text: str) -> List[float]:
    return self.embedding.embed_query(text=text)

self._get_embedding = _cache_embedding

@_async_lru_cache(maxsize=CASSANDRA_SEMANTIC_CACHE_EMBEDDING_CACHE_SIZE)
async def _acache_embedding(text: str) -> List[float]:
    return await self.embedding.aembed_query(text=text)