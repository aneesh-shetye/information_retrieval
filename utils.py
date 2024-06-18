import requests
from bs4 import BeautifulSoup as bs
import re

def preprocess_text(text: str):
  '''
  basic preprocessing, just keep the large text blocks, i.e,
  with more than 3 sentences. (Text blocks are defined as continuous text with less than 2 \n)
  TO DO: Add DrQA based preprocessing as given in DPR paper.
  '''
  text_blocks = re.split(r'\n\n|\t{4,}', text)
  condition = lambda block: len(block.split('.')) > 3
  long_text_blocks = [block for block in text_blocks if condition(block)]

  result_text = '\n\n'.join(long_text_blocks)
  return result_text

def get_text(url: str):

  try:
    response = requests.get(url)
    response.raise_for_status() #raise exception for HTTP errors

    soup = bs(response.content, 'html.parser')
    text = soup.get_text()

    text = preprocess_text(text)
    return text
  except requests.exceptions.RequestException as e:
    print(f'An error occured: {e}')
    return None
