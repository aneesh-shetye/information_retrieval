#from retro_pytorch.retrieval import chunks_to_index_embed
import os 
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

from retro_pytorch.retrieval import get_tokenizer, get_bert
import torch 
import faiss


if __name__ == '__main__': 

    index = faiss.read_index('index.dat')
    print(index.ntotal) 

    '''
    with open('train.doc_ids.dat', 'r') as f: 
        doc_ids = [line.strip() for line in f.readlines()]
    '''

    tokenizer = get_tokenizer()
    model = get_bert()

    query = input('Query:') 

    encoding = tokenizer.batch_encode_plus(
        [query],
        add_special_tokens = True,
        padding = True,
        return_tensors = 'pt'
    )

    token_ids = encoding.input_ids

    if torch.cuda.is_available(): 
        token_ids = token_ids.cuda()

    outputs = model(
        input_ids = token_ids,
        output_hidden_states = True
    )

    hidden_state = outputs.hidden_states[-1]

    query_vector = hidden_state[:, 0].detach() #cls representation of the query embedding

    x, indices = index.search(query_vector, k= 100) 

    print('x and indices are: ') 
    print(x, indices) 


    
