from agent import Agent

if __name__ == "__main__":
    agent = Agent(name="Tinga")
    print("Tinga is ready. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = agent.run(user_input)
        print(f"Tinga: {reply}")
