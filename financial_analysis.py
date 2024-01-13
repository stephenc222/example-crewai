from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()

# Install the required library for Yahoo Finance News Tool
# !pip install langchain_community

yahoo_finance_news_tool = YahooFinanceNewsTool()

# Define your agents with roles and goals
financial_analyst = Agent(
    role='Financial Analyst',
    goal='Analyze current financial news to identify market trends and investment opportunities',
    backstory="""You are an experienced financial analyst adept at interpreting market data and news
  to forecast financial trends and advise on investment strategies.""",
    verbose=True,
    allow_delegation=False,
    tools=[yahoo_finance_news_tool]
)

communications_specialist = Agent(
    role='Corporate Communications Specialist',
    goal='Communicate financial insights and market trends to company stakeholders',
    backstory="""As a communications specialist in a corporate setting, your expertise lies in
  crafting clear and concise messages from complex financial data for stakeholders and the public.""",
    verbose=True,
    allow_delegation=True,
    # (optional) llm=another_llm
)

# Create tasks for your agents
task1 = Task(
    description="""Review the latest financial news using the Yahoo Finance News Tool. Identify key market trends
  and potential investment opportunities relevant to our company's portfolio.""",
    agent=financial_analyst
)

task2 = Task(
    description="""Based on the financial analyst's report, prepare a press release for the company. The release should
  highlight the identified market trends and investment opportunities, tailored for our stakeholders and the general public.""",
    agent=communications_specialist
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[financial_analyst, communications_specialist],
    tasks=[task1, task2],
    verbose=2
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
