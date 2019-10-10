# Load sunspot data
from pandas import read_csv
from matplotlib import pyplot
from helperMethods import *
series = read_csv( 'monthly-sunspots.csv', header = 0, index_col = 0)
series.plot()

# Train-Test split
# Pro:  Large dataset, simple
train_sunspots, test_sunspots = train_test_split_series( series, .66)
pyplot.plot( train_sunspots)
pyplot.plot( [ None for i in train_sunspots] + [ x for x in test_sunspots])


# Multiple Train-Test Splits
# Pro: More robust than Train-Test split
# Cons: More computational effort

# Scikit-Learn, TimeSeriesSplit
# 	Input: 	Number of splits
#	Output:	Indexs of the train and test observation, for each split

train_test_split_multiple_series( series, 3)




pyplot.show()