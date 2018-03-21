import pandas as pd


def load_data():
    s = pd.read_csv("hn_stories.csv")
    s.columns=['submission_time','upvotes','url','headline']
    return s

if __name__ == "__main__":
        # This will call load_data if you run the script from the command line.
    load_data()

