import sys
from crewai import Crew

from agents.math_agent import MathAgent
from tasks.math_task import MathCalculationTask

input_expression = ''
if sys.stdin.isatty():
    # Running in interactive mode
    while True:
        try:
            input_expression = input("Enter a mathematical expression (or 'exit' to quit): ")
            if input_expression.lower() == 'exit':
                sys.exit(0)  # Exit the program if 'exit' is entered
            break  # Break the loop after getting a valid expression
        except EOFError:
            sys.exit(0)  # Exit the program if EOF is encountered
else:
    # Running in non-interactive mode (e.g., in CI/CD pipeline)
    print("Running in non-interactive mode. Please provide an expression as a command-line argument.")
    if len(sys.argv) > 1:
        input_expression = sys.argv[1]  # Take the first command-line argument as the expression
    else:
        print("Error: No expression provided.")
        sys.exit(1)  # Exit with an error code if no expression is provided


agent = MathAgent().get_agent()
task = MathCalculationTask().calculate(input_expression, agent)

crew = Crew(
    agents = [agent],
    tasks = [task]
)

result = crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)