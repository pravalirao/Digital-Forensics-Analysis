import pandas as pd

# Sample data for testing
data = {
    'Event ID': [1001, 1015, 1022, 1033],
    'Timestamp': ['2023-01-01 08:00:00', '2023-01-01 08:05:00', '2023-01-01 08:10:00', '2023-01-01 08:15:00'],
    'Event Type': ['Information', 'Warning', 'Error', 'Error'],
    'Source': ['System', 'Application', 'Security', 'System'],
    'Event Description': ['The system has started up.', 'The application failed to start.', 'An authentication error occurred.', 'The system encountered a critical error and needs to restart.']
}

# Create a DataFrame
df = pd.DataFrame(data)
