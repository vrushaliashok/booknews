from googlesearch import search
from newspaper import Article
from newspaper.article import ArticleException 
import streamlit as st
import nltk

nltk.download('punkt')
st.title("Book News")

def article_content(url):
    article = Article(url)
    
    try:
        article.download()
        article.parse()
        article.nlp()
        st.write(article.summary)
    except ArticleException as e:
        print("Error while processing article:", e)

def search_and_extract(query):
    search_results = search(query)
    for i, result in enumerate(search_results, start=1):
        if result in visited_links:
            continue
        visited_links.add(result)
        st.subheader(result)
        article_content(result)

if __name__ == "__main__":
    visited_links = {"https://www.booktrust.org.uk/news-and-features/", "https://bookmachine.org/2020/12/07/how-to-promote-a-childrens-book-a-primer/"}
    search_queries = ['licensing agreements regarding childrens books','top news in childrens books','how to market childrens books effectively']
    for search_query in search_queries:
        search_and_extract(search_query)
