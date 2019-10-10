from pandas import read_csv
from sklearn.model_selection import TimeSeriesSplit
from matplotlib import pyplot

# Use on a series and split it into a training and test set
def train_test_split_series( series, training_ratio):
	X = series.values
	train_size = int( len( X) * training_ratio)
	train, test = X[ 0: train_size], X[ train_size: len(X)]
	print('Observations: %d' % (len(X)))
	print('Training Observations: %d' % (len(train)))
	print('Testing Observations: %d' % (len(test)))
	return train, test

def train_test_split_multiple_series( series, splitsCount):
	X = series.values
	splits = TimeSeriesSplit( n_splits = splitsCount)
	index = 1
	for train_index, test_index in splits.split( X):
		train = X[ train_index]
		test = X[ test_index]
		print('Observations: %d' % (len(train) + len(test)))
		print('Training Observations: %d' % (len(train)))
		print('Testing Observations: %d' % (len(test)))
		pyplot.subplot(310 + index)
		pyplot.plot(train)
		pyplot.plot([None for i in train] + [x for x in test])
		index += 1
	pyplot.show()