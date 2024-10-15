from crewai import LLM, Agent
from tools.calculator_tool import CalculatorTool

class MathAgent():
    def __init__(self):
        # For local testing remove the base_url, 
        # http://ollama:11434 is the url for the ollama container
        self.model = LLM(model='ollama/llama3', base_url='http://ollama:11434')

    def get_agent(self):
        return Agent(
            role = "Mathematician",
            goal = "Perform mathematical calculations",
            backstory = "You are a mathematician that takes in mathematical expressions in string format and returns the result as an integer using the calculator tool.",
            llm = self.model,
            tools=[CalculatorTool()],
            verbose = True
        )
