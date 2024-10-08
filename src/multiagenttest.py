import ollama
from aitest import AIAgent

class MultiAgent:
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent_name, agent):
        self.agents[agent_name] = agent

    def ask(self, question):
        prompt1 = "create a table for this question: " + question
        print("prompt1: ", prompt1)
        table_response = self.agents["table_agent"].ask(prompt1)
        print("table_response: ", table_response)

        prompt2 = "create a sql query for this question: " + question + " and use the table: " + table_response
        print("prompt2: ", prompt2)
        sql_response = self.agents["sql_agent"].ask(prompt2)
        print("sql_response: ", sql_response)

        return table_response, sql_response

sql_agent = AIAgent(model="llama3")
table_agent = AIAgent(model="llama3")
multiagent = MultiAgent()
multiagent.add_agent("sql_agent", sql_agent)
multiagent.add_agent("table_agent", table_agent)

question = input("Enter a question to create a table and a sql query: ")
table_response, sql_response = multiagent.ask(question)
print("Final Output:")
print("Table: ", table_response)
print("SQL: ", sql_response)


