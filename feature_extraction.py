import pandas as pd

def load_keystroke_log(filename="keystroke_data.csv"):
    df = pd.read_csv(filename)
    return df

def extract_features(df):
    df = df.sort_values(by='timestamp').reset_index(drop=True)
    df['flight_time'] = df['timestamp'].diff().fillna(0)
    df['dwell_time'] = 0.1
    return df

def build_baseline_profile(features_df):
    mean_flight = features_df['flight_time'].mean()
    std_flight = features_df['flight_time'].std()
    return {'mean_flight_time': mean_flight, 'std_flight_time': std_flight}

if __name__ == "__main__":
    df = load_keystroke_log()
    features = extract_features(df)
    profile = build_baseline_profile(features)
    print("Baseline profile:", profile)
    features.to_csv("features.csv", index=False)
