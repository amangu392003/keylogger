import matplotlib.pyplot as plt
import pandas as pd
import anomaly_detection as ad

def plot_flight_times(features_df, anomalies):
    plt.figure(figsize=(12,6))
    plt.plot(features_df['timestamp'], features_df['flight_time'], label='Flight Time')
    if anomalies:
        anomaly_times = [a['timestamp'] for a in anomalies]
        anomaly_values = [a['flight_time'] for a in anomalies]
        plt.scatter(anomaly_times, anomaly_values, color='red', label='Anomalies')
    plt.xlabel('Timestamp')
    plt.ylabel('Flight Time (seconds)')
    plt.title('Keystroke Flight Time with Anomalies')
    plt.legend()
    plt.grid(True)
    plt.show()

def alert(anomalies):
    if anomalies:
        print(f"Warning: {len(anomalies)} suspicious typing events detected!")
    else:
        print("No suspicious activity detected.")

if _name_ == "_main_":
    features_df = pd.read_csv("features.csv")
    profile = {'mean_flight_time': features_df['flight_time'].mean(), 'std_flight_time': features_df['flight_time'].std()}
    anomalies = ad.detect_anomalies(features_df, profile)
    alert(anomalies)
    plot_flight_times(features_df, anomalies)
