print("Welcome to the Elite 101 Chatbot!")
name = input("What is your name? ")
print("Hi " + name + "! Nice to meet you.")
age = int(input("How old are you? "))
print("Wow, you are " + str(age) + " years old! What a great age to be!")
bool = True
while(bool is True):
  print("Please choose from the following options:")
  print("1. Placeholder Option 1")
  print("2. Placeholder Option 2")
  print("3. Placeholder Option 3")
  print("4. Exit the conversation")
  choice = int(input("Enter the number of your choice: "))
  if choice == 4:
    print("Goodbye, " + name + "!")
    bool = False