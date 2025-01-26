# Monty Hall Simulation

This project simulates the Monty Hall problem with a generalized number of doors. It runs multiple simulations to compare the probabilities of winning by keeping the initial choice versus switching to another door.

## Project Structure


- `montyhall.py`: Contains the main logic for running the Monty Hall simulations and plotting the results.

## Requirements

- Python 3.x
- `matplotlib`
- `numpy`

You can install the required packages using pip:

```sh
pip install matplotlib numpy

## Running the Simulation

To run the simulation, execute the 

montyhall.py

 script:

```sh
python montyhall.py
```

This will run the simulation for a range of door numbers and print the results to the console. It will also display a plot comparing the probabilities of the two strategies.


## Functions

get_initialized_doors(num_doors)

: Initializes the doors with one prize and the rest as goats.
- 

get_chosen_door_num(num_doors)

: Randomly selects a door.
- 

show_a_non_prize_door(doors, chosen_door_num)

: Shows a door that does not have the prize.
- 

get_another_door_num(doors, chosen_door_num)

: Selects another door that is not shown.
- 

run_game(num_doors)

: Runs the simulation for a given number of doors.
- 

print_strategy_result(result, strategy_name)

: Prints the result of a strategy.
- 

print_results(results)

: Prints the results of all simulations.
- 

get_door_nums(results)

: Gets the number of doors from the results.
- 

get_values(results, strategy_name, data_name)

: Gets the values for a strategy from the results.
- 

plot_results(results)

: Plots the results of the simulations.
- 

main()

: Main function to run the simulations and plot the results.
