import random

def get_response(user_input):
  # Convert user input to lowercase for easier comparision
  user_input = user_input.lower()

  # Define responses based on user input
  if 'hello' in user_input or 'hi' in user_input:
    return random.choice(["Hello! How can I assist you today?", "Hi there! What can I do for you?"])
  elif 'how are you' in user_input:
    return random.choice(["I'm just a bot, but I'm here to help! What do you need?", "I'm doing well, thank you. How can I assist you?"])
  elif 'help' in user_input:
    return random.choice(["Sure, I can help. What do you need assistance with?", "What can I ssist you with today?"])
  elif 'thank you' in user_input or 'thanks' in user_input:
    return "You're welcome!"
  elif 'exit' in user_input:
    return "Goodbye! Have a great day!"
  else:
    return "I'm sorry, I didn't catch that. Can you please provide more information?"

def chat():
  print("Chatbot: Hello! How can I assist you today? Type 'exit' to end the conversation.")

  while True:
    user_input = input("User: ")

    # Get response from the chatbot
    response = get_response(user_input)

    # Print response
    print("Chatbot:", response)

    # Check if the user wants to exit
    if 'exit' in user_input.lower():
      break

# Start the chat
chat()
