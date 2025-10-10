import pandas as pd
import re
import wordcloud
from wordcloud import WordCloud
from collections import Counter
#import emoji
def fetch_stats(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    num_messages=df.shape[0]
    words = []
    for message in df["message"]:
        words.extend(message.split())
    num_words=len(words)
    shared_media=df[df["message"]=="<Media omitted>\n"].shape[0]
    links=[]
    for i in df["message"]:
        if "https" in i:
            links.append(i)
    link_shared=len(links)
    return num_messages,num_words,shared_media,link_shared
def most_busy_user(df):
    x=df["user"].value_counts().head()
    df= round((df["user"].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={"count": "Percent"})
    return x,df
def create_wordcloud(selected_user,df):
    f = open("hinglish.txt", "r")
    stop_words = f.read()
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
    temp = df[df["user"] != "group_notification"]
    temp = df[df["message"] != "<Media omitted>\n"]
    def remove_stop_words(message):
        y=[]
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color="white")
    temp["message"]=temp["message"].apply(remove_stop_words)
    df_wc=wc.generate(temp["message"].str.cat(sep=" "))
    return df_wc
def most_common_words(selected_user,df):
    f=open("hinglish.txt","r")
    stop_words=f.read()
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    temp=df[df["user"]!="group_notification"]
    temp=df[df["message"]!="<Media omitted>\n"]
    words=[]
    for message in temp["message"]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_df
def emoji_helper(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
        "\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U0001F1E0-\U0001F1FF"  # Regional Indicator Symbols
        "\U0001F191-\U0001F251"  # Enclosed CJK Letters and Months
        "\U0001F004"  # Mahjong Tile Red Dragon
        "\U0001F0CF"  # Playing Card Black Joker
        "\U00002600-\U000026FF"  # Miscellaneous Symbols
        "\U0001F6E0-\U0001F6FF"  # Transport and Map Symbols Extended
        "\U00002B50-\U00002B55"  # Stars
        "]+", flags=re.UNICODE
    )
    # Initialize an empty list to store emojis
    emoji_list = []

    # Iterate over each message in d1["message"]
    for message in df["message"]:
        # Find all emojis in the message using regex
        emojis_found = emoji_pattern.findall(message)
        emoji_list.extend(emojis_found)

    # Create a DataFrame with counts of each emoji
    emoji_df = pd.DataFrame(Counter(emoji_list).most_common(len(Counter(emoji_list))), columns=["emoji", "count"])
    return emoji_df
def monthly_timeline(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    timeline=df.groupby(["year","month_num","month"]).count()["message"].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i]+"-"+str(timeline["year"][i]))
    timeline["time"]=time
    return  timeline
def daily_timeline(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    daily=df.groupby("only_date").count()["message"].reset_index()
    return daily
def week_activity_map(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    return df["day_name"].value_counts()
def month_activity_map(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    return df["month"].value_counts()
def activity_heat_map(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    activity_map=df.pivot_table(index="day_name",columns="period",values="message",aggfunc="count").fillna(0)
    return activity_map


