async def get_source_documents(self, query, kb_ids, cosine_thresh=None, top_k=None):
    if not top_k:
        top_k = self.top_k
    source_documents = []
    t1 = time.time()
    filter = lambda metadata: metadata['kb_id'] in kb_ids
    # filter = None
    debug_logger.info(f"query: {query}")
    docs = await self.faiss_client.search(kb_ids, query, filter=filter, top_k=top_k)
    debug_logger.info(f"query_docs: {len(docs)}")
    t2 = time.time()
    debug_logger.info(f"faiss search time: {t2 - t1}")
    for idx, doc in enumerate(docs):
        if doc.metadata['file_name'].endswith('.faq'):
            faq_dict = doc.metadata['faq_dict']
            doc.page_content = f"{faq_dict['question']}：{faq_dict['answer']}"
            nos_keys = faq_dict.get('nos_keys')
            doc.metadata['nos_keys'] = nos_keys
        doc.metadata['retrieval_query'] = query  # 添加查询到文档的元数据中
        doc.metadata['embed_version'] = self.embeddings.getModelVersion
        source_documents.append(doc)
    if cosine_thresh:
        source_documents = [item for item in source_documents if float(item.metadata['score']) > cosine_thresh]

    return source_documents