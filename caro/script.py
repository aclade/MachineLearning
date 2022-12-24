from tic_tac_toe import *

my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]

select_space(my_board, 5, "X")
select_space(my_board, 4, "X")
select_space(my_board, 6, "X")
available_moves(my_board)
print_board(my_board)
has_won(my_board,"X")
#print_board(my_board)

