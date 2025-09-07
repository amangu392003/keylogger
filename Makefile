.PHONY: all clean keylogger feature_extract anomaly_detect visualize

all: keylogger feature_extract anomaly_detect visualize

keylogger:
	@echo "Starting keystroke logger... Press ESC to stop."
	python keylogger.py

feature_extract:
	@echo "Extracting features from keystroke data..."
	python feature_extraction.py

anomaly_detect:
	@echo "Detecting anomalies based on profile..."
	python anomaly_detection.py

visualize:
	@echo "Visualizing flight time data and alerts..."
	python visualization_alerting.py

clean:
	@echo "Removing generated data files..."
	rm -f keystroke_data.csv features.csv keystroke_data.log

