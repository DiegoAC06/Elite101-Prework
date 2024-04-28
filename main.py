def main():
  print("Welcome to ClothingBot! What is your name?")
  name = input().lower()
  print("Hello " + name + "! What can I help you with today?")
  while True:
      user_input = input("Do you want to process a return, exchange, or exit? ").lower()
      if "return" in user_input:
        Return()
        print("Thank you for using ClothingBot. Have a great day!")
        break
      elif "exchange" in user_input:
        Exchange()
        print("Thank you for using ClothingBot. Have a great day!")
        break
      elif "exit" in user_input or "quit" in user_input:
        print("Thank you for using ClothingBot. Have a great day!")
        break
      else:
        print("ClothingBot: I'm sorry, I didn't understand that. Please specify if you want to 'return', 'exchange', or type 'exit' to end the conversation.")

def Return():
  print("ClothingBot: Thank you for choosing ClothingBot for your return. Please provide the details of the item you want to return.")
  item = input("Item type: ")
  if item[len(item) - 1] == "s":
    tempStr = ""
    for i in range(len(item) - 1):
      tempStr += item[i]
    item = tempStr
  amount = int(input("Item amount: "))
  price = float(input("Item price for each: "))
  if amount > 1:
    suffix = "s"
  else:
    suffix = ""
  print(f"ClothingBot: Thank you for returning {amount} {item}{suffix} for ${price*amount} total.")
  print("ClothingBot: Your return request has been processed. A return label will be sent to your email shortly.")

def Exchange():
  print("ClothingBot: Great! Let's proceed with the exchange. Please provide details about the item you want to exchange.")
  item1 = input("Item type: ").lower()
  if item1[len(item1) - 1] == "s":
    tempStr = ""
    for i in range(len(item1) - 1):
      tempStr += item1[i]
    item1 = tempStr
  amount = int(input("Item amount: "))
  soloPrice = float(input("Item price for each: "))
  price1 = amount * soloPrice
  item2 = input("Item that you want: ").lower()
  if item2[len(item2) - 1] == "s":
    tempStr = ""
    for i in range(len(item2) - 1):
      tempStr += item2[i]
    item2 = tempStr
  price2 = float(input("Item price for each: "))
  if amount > 1:
    suffix1 = "s"
  else:
    suffix1 = ""
  if(soloPrice == price2):
    print(f"ClothingBot: Your exchange request has been processed. Your {amount} {item1}{suffix1} will be replaced with {amount} {item2}{suffix1}. The new item{suffix1} will be shipped to you shortly.")
  elif price2%price1 == 0:
    if price2/price1 > 1:
      suffix2 = "s"
    else:
      suffix2 = ""
    print(f"ClothingBot: Your exchange request has been processed. Your {amount} {item1}{suffix1} will be replaced with {int(price2/price1)} {item2}{suffix2}. The new item{suffix2} will be shipped to you shortly.")
  elif price1%price2 == 0:
    if price1/price2 > 1:
      suffix2 = "s"
    else:
      suffix2 = ""
    print(f"ClothingBot: Your exchange request has been processed. Your {amount} {item1}{suffix1} will be replaced with {int(price1/price2)} {item2}{suffix2}. The new item{suffix2} will be shipped to you shortly.")
  else:
    print("ClothingBot: These items do not have the same value or provide an equal trade for a different amount of items, therefore, we cannot process this exchange.")


if __name__ == "__main__":
  main()