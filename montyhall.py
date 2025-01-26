import matplotlib.pyplot as plt
import numpy as np
import random
from my_vis import test_plot

TOTAL_GUESSES = 10000

MAX_NUM_DOORS = 10

PRIZE = 2
GOAT = 1
SHOWN = 0

NUMBER_OF_DOORS = "number of doors"
KEEP_DOOR_STRATEGY = "keep door strategy"
CHANGE_DOOR_STRATEGY = "change door strategy"
COUNT = "count"
PERCENT = "percent"
PROBABILITY = "probability"


def get_initialized_doors(num_doors):
    doors = [GOAT for i in range(num_doors)] 
    doors[random.randint(0, num_doors - 1)] = PRIZE
    return doors


def get_chosen_door_num(num_doors):
    return random.randint(0, num_doors - 1)


def show_a_non_prize_door(doors, chosen_door_num):
    showable_door_nums = [i for i, door in enumerate(doors) 
    if door != PRIZE and i != chosen_door_num]
    doors[random.choice(showable_door_nums)] = SHOWN


def get_another_door_num(doors, chosen_door_num):
    #strategy 2
    other_doors_nums = [i for i, door in enumerate(doors)
    if i != chosen_door_num and door != SHOWN]
    return random.choice(other_doors_nums)


def run_game(num_doors):
    change_doors = 0
    keep_doors = 0
    
    for i in range(TOTAL_GUESSES):
        doors = get_initialized_doors(num_doors)
        chosen_door_num = get_chosen_door_num(num_doors)
        show_a_non_prize_door(doors, chosen_door_num)
        other_door_num = get_another_door_num(doors, chosen_door_num)
        
        if doors[chosen_door_num] == PRIZE:
            keep_doors += 1
        elif doors[other_door_num] == PRIZE:
            change_doors += 1
    
    change_door_percent = round((change_doors/TOTAL_GUESSES)*100.0, 2)
    keep_door_percent = round((keep_doors/TOTAL_GUESSES)*100.0, 2)
    
    return {
        NUMBER_OF_DOORS: num_doors,
        KEEP_DOOR_STRATEGY: {
            COUNT: keep_doors,
            PERCENT: keep_door_percent,
            PROBABILITY: round(1.0/num_doors * 100.0, 2)
        },
        CHANGE_DOOR_STRATEGY: {
            COUNT: change_doors,
            PERCENT: change_door_percent,
            PROBABILITY: round((num_doors - 1.0)/(num_doors * (num_doors - 2.0)) * 100.0, 2)
        }
    }


def print_strategy_result(result, strategy_name):
    d = result[strategy_name]
    print(f'{strategy_name}: percent = {d[PERCENT]}, count = {d[COUNT]}, probability = {d[PROBABILITY]}')


def print_results(results):
    print(f"number of simulation runs is {TOTAL_GUESSES}")
    print()
    for result in results:
        print(f"number of doors: {result[NUMBER_OF_DOORS]}")
        print_strategy_result(result, KEEP_DOOR_STRATEGY)
        print_strategy_result(result, CHANGE_DOOR_STRATEGY)
        print()


def get_door_nums(results):
    return [result[NUMBER_OF_DOORS] for result in results]


def get_values(results, strategy_name, data_name):
    return [result[strategy_name][data_name] for result in results]


def plot_results(results):
    x = get_door_nums(results)
    y11 = get_values(results, KEEP_DOOR_STRATEGY, PERCENT)
    y12 = get_values(results, KEEP_DOOR_STRATEGY, PROBABILITY)
    y21 = get_values(results, CHANGE_DOOR_STRATEGY, PERCENT)
    y22 = get_values(results, CHANGE_DOOR_STRATEGY, PROBABILITY)

    #plt.style.use("_mpl-gallery")

    fig, ax = plt.subplots()
    ax.plot(x, y11, "x", markeredgewidth=2, label="keep door strategy percent")
    ax.plot(x, y12, linewidth=2.0, label="keep door strategy probability")
    ax.plot(x, y21, "o", markeredgewidth=2, label="change door strategy percent")
    ax.plot(x, y22, linewidth=2.0, label="change door strategy probability")

    ax.set(xlim=(x[0] - 1, x[-1] + 1), xticks=x,
           ylim=(0, 100), yticks=range(25, 100, 25))

    plt.title("Generalized Monty Hall Results")
    plt.xlabel("number of doors")
    plt.ylabel("probability/percent")

    plt.legend()
    plt.show()


def main():
    results = []
    for num_doors in range(3, MAX_NUM_DOORS + 1):
        results.append(run_game(num_doors))
    print_results(results)
    plot_results(results)


if __name__ == "__main__":
    main()
    
    
    