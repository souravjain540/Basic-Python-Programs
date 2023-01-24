from numpy import asarray
from numpy.random import rand

# objective function
def objective(x):
	return x**2.0

def derivative(x):
	return x * 2.0

def gradient_descent(objective, derivative, bounds, n_iter, step_size):
	solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	for i in range(n_iter):
		# calculate gradient
		gradient = derivative(solution)
		# take a step
		solution = solution - step_size * gradient
		# evaluate candidate point
		solution_eval = objective(solution)
		# report progress
		print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
	return [solution, solution_eval]

# Driver Code:

bounds = asarray([[-1.0, 1.0]])
n_iter = 30
step_size = 0.1
best, score = gradient_descent(objective, derivative, bounds, n_iter, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))
