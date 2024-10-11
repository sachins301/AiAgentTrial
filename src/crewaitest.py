import os
from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm = Ollama(model="llama2")

agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
    """,
    llm=llm
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
