import pandas as pd
from pytube import YouTube

df = pd.read_csv('/mnt/c/Users/bw800.PARTNERS/Desktop/urls.csv')
df = df[df.downloaded == False]

if len(df) > 0:
    for i in range(len(df)):
        this_url = df.urls.iloc[i]
        try:
            yt = YouTube(this_url)
            yt.streams.first().download('/home/brad/music')
            print('{} ({}) {}'.format('Success:', str(i), yt.title))
        except:
            print('{} ({}) {}'.format('Failed:', str(i), yt.title))

print('\n\nFinished!')
