# anomaly_detection.py

from sklearn.ensemble import IsolationForest

def anomaly_detection_model(contamination=0.05):
    """
    Initializes and returns an IsolationForest model for anomaly detection.
    
    Returns:
    - model (IsolationForest): The IsolationForest model initialized with default parameters.
    """
    model = IsolationForest(contamination=contamination, random_state=42)
    return model

def detect_anomalies(model, data):
    """
    Detects anomalies in a given chunk of the data stream using the IsolationForest model.
    
    Args:
    - model (IsolationForest): The pre-trained IsolationForest model.
    - data (numpy array): The chunk of data to be analyzed for anomalies.
    
    Returns:
    - anomalies (numpy array): Array indicating normal (-1 for anomaly, 1 for normal) for each data point.
    
    Raises:
    - ValueError: If the input data contains NaN, infinite, or empty values.
    """
    
    import numpy as np

    # Step 1: Check if the input data is empty
    if data.size == 0:
        raise ValueError("Input data is empty.")
    
    # Step 2: Check for NaN or infinite values in the data
    if np.isnan(data).any():
        raise ValueError("Input data contains NaN (missing) values.")
    
    if np.isinf(data).any():
        raise ValueError("Input data contains infinite values.")
    
    # Step 3: Check that data is numeric and has the correct shape (1D array)
    if data.ndim != 1:
        raise ValueError("Input data must be a 1D array.")
    
    # Step 4: Detect anomalies using IsolationForest
    anomalies = model.fit_predict(data.reshape(-1, 1))
    
    return anomalies
