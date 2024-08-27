import math

def softmax(scores: list[float]) -> list[float]:
	exp_scores = [math.exp(score) for score in scores]
	sum_all = sum(exp_scores)
	probabilities = [round(score/sum_all ,4) for score in exp_scores]
	return probabilities
