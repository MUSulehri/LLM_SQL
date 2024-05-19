from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = ''

# connect to test database
db = SQLDatabase.from_uri(
    database_uri="mssql+pyodbc://SSI-MSULEHRI-FL/LLM_SALES?driver=ODBC+Driver+17+for+SQL+Server"
)

toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

agent_executor = create_sql_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4"),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run("can you show the sales of first two months?")
