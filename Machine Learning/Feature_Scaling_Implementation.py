import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    mean = np.mean(data, axis = 0)
    std = np.std(data, axis = 0)
    standardized_data = (data - mean)/std
    
    min_data = np.min(data, axis=0)
    max_data = np.max(data, axis=0)
    normalized_data = (data - min_data)/(max_data - min_data)
    return np.round(standardized_data,4).tolist(),np.round(normalized_data,4).tolist()
