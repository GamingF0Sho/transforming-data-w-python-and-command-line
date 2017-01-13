import pandas as pd
import sys

df = pd.read_csv("hn_stories.csv")
df.columns = ["submission_time", "upvotes", "url", "headline"]

def load_data():
    return df

if __name__ == "__main__":
    load_data()
    
      
        
        
        
        
