import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
llm = Ollama(model="ollama/llama2", base_url="http://localhost:11434/v1")
print("########################")
print(llm)
print("########################")

agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
    """,
    llm='ollama/llama2'
)

task = Task(
    description="Tell me all about the box jellyfish.",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

print("\n\n########################")
print("## Here is the result")
print("########################\n")
print(result)