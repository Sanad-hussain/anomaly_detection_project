# main.py

from anomaly_detection import anomaly_detection_model, detect_anomalies
from data_stream import generate_data_stream
from visualization import real_time_visualization

import time

def run_anomaly_detection():
    """
    Runs the complete anomaly detection pipeline:
    - Simulates a continuous data stream.
    - Detects anomalies in real-time.
    - Visualizes the results with a real-time graph.
    """
    try:
        # Step 1: Initialize the anomaly detection model
        model = anomaly_detection_model(contamination=0.05)

        # Step 2: Generate simulated data stream
        stream_data = generate_data_stream(size=1000, noise_factor=0.1)

        # Step 3: Process the data stream in chunks
        for i in range(0, len(stream_data), 25):
            chunk = stream_data[i:i+50]  # Get a chunk of data points
            
            # Step 4: Detect anomalies and handle any errors
            try:
                anomalies = detect_anomalies(model, chunk)
                real_time_visualization(chunk, anomalies)
            except ValueError as ve:
                # Log the error and skip processing this chunk
                print(f"Error in data chunk: {ve}")
                continue  # Skip to the next chunk
            
            # Simulate real-time data streaming
            time.sleep(1)

    except Exception as e:
        # Handle any unexpected errors in the main pipeline
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    run_anomaly_detection()
