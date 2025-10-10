import streamlit as st
import preprocess,helper
import matplotlib.pyplot as plt
import seaborn as sns
from helper import most_common_words, activity_heat_map

st.sidebar.title("Chat Analyzer")
uploaded_file=st.sidebar.file_uploader("choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocess.preprocessor(data)
    #st.dataframe(df)
    user_list=df["user"].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Show Analysis",user_list)
    if st.sidebar.button("Show Analysis"):
        num_messages,num_words,shared_media,link_shared=helper.fetch_stats(selected_user,df)
        st.header("Top Statistics")
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header("Total Messages")
            st.subheader(num_messages)
        with col2:
            st.header("Total Words")
            st.subheader(num_words)
        with col3:
            st.header("Media Shared")
            st.subheader(shared_media)
        with col4:
            st.header("Links Shared")
            st.subheader(link_shared)

        st.header("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig,ax=plt.subplots()
        plt.xticks(rotation="vertical")
        ax.plot(timeline["time"],timeline["message"],color="green")
        st.pyplot(fig)

        st.header("Daily Timeline")
        d_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        plt.xticks(rotation="vertical")
        ax.plot(d_timeline["only_date"], d_timeline["message"], color="black")
        st.pyplot(fig)

        st.header("Activity Map")
        col1,col2=st.columns(2)
        with col1:
            week_map=helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(week_map.index,week_map.values)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            month_map=helper.month_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(month_map.index,month_map.values)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        st.header("Weekly Activity Map")
        activity_map=helper.activity_heat_map(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(activity_map)
        st.pyplot(fig)

        if selected_user=="Overall":
            st.header("Most Busy Users")
            x,new_df=helper.most_busy_user(df)
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index,x.values,color="red")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)
            with col2:
                st.header("WordCloud")
                df_wc=helper.create_wordcloud(selected_user, df)
                fig,ax=plt.subplots()
                ax.imshow(df_wc)
                st.pyplot(fig)
        most_common_df=helper.most_common_words(selected_user, df)
        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation="vertical")
        st.header("Most Common Words")
        st.pyplot(fig)
        emoji_df=helper.emoji_helper(selected_user,df)
        st.header("Emoji Analysis")
        col1,col2=st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax=plt.subplots()
            ax.pie(emoji_df["count"],labels=emoji_df["emoji"],autopct="%0.2f")
            st.pyplot(fig)








