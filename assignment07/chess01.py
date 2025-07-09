import time
from datetime import datetime

speed = 100 # speed of the game in seconds per move
Judit_time = 5/speed # Judit time move
Opponent_time = 55/speed # Opponent time move
Opponent = 24 # Number Opponent
move_pair = 30 # Number of moves pair

# def game(): # Co pilot
#     start_time = datetime.now()
#     print(f'Start time: {start_time.strftime("%H:%M:%S")}')
    
#     for i in range(move_pair):
#         print(f'Move {i+1}: Judit vs Opponent')
#         time.sleep(Judit_time)
#         print(f'Judit made a move in {Judit_time} seconds.')
        
#         time.sleep(Opponent_time)
#         print(f'Opponent made a move in {Opponent_time} seconds.')
    
#     end_time = datetime.now()
#     print(f'End time: {end_time.strftime("%H:%M:%S")}')
#     total_time = (end_time - start_time).total_seconds()
#     print(f'Total game time: {total_time} seconds')


# def oneGame(x):
#     start_time = datetime.now()
#     print(f'Start time: {start_time.strftime("%H:%M:%S")}')
#     move = x
#     print(f'Number of moves: {move}')
#     for i in range(move):
#         time.sleep(Judit_time)
#         print(f'Judit Move {i+1}: made a move in {Judit_time} seconds.')
        
#         time.sleep(Opponent_time)
#         print(f'Opponent Move {i+1}: made a move in {Opponent_time} seconds.\n')
#     print(f'{time.perf_counter()/60} min elapsed for {move} moves.')

#     print(f'End time: {datetime.now().strftime("%H:%M:%S")}')

def game(x):
    board_start_time = time.perf_counter()
    calulate_board_start_time = 0
    for i in range(move_pair):
        time.sleep(Judit_time)
        calulate_board_start_time = calulate_board_start_time + Judit_time
        print(f'Board-{x+1} {i+1} Judit made a move with {int(Judit_time*speed)} seconds.')

        time.sleep(Opponent_time)
        calulate_board_start_time = calulate_board_start_time + Opponent_time
        print(f'Board-{x+1} {i+1} Opponent made a move with {int(Opponent_time*speed)} seconds.\n')

    print(f'Board-{x+1} >>>>>>> finished move in {(time.perf_counter() - board_start_time)*speed:.2f} seconds.')
    print(f'Board-{x+1} >>>>>>> finished move in {calulate_board_start_time*speed:.2f} seconds (calulated).')
    return{
        'board_time' : (time.perf_counter() - board_start_time)*speed,
        'calulated_board_time' : calulate_board_start_time*speed
    }


if __name__ == "__main__":
    print(f"I hate my life")
    
    print(f"Number of game: {Opponent} games")
    print(f"Number of moves pair: {move_pair}")
    start_time = time.perf_counter()

    board_time = 0
    calutated_board_time = 0
    for board in range(Opponent):
        result = game(board)
        board_time += result['board_time']
        calutated_board_time += result['calulated_board_time']

    print(f"Board exhibition finished in {board_time:.2f} seconds.")
    print(f"finished in {round(time.perf_counter() - start_time)} seconds.")