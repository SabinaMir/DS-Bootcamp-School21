# Configuration for the program
num_of_steps = 3  # Number of predictions for predict_random

# Report template
report_template = """
Report

We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tail_fraction}% and {head_fraction}%, respectively.
Our forecast is that in the next {steps} observations we will have: {forecast_tails} tail and {forecast_heads} heads.
"""
