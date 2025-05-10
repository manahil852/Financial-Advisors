from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools

def get_company_symbol(company: str) -> str:
    """
    Use this function to get the symbol for a company
    Args:
        company (str): The name of the company
    Returns:
        str: The symbol for the company
    """
    symbols={
        "AIwithHassan": "AAPL",
        "Tesla": "TSLA",
        "Google": "GOOGL"
    }
    return symbols.get(company, "Unknown")



test_agent=Agent(
    model= Groq(
        id='deepseek-r1-distill-qwen-32b'
    ),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
    ), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=['Always take the symbols from the get_company_symbol tool and only use that symbol for further analysis, if the symbol doesnot exist, abort',
                  'Always create tables of camparison']
)
test_agent.print_response('Summarize and compare the analyst recommendations for the stocks of AIwithhassan and tesla?')
