players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

total_players = []
for i_key, i_value in players.items():
    i_player = i_key + i_value
    total_players.append(i_player)
print(total_players)

