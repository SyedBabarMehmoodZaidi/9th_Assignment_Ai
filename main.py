from my_agent.hotel_assistant import HotelAssistant

def main():
    print("=== Multi-Hotel Assistant (Gemini) ===")
    print("Type 'exit' to quit.\n")

    agent = HotelAssistant()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = agent.get_hotel_info(user_input)
        print("Agent:", response)
        print()

if __name__ == "__main__":
    main()
