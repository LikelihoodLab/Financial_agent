from crewai import Task
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d")

class StockAnalysisTasks():
  def research(self, agent):
    return Task(description= f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to gold and
        its industry from website such as KITCO, FXstreet, investing.com on {date}.
        

      """, 
         expected_output = "string",
      agent=agent
    )


  def financial_analysis(self, agent):
    return Task(description= f"""
        Pay special attention to any significant events, market
        sentiments,and analysts' opinions. Also include upcoming central bank's monetary policies on interest rates changes, currency value changes and other relevant events that may impact the value of gold.
        Your final answer MUST be a report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the gold.
        Make sure to use the most recent data as possible.

        """, 
         expected_output = "string",
      agent=agent
    )

  def recommend(self, agent):
    return Task(description=f"""
        Review and synthesize the analyses provided by the
       the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation. 

        You MUST Consider all aspects, including market overview,          recent events summary, geopolotical impacts, central banks' policies and potential risks.

        Your final answer MUST be a recommendation for your
        customer. It should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formatted for your customer.
        {self.__tip_section()}
      """,
                expected_output = "string",
      agent=agent
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"