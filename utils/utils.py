'''
basic utilities. Include: 
- preprocess_text: preprocesses text retrieved from a source. 
- get_text: retrieves text from a url.
'''

import requests
from bs4 import BeautifulSoup as bs
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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

def fetch_content2(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headless Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    content = driver.page_source
    driver.quit()
    return content

def fetch_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # This will raise an HTTPError for bad responses
    return response

def get_text(url: str):

  try:
    response = fetch_content(url)
    # response.raise_for_status() #raise exception for HTTP errors
    if response.status_code != 200: 
      print("Failed to retrieve text")
      return None 

    soup = bs(response.text, 'html.parser')
    #text = soup.get_text()
    if soup is None:
      print("Failed to parse text")
      return None

    paragraphs = soup.find_all('p')
    text = "\n\n".join([para.get_text()for para in paragraphs]) 

    text = preprocess_text(text)
    return text

  except requests.exceptions.RequestException as e:
    print(f'An error occured: {e}')
    response = fetch_content2(url)
    # soup = bs(response.text, 'html.parser')
    
    if response is not None: 
      # paragraphs = soup.find_all('p')
      # text = "\n\n".join([para.get_text() for para in paragraphs])
      return preprocess_text(response)

    return None
