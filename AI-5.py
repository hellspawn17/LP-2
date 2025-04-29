# Simple Customer Support Chatbot in Python

def chatbot():
    print("Welcome to ShopSmart Support!")
    print("Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I assist you today?")
        
        elif "order" in user_input:
            print("Bot: You can check your order status in 'My Orders' section.")
        
        elif "refund" in user_input or "return" in user_input:
            print("Bot: To request a refund or return, go to your recent orders and select 'Request Return'.")
        
        elif "delivery" in user_input or "shipping" in user_input:
            print("Bot: Most deliveries are made within 3-5 business days. You can track your order online.")
        
        elif "account" in user_input:
            print("Bot: You can manage your account settings from the Profile section.")
        
        elif user_input == "exit":
            print("Bot: Thank you for contacting ShopSmart. Have a great day!")
            break
        
        else:
            print("Bot: I'm sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
chatbot()
