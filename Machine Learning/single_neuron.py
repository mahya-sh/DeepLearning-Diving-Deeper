import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    for feature_vector in features:
        z = sum(weight * feature for weight, feature in zip(weights, feature_vector)) + bias
        prob = 1 / (1 + math.exp(-z))  # Corrected parentheses
        probabilities.append(round(prob, 4))
    
    
    mse = round(sum((prob - label) ** 2 for prob, label in zip(probabilities, labels)) / len(labels), 4)
    return probabilities, mse
