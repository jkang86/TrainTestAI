# Joseph Kang
# jkang86@uic.edu
# I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s Academic Integrity standards. Signed: Joseph Kang

"""This is a model to test the possible scenario of what an AI can take to see it's success and fail rate based on using dictionaries and functions to recall previous trainings. By randomly picking a key, which is represented as a Probability, we can get the stored value and change that value based on scenarios."""

import random

def train(t_num, t_quality):
    p_values = {}
    x_values = {}  # This dictionary is storing the values of x for each probability 
    prev_trial_success = {}  # Dictionary to store a success for the previous result in the probability 

    # Given each probability it's own value being 50% and then setting x_values to 1 to increase the x for each individual probability
    for nums in range(1, 21):
        key = f"P{nums}"
        value = 50
        p_values[key] = {'probability': value}
        x_values[key] = 1
        prev_trial_success[key] = False # Set as false for it to change or stay the same in trials 

    for trials in range(t_num):
        key = random.choice(list(p_values.keys()))  # Randomly select one question
        percentage = p_values[key]['probability']
        random_float = random.random() 

        # To store the previous success and previous x for the question we are randomly choosing 
        prev_success = prev_trial_success[key]
        prev_x = x_values[key]

        if t_quality > random_float:
            if prev_success:
                x = prev_x * 2  # Double the value of x
            else:
                x = 1  # Reset x back to 1
            newProb = percentage + x
            prev_trial_success[key] = True # Change to True to later come back to x if we need to double the value
        else:
            if prev_success:
                x = 1  # Reset x back to 1
            else:
                x = prev_x * 2  # Double the value of x
            newProb = percentage - x
            prev_trial_success[key] = False

        # Ensure the probability stays within 0 - 100 
        newProb = max(0, min(100, newProb))

        # Update the selected probability, x, and success status in the dictionaries
        p_values[key]['probability'] = newProb
        x_values[key] = x

        # Print the resulting probabilities in the dictionary after each trial
    resulting_probs = [p_values[f'P{i}']['probability'] for i in range(1, 21)] # This is just to test if the resulting probabilities are returned properly  
    return resulting_probs

def test(prob_list): 
    num_correct = 0 

    for probs in prob_list:
        random_float = random.random() # Get a random float to test if it's less than or equal to the float in the list 

        if random_float <= (probs/100):
            num_correct += 1 # increment the num_correct to later put in the numerator for correctness/number of trials 

    if num_correct >= 15:
        return 1 
    else:
        return 0  

final_probabilities = train(100, 0.9) 
result = test(final_probabilities)

if result == 1:
    print("AI passed the test.")
else:
    print("AI did not pass the test.") # To test if the AI will pass based on different scenarios (can comment out if needed)

def pass_rate(t_num, t_quality):
    num_trials = 1000
    num_passed = 0 

    for _ in range(num_trials): # _ is set to say that there's no reason for it to be used in the loop, could be set as any variable 
        final_probabilities = train(t_num, t_quality)
        result = test(final_probabilities) # Recall the function to get the result to see if it has passed

        if result == 1:
            num_passed += 1 

    pass_percent = (num_passed / num_trials) * 100 # To print the result in a percentage 
    print(f"The pass rate for this AI is {pass_percent:.1f}%")
pass_rate(500, 0.6) # To test the printing feature 



