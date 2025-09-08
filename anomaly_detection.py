import pandas as pd

def detect_anomalies(features_df, profile, threshold=3):
    anomalies = []
    mean = profile['mean_flight_time']
    std = profile['std_flight_time']

    for idx, row in features_df.iterrows():
        if abs(row['flight_time'] - mean) > threshold * std:
            anomalies.append({'timestamp': row['timestamp'], 'flight_time': row['flight_time']})
    return anomalies

if __name__ == "__main__":
    features_df = pd.read_csv("features.csv")
    profile = {'mean_flight_time': features_df['flight_time'].mean(), 'std_flight_time': features_df['flight_time'].std()}
    anomalies = detect_anomalies(features_df, profile)
    if anomalies:
        print(f"Alert! Detected {len(anomalies)} anomalies:")
        for a in anomalies:
            print(a)
    else:
        print("No anomalies detected.")
