def chatbot(msg):
    msg = msg.lower()
    if "hello" in msg:
        return "Hi!"
    elif "how are you" in msg:
        return "I'm fine"
    elif "bye" in msg:
        return "Goodbye!"
    else:
        return "I don't understand"

while True:
    m = input("You: ")
    if m == "exit":
        break
    print("Bot:", chatbot(m))
