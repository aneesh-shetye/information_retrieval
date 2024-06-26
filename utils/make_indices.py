#creating chunks and indices of text documents 
import os 
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import time
import argparse
from retro_pytorch.retrieval import text_folder_to_chunks_, chunks_to_index_and_embed
import faiss 

parser = argparse.ArgumentParser(description='chunk documents and make faiss index')

#filenames
parser.add_argument('--textFolder', type=str, default='text_docs', help='folder with text documents')
parser.add_argument('--chunksFolder', type=str, default='train.chunks.dat', help='folder with text documents')
parser.add_argument('--seqFolder', type=str, default='train.seq.dat', help='folder with text documents')
parser.add_argument('--docIdsFolder', type=str, default='train.doc_ids.dat', help='folder with text documents')
parser.add_argument('--indexFolder', type=str, default='index.dat', help='folder with text documents')

#hyperparameters: 
parser.add_argument('--chunkSize', type=int, default=128, help='size of chunks')
parser.add_argument('--seqLen', type=int, default=4096, help='sentence length')
parser.add_argument('--maxChunks', type=int, default=1_000_000_000, help= 'max number of chunks') 
parser.add_argument('--maxSeqs', type=int, default=1_000_000, help='max number of sequences')

#indexparameters: 
parser.add_argument('--indexString', type=str, default=None, help='index string for FAISS index factory')

args = parser.parse_args()
#create chunks and chunk start indices

if __name__ == '__main__': 
    
    '''
    root = os.getcwd()
    text_folder = os.path.join(root, args.textFolder) 
    chunks_path = os.path.join(root, args.chunksFilename) 
    seq_path = os.path.join(root, args.seqFilename) 
    doc_id_path = os.path.join(root, args.docIdFilename) 
    faiss_index_path = os.path.join(root, args.indexFilename) 
    '''
    
    '''
    stats = text_folder_to_chunks_(
        folder = args.textFolder,
        glob = '**/*.txt',
        chunks_memmap_path = args.chunksFolder,
        seqs_memmap_path = args.seqFolder,
        doc_ids_memmap_path = args.docIdsFolder,  # document ids are needed for filtering out neighbors belonging to same document appropriately during computation of nearest neighbors
        chunk_size = args.chunkSize,
        seq_len = args.seqLen,
        max_chunks = args.maxChunks,
        max_seqs = args.maxSeqs
    )
    print(stats)
    '''

    #convert chunks into embeddings and faiss index 
    index, embeddings = chunks_to_index_and_embed(
        num_chunks = 1000,
        chunk_size = 64,
        chunk_memmap_path = args.chunksFolder, 
        index_string = args.indexString
    )

    faiss.write_index(index, args.indexFolder)

    #NOTE: We are building index w.r.t l2 metric, suggested change to cosine similarity

    print(f'FAISS index created at: {args.indexFolder}')
    print("###################################################")

    k = 5
    print(f'sanity check: query= Doc 1, k = {k}')
    query_vector = embeddings[:1]                   # use first embedding as query

    start_time = time.time()
    x, indices = index.search(query_vector, k = k)  # fetch k neighbors, first indices should be self
    end_time = time.time()

    print(f'TIME FOR SEARCHING {k}-NN: {end_time - start_time}')

    neighbor_embeddings = embeddings[indices]       # (1, 2, 768)
    print(x, indices)

