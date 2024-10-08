import ollama


class AIAgent:
    def __init__(self, model="llama3"):
        self.model = model

    def ask(self, question):
        response = ollama.chat(model=self.model, messages=[
                {
                    "role": "user",
                    "content": question
                }
        ])
        return response["message"]["content"]


if __name__ == "__main__":
    # Create an instance of the AI agent
    agent = AIAgent()

    # Example usage
    question = "What are the benefits of AI in healthcare?"
    answer = agent.ask(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}")

