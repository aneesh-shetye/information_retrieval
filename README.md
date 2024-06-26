## Code for benchmarking document ranking 

### STEP 1: Downloading text documents:
`python utils/make_text_docs.py --textfolder '/output/folder/name'`


### STEP 2: Generating the index:
`python utils/make_index.py --textFolder '/text/folder/name' --indexFolder '/output/folder/name' --indexString 'faiss_index_string'`

Reference to FAISS composite index and FAISS index factory- https://github.com/facebookresearch/faiss/wiki/The-index-factory 


