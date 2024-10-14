from crewai import Crew

from agents.math_agent import MathAgent
from tasks.math_task import MathCalculationTask


input_expression = input("Enter a mathematical expression: ")

agent = MathAgent().get_agent()
task = MathCalculationTask().calculate(input_expression, agent)

crew = Crew(
    agents = [agent],
    tasks = [task]
)

result =crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)