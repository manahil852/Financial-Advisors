from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

financial_agent=Agent(
    model= Groq(id='deepseek-r1-distill-qwen-32b'),
    #model= Groq(id='llama-3.3-70b-versatile'),
    name='financial Analyst',
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
    )],
    show_tool_calls=True,
    markdown=True,
    instructions=['Always create tables of camparison'],
)


web_researcher=Agent(
    model= Groq(id='deepseek-r1-distill-qwen-32b'),
    #model= Groq(id='llama-3.3-70b-versatile'),
    name= 'web Researcher',
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=['Always include sources of information that you gather'],
)

agents_team=Agent(
    team=[financial_agent, web_researcher],
    model= Groq(id='deepseek-r1-distill-qwen-32b'),
    #model= Groq(id='llama-3.3-70b-versatile'),
    show_tool_calls=True,
    markdown=True,
    instructions=['Always include sources of information gathered', 'Always create tables for comparisons'],
    debug_code=True
    
)


agents_team.print_response('Summarize the analyst recommendations and share the latest information about google for Nvdia?')
