import random
import os
# yorum satırı eklendi
class BlackjackGame:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        random.shuffle(self.deck)
        self.dealer_hand = []
        self.player_hand = []

    def deal_card(self):
        card = self.deck.pop()
        return {11: "J", 12: "Q", 13: "K", 14: "A"}.get(card, card)

    def deal_hand(self):
        return [self.deal_card(), self.deal_card()]

    def calculate_total(self, hand):
        total = 0
        ace_count = 0
        for card in hand:
            if card in ["J", "Q", "K"]:
                total += 10
            elif card == "A":
                ace_count += 1
                total += 11
            else:
                total += card
        while total > 21 and ace_count:
            total -= 10
            ace_count -= 1
        return total

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_results(self):
        self.clear_screen()
        print(f"Dealer's hand: {self.dealer_hand} (Total: {self.calculate_total(self.dealer_hand)})")
        print(f"Your hand: {self.player_hand} (Total: {self.calculate_total(self.player_hand)})")

    def check_blackjack(self):
        if self.calculate_total(self.player_hand) == 21:
            self.print_results()
            print("🎉 Blackjack! You win!\n")
            return True
        elif self.calculate_total(self.dealer_hand) == 21:
            self.print_results()
            print("😞 Dealer has Blackjack. You lose.\n")
            return True
        return False

    def evaluate_score(self):
        self.print_results()
        player_total = self.calculate_total(self.player_hand)
        dealer_total = self.calculate_total(self.dealer_hand)

        if player_total > 21:
            print("😵 You busted. Dealer wins.\n")
        elif dealer_total > 21:
            print("🎉 Dealer busted. You win!\n")
        elif player_total > dealer_total:
            print("🎉 You beat the dealer!\n")
        elif player_total < dealer_total:
            print("😞 Dealer wins.\n")
        else:
            print("🤝 It's a tie!\n")

    def play(self):
        self.clear_screen()
        print("🃏 WELCOME TO BLACKJACK 🃏\n")
        self.dealer_hand = self.deal_hand()
        self.player_hand = self.deal_hand()

        while True:
            print(f"Dealer shows: {self.dealer_hand[0]}")
            print(f"Your hand: {self.player_hand} (Total: {self.calculate_total(self.player_hand)})")

            if self.check_blackjack():
                break

            choice = input("Do you want to [H]it, [S]tand, or [Q]uit? ").lower()
            if choice == "h":
                self.player_hand.append(self.deal_card())
                if self.calculate_total(self.player_hand) > 21:
                    break
            elif choice == "s":
                while self.calculate_total(self.dealer_hand) < 17:
                    self.dealer_hand.append(self.deal_card())
                break
            elif choice == "q":
                print("👋 Thanks for playing!")
                exit()

        self.evaluate_score()
        self.play_again()

    def play_again(self):
        again = input("Play again? (Y/N): ").lower()
        if again == "y":
            self.__init__()
            self.play()
        else:
            print("👋 Goodbye!")
            exit()

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
   # yorum satırı eklendi