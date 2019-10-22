from ivis import Ivis
from sklearn import datasets
import numpy as np


def test_iris_embedding():
	iris = datasets.load_iris()
	x = iris.data
	y = iris.target
	y = np.array(y)
	mask = np.random.choice(range(len(y)), size=len(y) // 2, replace=False)
	y[mask] = -1

	ivis_iris = Ivis(epochs=5)
	ivis_iris.k = 15
	ivis_iris.batch_size = 16

	y_pred_iris = ivis_iris.fit_transform(x, y)
