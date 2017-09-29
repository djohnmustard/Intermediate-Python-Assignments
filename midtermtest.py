import random

number_of_decks = 4

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]



def cards_define_function():
    cards = deck * number_of_decks
    return cards

cards = cards_define_function()

def remove_card(string):
    return cards.remove(string)

def dealer_cards():
    dealer_card_one = random.choice(cards)
    remove_card(dealer_card_one)
    dealer_card_two = random.choice(cards)
    remove_card(dealer_card_two)
    dealer_total = dealer_card_one + dealer_card_two
    return dealer_card_one, dealer_card_two, dealer_total

def user_cards():
    user_card_one = random.choice(cards)
    remove_card(user_card_one)
    user_card_two = random.choice(cards)
    remove_card(user_card_two)
    user_total = user_card_one + user_card_two
    return user_card_one, user_card_two, user_total


def one_more_card():
    extra_card = random.choice(cards)
    remove_card(extra_card)
    return extra_card


def dealer_new_random_card():
    dealer_new_card = random.choice(cards)
    remove_card(dealer_new_card)
    return dealer_new_card

dealer_cards = list(dealer_cards())
user_cards = list(user_cards())


dealer_stands_on = 17


def dealer_show():
    print("Dealer has {}".format(dealer_cards))

def user_show():
    print("You have {}:".format(user_cards))

def bust():
    print("BUST!!!")

def ask_again():
     new_answer = input("Dealer stands on {}. Do you want another card? ".format(dealer_stands_on))
     return new_answer



def ask_user_initial():
    answer = input("Your 1st card is {}, The Dealers 1st card is {}, type 'yes' to Continue! "
        .format(user_cards[0], dealer_cards[0]))
    if answer != '':
        user_show()
    while user_cards[len(user_cards)-1] <= 21:
        new_answer = ask_again()
        if new_answer == 'yes' or new_answer == 'YES':
            extra_card = one_more_card()
            user_cards[len(user_cards)-1] += extra_card
            print("Your new card is a : {}!".format(extra_card))
            print("The new total is : {}".format(user_cards[len(user_cards)-1]))
            user_cards.insert(len(user_cards)-1, extra_card)
        else:
            while dealer_cards[len(dealer_cards)-1] < dealer_stands_on:
                dealer_new_card = dealer_new_random_card()
                print("Dealer has drawn : {}".format(dealer_new_card))
                dealer_cards[len(dealer_cards)-1] += dealer_new_card
                dealer_cards.insert(len(dealer_cards)-1, dealer_new_card)

            else:
                if dealer_cards[len(dealer_cards)-1] <= 21:
                    if dealer_cards[len(dealer_cards)-1] < user_cards[len(user_cards)-1]:
                        print("Your total is {}".format(user_cards[len(user_cards)-1]))
                        user_show()
                        print("Dealer has : {}".format(dealer_cards))
                        print("CONGRATS!!! You Won!")
                        break
                    elif dealer_cards[len(dealer_cards)-1] > user_cards[len(user_cards)-1]:
                        print("Your total : {}".format(user_cards[len(user_cards)-1]))
                        user_show()
                        print("Dealer has : {}".format(dealer_cards))
                        print("Oh NO!!! You should have went for another card, Dealer wins again!!")
                        break
                    else:
                        print("Your total is : {}".format(user_cards[len(user_cards)-1]))
                        print("Dealer has : {}".format(dealer_cards))
                        print("This is a PUSH, it was a nice hand both of you played great!")
                        break
                else:
                    print("Your total is : {}".format(user_cards[len(user_cards)-1]))
                    user_show()
                    print("Dealer has : {}".format(dealer_cards))
                    print("CONGRATS!!! You Won!")
                    break

    else:
        bust()
        user_show()
        while dealer_cards[len(dealer_cards)-1] < dealer_stands_on:
            dealer_new_card = dealer_new_random_card()
            print("Dealer has drawn : {}".format(dealer_new_card))
            dealer_cards[len(dealer_cards)-1] += dealer_new_card
            dealer_cards.insert(len(dealer_cards)-1, dealer_new_card)
        dealer_show()

ask_user_initial()
quit()
