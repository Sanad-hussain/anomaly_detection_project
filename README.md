# Efficient Data Stream Anomaly Detection

This project is part of the application process for the Graduate Software Engineer role at Cobblestone Energy. It demonstrates a real-time anomaly detection system applied to a continuous data stream, simulating real-world scenarios like financial transactions or system metrics.

## Project Features:
- **Algorithm Selection**: Uses the `IsolationForest` algorithm to detect anomalies in real-time. The algorithm is robust to concept drift and seasonal variations, making it suitable for detecting unusual patterns in streaming data.
- **Data Stream Simulation**: The data stream includes sinusoidal patterns to simulate seasonality, random noise, and concept drift to represent changing conditions over time.
- **Real-Time Anomaly Detection**: The system processes data in chunks and flags anomalies as they are detected.
- **Real-Time Visualization**: Detected anomalies are displayed in real-time using Streamlit, with red dots highlighting anomalous points.

## Project Structure:
- `data_stream.py`: Generates the simulated data stream with seasonality, noise, and concept drift.
- `anomaly_detection.py`: Contains the anomaly detection logic using `IsolationForest`.
- `visualization.py`: Handles real-time visualization of the data stream and anomalies using `matplotlib` and Streamlit.
- `main.py`: Main script that integrates all components to simulate, detect, and visualize anomalies in real-time.

## Algorithm Explanation:
The **IsolationForest** algorithm was chosen due to its efficiency in detecting anomalies in high-dimensional data. It works by isolating points that are far away from the majority of the data. The algorithm is particularly well-suited for streaming data as it can adapt to evolving patterns.

## Requirements
- Python 3.x
- Streamlit
- Scikit-learn
- NumPy
- Matplotlib

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd anomaly_detection_project
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project
1. Run the Streamlit application:
    ```sh
    streamlit run main.py
    ```

2. The application will open in your default web browser, showing the real-time data stream and detected anomalies.

## Files
- `main.py`: Main script to run the anomaly detection pipeline.
- `anomaly_detection.py`: Contains the anomaly detection model and function.
- `data_stream.py`: Simulates the continuous data stream.
- `visualization.py`: Handles the real-time visualization of the data and anomalies.
- `requirements.txt`: Lists the required Python libraries.

## Error Handling
- Handles missing or malformed data with appropriate error messages and skips processing invalid data chunks.

## Contact
For any questions or further information, please contact Sanad Hussain at sanadhussain25@gmail.com.

---

**Note**:URL of the repository <> where the company can clone the project.
# anomaly_detection_project
