# data_stream.py

import numpy as np

def generate_data_stream(size=1000, noise_factor=0.2):
    """
    Generates a simulated data stream that includes regular patterns (sinusoidal), 
    seasonal variations, random noise, and concept drift.
    
    Args:
    - size (int): Number of data points to generate.
    - noise_factor (float): Factor to scale the random noise added to the stream.
    
    Returns:
    - data (numpy array): Generated data stream.
    
    Raises:
    - ValueError: If size is non-positive or noise_factor is negative.
    """
    
    # Step 1: Validate the size of the stream
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    
    # Step 2: Validate the noise factor
    if noise_factor < 0:
        raise ValueError("Noise factor must be a non-negative value.")
    
    # Step 3: Generate sinusoidal pattern with noise and concept drift
    time_series = np.sin(np.linspace(0, 20, size))
    noise = noise_factor * np.random.randn(size)
    concept_drift = np.hstack([np.ones(size // 2), np.ones(size // 2) * 3])
    
    # Step 4: Combine components to form the final data stream
    data = time_series + noise + concept_drift
    
    return data
