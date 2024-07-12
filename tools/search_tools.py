import json
import os

import requests
from langchain.tools import tool


class SearchTools():
  @tool("Search the internet")
  def search_internet(query):
    """Useful to search the internet 
    about a a given topic and return relevant results"""
    top_result_to_return = 10
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': "68dbe144a0c49318de8b21298c1a775c39de3eb5",
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    return '\n'.join(string)

  @tool("Search news on the internet")
  def search_news(query):
    """Useful to search news about a company, stock or any other
    topic and return relevant results"""""
    top_result_to_return = 4
    url = "https://google.serper.dev/news"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': "68dbe144a0c49318de8b21298c1a775c39de3eb5",
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['news']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    return '\n'.join(string)


if __name__ == "__main__":
  query = "Most recent news article about gold on KITCO"
  tool = SearchTools()
  print(tool.search_news.invoke(query))