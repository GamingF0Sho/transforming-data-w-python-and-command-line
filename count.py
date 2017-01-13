import read
import re
from collections import Counter

df = read.load_data()

headline_col = df['headline']

string = ""
for row in headline_col:
    string += str(row) + " "
string = string.lower()
string_list = string.split(" ")

cnt = Counter()
for word in string_list:
    cnt[word] += 1

top_100 = Counter(string_list).most_common(100)

if __name__ == "__main__":
    print(top_100)