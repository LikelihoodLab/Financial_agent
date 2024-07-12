from crewai import Agent
import os

from tools.browser_tool import BrowserTools
from tools.search_tools import SearchTools
import datetime

import dotenv

# define llm 

os.environ["OPENAI_API_BASE"] = 'https://api.openai.com/v1'
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'


date = datetime.datetime.now().strftime("%Y-%m-%d")

class StockAnalysisAgents():
  def financial_analyst(self):
    return Agent(
      role='The Best Financial Analyst',
      goal=f"""Go to websites such as Kitco, fxstreet, wsj, find the news articles that published {date}, and summarize it""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in financial market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
      ]
    )

  def research_analyst(self):
    return Agent(
      role='Staff Research Analyst',
      goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
      backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
      verbose=True,
      tools=[
              
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
 
      ]
  )

  def investment_advisor(self):
    return Agent(
      role='Private Investment Advisor',
      goal="""Impress your customers with full analyses over the market
      and completer investment recommendations""",
      backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,

      ]
    )