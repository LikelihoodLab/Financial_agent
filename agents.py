from crewai import Agent
import os

from tools.browser_tool import BrowserTools
from tools.search_tools import SearchTools
import datetime

import dotenv

# define llm

# os.environ["OPENAI_API_KEY"]='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'
# os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o-mini'

date = datetime.datetime.now().strftime("%Y-%m-%d")


class StockAnalysisAgents():

  def financial_analyst(self):
    return Agent(
        role='The Best Financial Analyst',
        goal=
        f"""Go to websites such as Kitco, fxstreet, wsj, find the news articles that published {date}, and summarize it""",
        backstory="""The most seasoned financial analyst with 
      lots of expertise in financial market analysis and investment
      strategies that is working for a super important customer.""",
        verbose=True,
        tools=[
            BrowserTools.scrape_and_summarize_website,
            SearchTools.search_internet,
            SearchTools.search_news,
        ])

  def research_analyst(self):
    return Agent(
        role='Staff Research Analyst',
        goal=
        """Gather, interpret, and synthesize data from various sources to discover actionable insights.""",
        backstory=
        """Recognized as the best in the field, you excel at sifting through news, company announcements, and market sentiments to provide detailed analyses for critical clients.""",
        verbose=True,
        tools=[
            BrowserTools.scrape_and_summarize_website,
            SearchTools.search_internet,
            SearchTools.search_news,
        ])

  def investment_advisor(self):
    return Agent(
        role='Strategic Investment Advisor',
        goal=
        """"Analyze market data and research findings to develop comprehensive investment recommendations for high-profile clients.""",
        backstory=
        """An experienced investment advisor known for combining diverse analytical insights to craft strategic investment advice, now working to impress a very important client.""",
        verbose=True,
        tools=[
            BrowserTools.scrape_and_summarize_website,
            SearchTools.search_internet,
            SearchTools.search_news,
        ])
