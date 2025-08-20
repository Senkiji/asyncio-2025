import asyncio
import random
import matplotlib.pyplot as plt

# Number of agents
N_AGENTS = 10
# Maximum number of steps
N_STEPS = 1000

# Random target position
TARGET_POSITION = (random.randint(-20, 20), random.randint(-20, 20))

# Dictionary to store the path (trace) of each agent
traces = {i: [(0,0)] for i in range(N_AGENTS)}
# Dictionary to record which agent found the target which step
found_by = {}

# Flag to indicate if the target has been found
target_found = False

async def explore(agent_id:int):

    global target_found
    x,y= traces[agent_id][0]
    for step in range(1, N_STEPS + 1):

        if target_found:
            break

        # Random movement
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x,y = x + dx, y + dy
        # Update the agent's trace
        traces[agent_id].append((x, y))

        # Check if the agent found the target
        if (x, y) == TARGET_POSITION:
            found_by[agent_id] = step
            target_found = True
            print(f"Agent {agent_id} found the target at step {step}")
            break

        await asyncio.sleep(0.01)

async def main():
    print(f'Random target location: {TARGET_POSITION}')
    # Launch all agents as asynchronous tasks
    tasks = [asyncio.create_task(explore(i)) for i in range(N_AGENTS)]
    await asyncio.gather(*tasks)

    # Plot which agent found the target
    for agent_id, path in traces.items():
        xs, ys = zip(*path)
        plt.plot(xs,ys, marker=".", alpha = 0.6 , label=f'Agent {agent_id}')

    plt.scatter(*TARGET_POSITION, color='red', label='Target', s=100 , marker='X')

    plt.title('Swarm Exploration')
    plt.legend()
    plt.grid()
    plt.show()

    if found_by:
        print(f"Target found by:")
        for agent, step in found_by.items():
            print(f"Agent {agent} at step {step}")
        else:
            print("No agent found the target.")

if __name__ == "__main__":
    # Run the main function
    print("Starting swarm exploration...")
    asyncio.run(main())

