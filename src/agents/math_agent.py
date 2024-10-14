from crewai import Agent
from tools.calculator_tool import CalculatorTool

class MathAgent():
    def __init__(self):
        self.model = 'ollama/llama3'

    def get_agent(self):
        return Agent(
            role = "Mathematician",
            goal = "Perform mathematical calculations",
            backstory = "You are a mathematician that takes in mathematical expressions in string format and returns the result as an integer using the calculator tool.",
            llm = self.model,
            tools=[CalculatorTool()],
            verbose = True
        )
