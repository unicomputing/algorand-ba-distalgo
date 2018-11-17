import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import random

# scale = 3.
# range = 10
# size = 100000
#
# X = truncnorm(a=-range/scale, b=range/scale, scale=scale).rvs(size=size)
# X = X.round().astype(int)
#
# bins = 2 * range + 1
# plt.hist(X, bins)
#
# plt.show()

num_procs = 50
num_role = 20
if num_procs <= 10:
    scale = 0.5
elif num_procs <= 50:
    scale = 1.0
else:
    scale = 1.5
A = np.histogram(np.random.normal(loc=num_procs/2, scale=1.*num_procs/10,
                                  size=num_role).round().astype(np.int32),
                 bins=num_procs)[0]
bins = range(0, num_procs)
plt.bar(bins, A)
plt.show()

chosen_users = [i for i in range(num_procs) if A[i]]

print('Chosen Users: {}'.format(chosen_users))
print('Number of chosen users: {}'.format(len(chosen_users)))