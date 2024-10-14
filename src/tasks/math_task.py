
from crewai import Agent, Task


class MathCalculationTask():
    def calculate(self, operation: str, agent: Agent):
        return Task(
            description = f"""Perform a mathematical calculation. 
                If the input is not a mathematical expression, convert the sentence into a mathematical expression 
                and then perform the calculation if possible else return statement saying it's not possible.
                
                Input: {operation}
                """,
            goal = "Perform a mathematical calculation",
            expected_output = "The result of the mathematical expression",
            agent = agent
        )
