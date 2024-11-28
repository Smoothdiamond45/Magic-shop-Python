import random
import sys

print("Welcome to my magic shop, I am your host, the mighty Magic Bean")

while True:
    experience_choice = input("Well well well, Shall we begin? "
                              "Type 'y' to start  ")
    gold_coins = 109.99
    if experience_choice.lower() == 'y':
        print("Here are my items for sale, do choose wisely or you might wind up like the others")
        print("1. Magic Beans (20 gold coins per bean)")
        print("2. Magic carpet (50 gold coins)")
        print("3. Immortality spell (90 gold coins)")
        print("4. Magic broomstick (110 gold coins)")

        while True:
            print(f"\nYou have {gold_coins:.2f} gold coins with you currently")
            choice = input("Would you like to purchase something? (or simply enter 'exit' to leave):  ")

            if choice.lower() == 'exit':
                print("You should count yourself lucky, leaving with everything attached.....")
                sys.exit()


            elif choice.lower() == 'yes':
                item_choice = int(input("Enter the number of the item you want to purchase (1-4): "))

                if 1 <= item_choice <= 4:
                    item_prices = [20, 50, 90, 110]
                    item_quantity = int(input(f"How many of item {item_choice} would you like to purchase? "))

                    if item_choice == 1:
                        total_cost = item_prices[0] * item_quantity
                    elif item_choice == 2:
                        total_cost = item_prices[1] * item_quantity
                    elif item_choice == 3:
                        total_cost = item_prices[2] * item_quantity
                    elif item_choice == 4:
                        total_cost = item_prices[3] * item_quantity
                    else:
                        print("Invalid item choice.")

                    if total_cost <= gold_coins:
                        gold_coins -= total_cost
                        print(f"You have purchased {item_quantity} of item {item_choice} for {total_cost} gold coins.")
                    else:
                        print("Sorry, you don't have enough gold coins for that purchase.")

                    if 100 <= total_cost <= 105:
                        print("Well well well, I suppose I should reward you for the amount you have purchased.")
                        random_num = random.randint(1, 4)
                        if random_num == 1:
                            print("Congratulations! You have added an extra magic bean to your basket.")
                        elif random_num == 2:
                            print("Hmmm, very well. You may take one of my magic carpets.")
                        elif random_num == 3:
                            print("You better not use this incorrectly, trust me, I'll know.")
                        elif random_num == 4:
                            print("Damn, I hate this dumb rule. Here you go and enjoy it.")

                    elif 70 <= total_cost <= 95:
                        print("Congratulations, you have spent enough to win a magic spell")
                        if 70 <= total_cost <= 75:
                            print("This Magic spell will grant you with pain immunity for 4 moon cycles")
                        elif 80 <= total_cost <= 95:
                            print("This Magic spell shall grant you great strength in a time of need")


                else:
                    print("Invalid item choice. Please enter a number between 1 and 4.")
            else:
                print("Invalid choice. Please enter 'exit' or 'yes'.")
    else:
        print("Invalid choice. Please enter 'y' to begin.")