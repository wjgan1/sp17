import numpy as np
"""
In the below function you will be implementing a function
to calculate the gini impurity for a given collection of labels
below are some examples to test how your function behaves
"""
def gini_index(classes):
	counts = {}
	for x in classes:
		if x not in counts:
			counts[x] = 1
		else:
			counts[x] += 1
	sum = 0
	for c in counts.values():
		f = c/len(classes)
		sum += f*f
	return 1-sum

"""
Uncomment these tests to see how
your function behaves

"""
print(gini_index([0, 0, 0, 0,0, 0]))
print(gini_index([0, 1, 0, 1, 0, 1]))
