from Classes import Game, Round, Card, Player

# enter the number of players
num_of_players = int(input("How many players? "))
# initiate the game
game1 = Game(num_of_players)
# create deck of cards
game1.create_deck_of_cards()
# instantiate players
game1.create_players()

rounds_played = [] # For saving rounds which have been played

while game1.num_of_rounds < 2:
    game1.num_of_rounds += 1
    current_round = Round()

    # Choose the player who will start the round
    if game1.num_of_rounds == 1:
        current_round.first_player = current_round.choose_first_player(game1)
    else:
        pass # Otherwise starts the player who lost the last round

    current_round.deal_cards(game1) # parameters of a specific game - deck and num of players
    print(f"{game1.players[1].name} has these cards: {game1.players[0].cards_in_hand} .")

    print(f"{game1.num_of_rounds}. round is finished")

    rounds_played.append(current_round) # Saving played rounds into a list


print(rounds_played)