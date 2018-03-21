import read
import dateutil 

df = read.load_data()

def time(x):
    y=dateutil.parser.parse(x)    
    return y.hour
df['submission_hours']=df['submission_time'].apply(time)
print(df['submission_hours'].value_counts().head())