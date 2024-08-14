from crewai import Task
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d")


class StockAnalysisTasks():

  def research(self, agent):
    return Task(description=f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to gold and
        its industry from website such as KITCO, FXstreet, investing.com on {date}.
        

      """,
                expected_output="string",
                agent=agent)

  def financial_analysis(self, agent):
    return Task(description=f"""
        Pay special attention to any significant events, market
        sentiments,and analysts' opinions. Also include upcoming central bank's monetary policies on interest rates changes, currency value changes and other relevant events that may impact the value of gold.
        Your final answer MUST be a report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the gold.
        Make sure to use the most recent data as possible.

        """,
                expected_output="string",
                agent=agent)

  def recommend(self, agent):
    return Task(description=f"""
        Review and synthesize the analyses provided by the
        Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation. 
  
        You MUST Consider all aspects, including market overview,recent events summary, geopolotical impacts, 
        central banks' policies and potential risks.
        generate a numerical index that reflects the current performance of gold in the market. The index should take into account key factors such as the recent price trends of gold (over the past month), comparisons with other precious metals (like silver and platinum), global economic indicators (such as inflation rates and currency strength), and recent geopolitical events. Present the index as a number between 0 and 100, where 0 indicates very poor performance and 100 indicates extremely strong performance.Each of the factors should be weighted differently, and the index should be calculated based on the relative importance of each rated factors. Show the calculation steps.
        The gold index result should consist of following parameters: 
            Current Gold Price, Central Bank Policy Impact, Geopolitical Influence, Demand Trends, Price Forecast
            and the gold index result.
        Your final answer MUST be a comprehensive report of this date {date} for your
        customer and a gold index from the input of index task. The recommendation should be a full super detailed report, providing a 
        clear investment stance and strategy with clear supporting evidence.
        Make it pretty and well formatted for your customer. 
      """,
                expected_output="string",
                agent=agent,
                output_file=f'./res/{date}.md')
