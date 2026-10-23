# Retail Store Chatbot
# Answers customer questions about store hours, location, products, and prices.

PRICES = {
    "laptop": 750,
    "headphone": 60,
    "charger": 20,
    "mouse": 25,
    "watch": 150,
}

def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"\nHello, {name}! I am the rain-retail chatbot. How may I help you today?\n")

def main():
    # Start chatbot
    user_name = get_user_name()
    greet_user(user_name)

    # Menu loop
    while True:
        print("Please choose from the following options:")
        print("1. Ask about store hours")
        print("2. Ask for store location")
        print("3. Ask about available products")
        print("4. Ask about prices")
        print("5. Exit the conversation")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("Our store hours are Monday-Saturday: 10 AM-9 PM\n")

        elif choice == "2":
            print("We are located at 123 Main Street TX.\n")

        elif choice == "3":
            print("We currently have laptops, headphones, chargers, mouses, and smartwatches.\n")

        elif choice == "4":
            text = input("Please type your question about prices: \n ").lower()
            found = False

            for item, price in PRICES.items():
                if item in text:
                    print(f"The {item} costs ${price}.\n")
                    found = True
                    break

            if not found:
                print("Please tell me which product you want the price for.\n")

        elif choice == "5":
            print("Goodbye! Thank you for chatting with rain-retail chatbot.")
            break

        else:
            print("Please choose 1, 2, 3, 4, or 5.\n")

if __name__ == "__main__":
    main()
