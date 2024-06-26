from gliner import GLiNER as gl 


import argparse
parser = argparse.ArgumentParser(description='get queries accoding to the titles')

parser.add_argument('--textfile', type=str, default='queries.txt', help='file to save queries in')


if __name__ == "__main__": 
    
    model = gl.from_pretrained("urchade/gliner_multi")
    
    list_of_interesting_words = ['company', 'commodity', 'strategy', 'branch', 'country', 'state', 'location', 'authority']

    