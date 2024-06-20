#creating chunks and indices of text documents 
import os 
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

from retro_pytorch.retrieval import text_folder_to_chunks_, chunks_to_index_and_embed

import faiss 

#create chunks and chunk start indices
stats = text_folder_to_chunks_(
    folder = 'text_docs',
    glob = '**/*.txt',
    chunks_memmap_path = 'train.chunks.dat',
    seqs_memmap_path = 'train.seq.dat',
    doc_ids_memmap_path = 'train.doc_ids.dat',  # document ids are needed for filtering out neighbors belonging to same document appropriately during computation of nearest neighbors
    chunk_size = 64,
    seq_len = 2048,
    max_chunks = 1_000_000,
    max_seqs = 100_000
)
print(stats)

#convert chunks into embeddings and faiss index 
index, embeddings = chunks_to_index_and_embed(
    num_chunks = 1000,
    chunk_size = 64,
    chunk_memmap_path = 'train.chunks.dat'
)

faiss.write_index(index, 'index.dat')

#NOTE: We are building index w.r.t l2 metric, suggested change to cosine similarity

query_vector = embeddings[:1]                   # use first embedding as query
x, indices = index.search(query_vector, k = 2)  # fetch 2 neighbors, first indices should be self

neighbor_embeddings = embeddings[indices]       # (1, 2, 768)
print(x, indices)

