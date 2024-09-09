import numpy as np
def precision(y_true, y_pred):
	true_pos = np.sum((y_pred==1) & (y_true ==1)) 
	false_pos = np.sum((y_pred ==1) & (y_true ==0))
	return true_pos/(true_pos + false_pos) if (true_pos + false_pos)>0 else 0
