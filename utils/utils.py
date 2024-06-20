'''
basic utilities. Include: 
- preprocess_text: preprocesses text retrieved from a source. 
- get_text: retrieves text from a url.
'''

import requests
from bs4 import BeautifulSoup as bs
import re

def preprocess_text(text: str):
  '''
  basic preprocessing, just keep the large text blocks, i.e,
  with more than 3 sentences. (Text blocks are defined as continuous text with less than 2 \n)
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
    if response.status_code != 200: 
      print("Failed to retrieve text")
      return None 

    soup = bs(response.content, 'html.parser')
    #text = soup.get_text()
    if soup is None:
      print("Failed to parse text")
      return None

    paragraphs = soup.findall('p')
    text = "\n\n".join([para.get_text()for para in paragraphs]) 

    text = preprocess_text(text)
    return text

  except requests.exceptions.RequestException as e:
    print(f'An error occured: {e}')
    return None
