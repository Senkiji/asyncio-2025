import asyncio
from datetime import datetime
import time

speed = 100 # speed of the game in seconds per move
Judit_time = 5/speed # Judit time move
Opponent_time = 55/speed # Opponent time move
Opponent = 24 # Number Opponent
move_pair = 30 # Number of moves pair

async def game(x):
    board_start_time = time.perf_counter()
    calulate_board_start_time = 0
    for i in range(move_pair):
        await asyncio.sleep(Judit_time)
        calulate_board_start_time += Judit_time
        print(f'Board-{x+1} {i+1} Judit made a move with {int(Judit_time*speed)} seconds.')

        await asyncio.sleep(Opponent_time)
        calulate_board_start_time += Opponent_time
        print(f'Board-{x+1} {i+1} Opponent made a move with {int(Opponent_time*speed)} seconds.\n')

    print(f'Board-{x+1} >>>>>>> finished move in {(time.perf_counter() - board_start_time)*speed:.2f} seconds.')
    print(f'Board-{x+1} >>>>>>> finished move in {calulate_board_start_time*speed:.2f} seconds (calculated).')
    return {
        'board_time': (time.perf_counter() - board_start_time) * speed,
        'calculated_board_time': calulate_board_start_time * speed
    }

async def main():
    print(f"Number of game: {Opponent} games")
    print(f"Number of moves pair: {move_pair}")
    start_time = time.perf_counter()

    board_time = 0
    calutated_board_time = 0
    tasks = [asyncio.create_task(game(i)) for i in range(Opponent)]
    results = await asyncio.gather(*tasks)
    for result in results:
        board_time += result['board_time']
        calutated_board_time += result['calculated_board_time']

    print(f"Board exhibition finished in {board_time:.2f} seconds.")

asyncio.run(main())  # run top-level function concurrently