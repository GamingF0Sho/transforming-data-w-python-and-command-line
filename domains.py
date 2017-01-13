import read
df = read.load_data()

domain_count = df['url'].value_counts()

if __name__ == "__main__":
    print(domain_counts)