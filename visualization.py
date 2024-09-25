# visualization.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def real_time_visualization(data, anomalies):
    """
    Visualizes the data stream and highlights detected anomalies in real-time.

    Args:
    - data (numpy array): The data stream to be plotted.
    - anomalies (numpy array): Array indicating anomalies (-1) and normal data (1).
    
    Visualization:
    - A line chart of the data stream.
    - Red dots mark points where anomalies were detected.
    """
    # Create a new figure and axis for plotting.
    fig, ax = plt.subplots()

    # Plot the data stream as a line chart.
    ax.plot(data, label="Data Stream")
    
    # Highlight anomalies as large red dots.
    anomaly_points = [data[i] if anomalies[i] == -1 else np.nan for i in range(len(anomalies))]
    ax.plot(anomaly_points, 'ro', markersize=8, label="Anomalies")

    # Add labels and legend for clarity.
    ax.legend()
    ax.set_title("Real-Time Data Stream and Anomalies")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

    # Render the figure in Streamlit.
    st.pyplot(fig)
