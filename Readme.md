# Monty Hall Simulation

This project simulates the Monty Hall problem with a generalized number of doors. It runs multiple simulations to compare the probabilities of winning by keeping the initial choice versus switching to another door.

## Project Structure

- `montyhall.py`: Contains the main logic for running the Monty Hall simulations and plotting the results.

## Requirements

- Python 3.x
- `matplotlib`

You can install the required packages using pip:

```sh
pip install matplotlib
```

## Usage

To run the simulation and save the results to a JSON file, execute the montyhall.py script with a filename argument:

```sh
python montyhall.py results.json
```

This will run the simulation for a range of door numbers, print the results to the console, save the results to the specified JSON file, and display a plot comparing the probabilities of the two strategies.
