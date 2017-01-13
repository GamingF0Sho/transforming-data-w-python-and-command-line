import read
from dateutil.parser import parse
import datetime

df = read.load_data()

def extract_hour(row):
    to = parse(row['submission_time']).strftime("%H")
    return to

Submission_Hours = df.apply(extract_hour, axis=1)
sub_hour_counts = Submission_Hours.value_counts()      
    
if __name__ == "__main__":
    print(sub_hour_counts)