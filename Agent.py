from langchain.chat_models import ChatOpenAI
from langchain import hub
from tools import sqlexetool, sqlgentool
from langchain.agents import AgentExecutor
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import OpenAI

from langchain.prompts import PromptTemplate
# llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key="api_key")

from langchain_openai import AzureOpenAI

llm = AzureOpenAI(model="model_name",api_key="api_key",api_version="api-preview-version",azure_endpoint = "https://endpoint.openai.azure.com/")


# Get the prompt to use - we can modify this!
# prompt = hub.pull("hwchase17/react")

prompt = """
Answer the question as best as you can using the following tool: 

[


]

{tools}

Use the following format:

Question: the input question you must answer
Thought: comment on what you want to do next
Action: the action to take, exactly one element of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation repeats N times, use it until you are sure of the answer)
Thought: I now know the final answer
Final Answer: your final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}
"""
prompt = PromptTemplate(
    input_variables=['tool_description', 'tool_names'],
    template=prompt,
    
)
print(prompt)
tools = [sqlexetool, sqlgentool]

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print(agent_executor.invoke({"input": "provide me value of sum the total items buy from the store"}))
