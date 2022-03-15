
import streamlit as st
from janome.tokenizer import Tokenizer
import numpy as np
import pandas as pd
import tweepy
from twitter import *
from wordcloud import WordCloud
import json
import matplotlib.pyplot as plt
import nlplot
import requests
import time
import datetime
import itertools
from bs4 import BeautifulSoup




def page1():
    st.title('分析')
    """ 
    # 1.データの取得

    """

    NGWORD1 = ''
    NGWORD2 = ''
    NGWORD3 = ''
    NGWORD4 = ''
    NGWORD5 = ''
    NGWORD6 = ''
    NGWORD7 = ''
    NGWORD8 = ''
    NGWORD9 = ''
    NGWORD10 = ''
    NGWORD11 = ''
    NGWORD12 = ''
    NGWORD13 = ''
    NGWORD14 = ''
    NGWORD15 = ''
    NGWORD16 = ''
    NGWORD17 = ''
    NGWORD18 = ''
    NGWORD19 = ''
    NGWORD20 = ''
    STOPWORD1 = ''
    STOPWORD2 = ''
    STOPWORD3 = ''
    STOPWORD4 = ''
    STOPWORD5 = ''
    STOPWORD6 = ''
    STOPWORD7 = ''
    STOPWORD8 = ''
    STOPWORD9 = ''
    STOPWORD10 = ''
    STOPWORD11 = ''
    STOPWORD12 = ''
    STOPWORD13 = ''
    STOPWORD14 = ''
    STOPWORD15 = ''
    STOPWORD16 = ''
    STOPWORD17 = ''
    STOPWORD18 = ''
    STOPWORD19 = ''
    STOPWORD20 = ''

    CONSUMER_KEY = 'KTD6yq9nBXs9mbDciDentNEt4'
    CONSUMER_SECRET = 'hTe4lqtjYbBPKHbeBmgDiYPcZsfNhms1CO0iDgNIvMBTqvjecY'
    ACCESS_TOKEN = '1500824873882456069-46anQERuNYnwH6NuYzSnkUdmuPab7L'
    ACCESS_TOKEN_SECRET = 'i4BG5yqenpKZbeT9PLuwrhaoOThnWeXGRcvMeUqj6L4NE'

    auth = OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    twitter = Twitter(auth = auth)
    word = st.text_input('検索する言葉を入力してください','')
    NG_COUNT = st.slider('投稿内容からNG言葉の数を選択してください',0,20,0)
    if NG_COUNT == 0:
        st.write('NG言葉はありません')

    elif NG_COUNT == 1:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
    elif NG_COUNT == 2:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
    elif NG_COUNT == 3:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
    elif NG_COUNT == 4:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
    elif NG_COUNT == 5:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
    elif NG_COUNT == 6:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
    elif NG_COUNT == 7:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
    elif NG_COUNT == 8:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
    elif NG_COUNT == 9:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
    elif NG_COUNT == 10:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
    elif NG_COUNT == 11:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
    elif NG_COUNT == 12:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
    elif NG_COUNT == 13:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
    elif NG_COUNT == 13:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
    elif NG_COUNT == 14:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
        NGWORD14 = st.text_input('14つ目のNG言葉を入れてください','')
    elif NG_COUNT == 15:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
        NGWORD14 = st.text_input('14つ目のNG言葉を入れてください','')
        NGWORD15 = st.text_input('15つ目のNG言葉を入れてください','')
    elif NG_COUNT == 16:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
        NGWORD14 = st.text_input('14つ目のNG言葉を入れてください','')
        NGWORD15 = st.text_input('15つ目のNG言葉を入れてください','')
        NGWORD16 = st.text_input('16つ目のNG言葉を入れてください','')
    elif NG_COUNT == 17:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
        NGWORD14 = st.text_input('14つ目のNG言葉を入れてください','')
        NGWORD15 = st.text_input('15つ目のNG言葉を入れてください','')
        NGWORD16 = st.text_input('16つ目のNG言葉を入れてください','')
        NGWORD17 = st.text_input('17つ目のNG言葉を入れてください','')
    elif NG_COUNT == 18:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
        NGWORD14 = st.text_input('14つ目のNG言葉を入れてください','')
        NGWORD15 = st.text_input('15つ目のNG言葉を入れてください','')
        NGWORD16 = st.text_input('16つ目のNG言葉を入れてください','')
        NGWORD17 = st.text_input('17つ目のNG言葉を入れてください','')
        NGWORD18 = st.text_input('18つ目のNG言葉を入れてください','')
    elif NG_COUNT == 19:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
        NGWORD14 = st.text_input('14つ目のNG言葉を入れてください','')
        NGWORD15 = st.text_input('15つ目のNG言葉を入れてください','')
        NGWORD16 = st.text_input('16つ目のNG言葉を入れてください','')
        NGWORD17 = st.text_input('17つ目のNG言葉を入れてください','')
        NGWORD18 = st.text_input('18つ目のNG言葉を入れてください','')
        NGWORD19 = st.text_input('19つ目のNG言葉を入れてください','')
    elif NG_COUNT == 20:
        NGWORD1 = st.text_input('1つ目のNG言葉を入れてください','')
        NGWORD2 = st.text_input('2つ目のNG言葉を入れてください','')
        NGWORD3 = st.text_input('3つ目のNG言葉を入れてください','')
        NGWORD4 = st.text_input('4つ目のNG言葉を入れてください','')
        NGWORD5 = st.text_input('5つ目のNG言葉を入れてください','')
        NGWORD6 = st.text_input('6つ目のNG言葉を入れてください','')
        NGWORD7 = st.text_input('7つ目のNG言葉を入れてください','')
        NGWORD8 = st.text_input('8つ目のNG言葉を入れてください','')
        NGWORD9 = st.text_input('9つ目のNG言葉を入れてください','')
        NGWORD10 = st.text_input('10つ目のNG言葉を入れてください','')
        NGWORD11 = st.text_input('11つ目のNG言葉を入れてください','')
        NGWORD12 = st.text_input('12つ目のNG言葉を入れてください','')
        NGWORD13 = st.text_input('13つ目のNG言葉を入れてください','')
        NGWORD14 = st.text_input('14つ目のNG言葉を入れてください','')
        NGWORD15 = st.text_input('15つ目のNG言葉を入れてください','')
        NGWORD16 = st.text_input('16つ目のNG言葉を入れてください','')
        NGWORD17 = st.text_input('17つ目のNG言葉を入れてください','')
        NGWORD18 = st.text_input('18つ目のNG言葉を入れてください','')
        NGWORD19 = st.text_input('19つ目のNG言葉を入れてください','')
        NGWORD20 = st.text_input('20つ目のNG言葉を入れてください','')

    words = f'{word} -{NGWORD1} -{NGWORD2} -{NGWORD3} -{NGWORD4} -{NGWORD5} -{NGWORD6} -{NGWORD7} -{NGWORD8} -{NGWORD9} -{NGWORD10} -{NGWORD11} -{NGWORD12} -{NGWORD13} -{NGWORD14} -{NGWORD15} -{NGWORD16} -{NGWORD17} -{NGWORD18}  -{NGWORD19} -{NGWORD20} -交換 -会い -ブックレットガチ -表紙 -RT -まってなんか重岡ごめんすぎる -好きだわ❤️❤️❤️ -@ -【求】-みんなからの匿名質問を募集中！ -【日時】 -【取引】 -定期'

            
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    texta = []
    names = []
    a=[]
    b=[]
    for i in range(0,10):
        rag = time.time() - 86400 * i
        rag7 = datetime.datetime.fromtimestamp(rag).strftime('%Y-%m-%d')
        ha =datetime.datetime.now().strftime('%Y-%m-%d')
        tweets = api.search_tweets(q=words,count=100,until = rag7)
        for res in tweets:
            text = res.text
            ida = res.id
            desc = res.user.description
            name = res.user.screen_name
            place=res.created_at
            texta.append(text)
            names.append(name)
            bb={}
            bb=place
            b.append(bb)
            
            
            aa={}
            aa=res.text
            a.append(aa)
    df2=pd.DataFrame(a)
    df3 = pd.DataFrame(b)
    df3 = df3.drop_duplicates()
    b = df3.values.tolist()
    b = str(b)
    c = b.split(')')
    z = len(c)
    zz = z - 1 
    t = []
    l = []
    y = ''
    for i in range(zz):
        if i == 0:
            b = c[i]
            f = b[13:23]
            a.append(f)
            y = f
        else:
            b = c[i]
            f = b[15:25]
            if y == f:
                t.append(f)
                y = f
            else:
                d={}
                kazu = len(t)
                d[y]=kazu
                l.append(d)
                t = []
                t.append(f)
                y = f



    
    """ 
    ## 1.2データの中身

    """
    df2
    SUZI1 = len(df2)
    st.write('取得ツイート数',SUZI1,'(最大900)')
    df2 = df2.drop_duplicates()
    df2
    SUZI2 = len(df2)
    SUZI3 = SUZI1 - SUZI2
    st.write('重複削除後のツイート数',SUZI2,'(削除ツイート数:',SUZI3,')')
    a = df2.values.tolist()

    text = list(itertools.chain.from_iterable(a))
    """ 
    ## 1.3　1週間のツイート数推移

    """
    df3 = l
    st.bar_chart(df3)

    """ 
    # 2.分析

    """

    tokenizer = Tokenizer()

    a=[]
    for sentence in text:
    
        

        for token in tokenizer.tokenize(sentence):
            
            a.append(token.surface)
    if st.checkbox('defalut STOPWORD'):
        """ 
        ##### 以下の言葉は既に除外されています
        ###### ・ひらがな五十音、濁点、小文字
        ###### ・アルファベット小文字
        ###### ・[]、『』、【】や特殊記号
        ###### 
        ###### 
        ###### 
        
        """     
    STOP_COUNT = st.slider('いらない言葉の数を選択してください',0,20,0)        
    if STOP_COUNT == 0:
        st.write('いらない言葉はありません')

    elif STOP_COUNT == 1:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 2:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 3:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 4:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 5:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 6:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 7:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 8:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 9:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 10:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 11:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 12:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 13:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 13:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 14:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 15:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 16:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 17:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 18:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 19:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
        STOPWORD19 = st.text_input('19つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 20:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
        STOPWORD19 = st.text_input('19つ目のいらない言葉を入れてください','')
        STOPWORD20 = st.text_input('20つ目のいらない言葉を入れてください','')
        
    """ 
    ## 2.1分析結果

    """

    defalut = ''        
    defalut1 = 'あ' 
    defalut2 = 'い'
    defalut3 = 'う'
    defalut4 = 'え'
    defalut5 = 'お'
    defalut6 = 'か'
    defalut7 = 'き'
    defalut8 = 'く'
    defalut9 = 'け'
    defalut10 = 'こ'
    defalut11 = 'さ'
    defalut12 = 'し'
    defalut13 = 'す'
    defalut14 = 'せ'
    defalut15 = 'そ'
    defalut16 = 'た'
    defalut17 = 'ち'
    defalut18 = 'つ'
    defalut19 = 'て' 
    defalut20 = 'と'
    defalut21 = 'な'
    defalut22 = 'に'
    defalut23 = 'ぬ'
    defalut24 = 'ね'
    defalut25 = 'の'
    defalut26 = 'は'
    defalut27 = 'ひ'
    defalut28 = 'ふ'
    defalut29 = 'へ'
    defalut30 = 'ほ'
    defalut31 = 'ま'
    defalut32 = 'み'
    defalut33 = 'ぬ'
    defalut34 = 'め'
    defalut35 = 'も'
    defalut36 = 'や'
    defalut37 = 'ゃ'
    defalut38 = 'ゆ'
    defalut39 = 'ゅ'
    defalut40 = 'よ'
    defalut41 = 'ょ'
    defalut42 = 'ら'
    defalut43 = 'り'
    defalut44 = 'る'
    defalut45 = 'れ'
    defalut46 = 'ろ'
    defalut47 = 'わ'
    defalut48 = 'を'
    defalut49 = 'ん'
    defalut50 = 'が'
    defalut51 = 'ぎ'
    defalut52 = 'ぐ'
    defalut52 = 'げ'
    defalut53 = 'ご'
    defalut54 = 'だ'
    defalut55 = 'ぢ'
    defalut56 = 'づ'
    defalut57 = 'で'
    defalut58 = 'ど'
    defalut59 = 'ざ'
    defalut60 = 'じ'
    defalut61 = 'ず'
    defalut62 = 'ぜ'
    defalut63 = 'ぞ'
    defalut64 = 'ば'
    defalut65 = 'び'
    defalut66 = 'ぶ'
    defalut67 = 'べ'
    defalut68 = 'ぼ'
    defalut69 = 'っ'
    defalut70 = '://'
    defalut71 = 'https'
    defalut72 = '('
    defalut73 = ')'
    defalut74 = '（'
    defalut75 = '）'
    defalut76 = '「'
    defalut77 = '」'
    defalut78 = '['
    defalut79 = ']'
    defalut80 = '.'
    defalut81 = ','
    defalut82 = ':'
    defalut83 = '。'
    defalut84 = ' '
    defalut85 = 'a'
    defalut86 = 'b'
    defalut87 = 'c'
    defalut88 = 'd'
    defalut89 = 'e'
    defalut90 = 'f'
    defalut91 = 'g'
    defalut92 = 'h'
    defalut93 = 'i'
    defalut94 = 'j'
    defalut95 = 'k'
    defalut96 = 'l'
    defalut97 = 'm'
    defalut98 = 'n'
    defalut99 = 'o'
    defalut100 = 'p'
    defalut101 = 'q'
    defalut102 = 'r'
    defalut103 = 's'
    defalut104 = 't'
    defalut105 = 'u'
    defalut106 = 'v'
    defalut107 = 'w'
    defalut108 = 'x'
    defalut109 = 'y'
    defalut110 = 'z'
    defalut111 = '、'
    defalut112 = '【'
    defalut113 = '】'
    defalut114 = '/'
    defalut115 = '・'
    defalut116 = '『'
    defalut117 = '』'
    defalut118 = '_'
    defalut119 = '…'


    stopwords = [defalut1,defalut2,defalut3,defalut4,defalut5,defalut6,defalut7,defalut8,defalut9,defalut10,defalut11,defalut12,defalut13,defalut14,defalut15,defalut16,defalut17,defalut18,defalut19,defalut20,defalut21,defalut22,defalut23,defalut24,defalut25,defalut26,defalut27,defalut28,defalut29,defalut30,defalut31,defalut32,defalut33,defalut34,defalut35,defalut36,defalut37,defalut38,defalut39,defalut40,defalut41,defalut42,defalut43,defalut44,defalut45,defalut46,defalut47,defalut48,defalut49,defalut50,defalut51,defalut52,defalut53,defalut54,defalut55,defalut56,defalut57,defalut58,defalut59,defalut60,defalut61,defalut62,defalut63,defalut64,defalut65,defalut66,defalut67,defalut68,defalut69,defalut70,defalut71,defalut72,defalut73,defalut74,defalut75,defalut76,defalut77,defalut78,defalut79,defalut80,defalut81,defalut82,defalut83,defalut84,defalut85,defalut86,defalut87,defalut88,defalut89,defalut90,defalut91,defalut92,defalut93,defalut94,defalut95,defalut96,defalut97,defalut98,defalut99,defalut100,defalut101,defalut102,defalut103,defalut104,defalut105,defalut106,defalut107,defalut108,defalut109,defalut111,defalut112,defalut113,defalut114,defalut115,defalut116,defalut117,defalut118,defalut119,STOPWORD1,STOPWORD2,STOPWORD3,STOPWORD4,STOPWORD5,STOPWORD6,STOPWORD7,STOPWORD8,STOPWORD9,STOPWORD10,STOPWORD11,STOPWORD12,STOPWORD13,STOPWORD14,STOPWORD15,STOPWORD16,STOPWORD17,STOPWORD18,STOPWORD19,STOPWORD20]
    s = pd.DataFrame(a,columns=['sigeoka'])
    npt = nlplot.NLPlot(s,target_col='sigeoka')
    gram =  npt.bar_ngram(title='n-gram',stopwords=stopwords)
    gram

    tree = npt.treemap(
        title='Tree of Most Common Words',
        ngram=1,
        top_n=30,
        width=1300,
        height=600,
        stopwords=stopwords,
        verbose=True,
        save=False
    )
    tree

    stop_words = ['https','t','CO']
    a = "".join(a)
    wordcloud = WordCloud(
        width=900, height=600,   # default width=400, height=200
        background_color="white",   # default=”black”
        stopwords=set(stop_words),
        max_words=100,   # default=200
        min_font_size=4,   #default=4
        collocations = False   #default = True
        ).generate(a)
    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    
def page2():
    st.title('分析')
    """ 
    # 1.データの取得

    """
    if st.checkbox('Example'):
        """ 
        ##### 例                           
        ###### ・日本平ホテルactivesort「7」ホテル番号「304915」
        ###### ・星野リゾート　界　遠州activesort「6」ホテル番号 「358809」 
        ###### 
        """

    STOPWORD1 = ''
    STOPWORD2 = ''
    STOPWORD3 = ''
    STOPWORD4 = ''
    STOPWORD5 = ''
    STOPWORD6 = ''
    STOPWORD7 = ''
    STOPWORD8 = ''
    STOPWORD9 = ''
    STOPWORD10 = ''
    STOPWORD11 = ''
    STOPWORD12 = ''
    STOPWORD13 = ''
    STOPWORD14 = ''
    STOPWORD15 = ''
    STOPWORD16 = ''
    STOPWORD17 = ''
    STOPWORD18 = ''
    STOPWORD19 = ''
    STOPWORD20 = ''
    kazu1 = st.text_input('activeSort','')
    hotels_number = st.text_input('ホテル番号','')

    html = requests.get(f'https://www.jalan.net/yad{hotels_number}/kuchikomi/?screenId=UWW3701&idx=0&activeSort={kazu1}&smlCd=212602&dateUndecided=1&yadNo={hotels_number}&distCd=01')
    soup = BeautifulSoup(html.content,'html.parser')
    all=soup.find_all("p",attrs={"class":"jlnpc-kuchikomiCassette__postBody"})

    a=[]


    for item in all:
        d={}
        d=item.text
        a.append(d)

    df=pd.DataFrame(a)


    for i in range(2,20):
        try: 
            kazu3 = 30*(i - 1)
            
            html = requests.get(f'https://www.jalan.net/yad{hotels_number}/kuchikomi/{i}.HTML?screenId=UWW3701&idx={kazu3}&activeSort=30&smlCd=212602&dateUndecided=1&yadNo={hotels_number}&distCd=01')
            soup = BeautifulSoup(html.content,'html.parser')
            all=soup.find_all("p",attrs={"class":"jlnpc-kuchikomiCassette__postBody"})

            
            for item in all:
                aa={}
                aa=item.text
                a.append(aa)

            df2 = pd.DataFrame()
            df2=pd.DataFrame(a)
            df=pd.concat([df,df2])
                
        except:
            break
    df = df.drop_duplicates()
    """ 
    ## 1.2データの中身

    """
    df
    SUZI1 = len(df)
    st.write('取得口コミ数',SUZI1)
    a = df.values.tolist()
    text = list(itertools.chain.from_iterable(a))
    tokenizer = Tokenizer()

    a=[]
    for sentence in text:
    
        

        for token in tokenizer.tokenize(sentence):
            
            a.append(token.surface)
            

    """ 
    # 2.分析

    """

    if st.checkbox('defalut STOPWORD'):
        """ 
        ##### 以下の言葉は既に除外されています
        ###### ・ひらがな五十音、濁点、小文字
        ###### ・アルファベット小文字
        ###### ・[]、『』、【】や特殊記号
        ###### ・です、でし、まし、ます等
        ###### 
        ###### 
        
        """    

            
            
    STOP_COUNT = st.slider('いらない言葉の数を選択してください',0,20,0)        
    if STOP_COUNT == 0:
        st.write('いらない言葉はありません')

    elif STOP_COUNT == 1:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 2:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 3:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 4:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 5:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 6:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 7:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 8:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 9:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 10:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 11:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 12:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 13:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 13:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 14:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 15:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 16:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 17:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 18:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 19:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
        STOPWORD19 = st.text_input('19つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 20:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
        STOPWORD19 = st.text_input('19つ目のいらない言葉を入れてください','')
        STOPWORD20 = st.text_input('20つ目のいらない言葉を入れてください','')


    defalut = ''        
    defalut1 = 'あ' 
    defalut2 = 'い'
    defalut3 = 'う'
    defalut4 = 'え'
    defalut5 = 'お'
    defalut6 = 'か'
    defalut7 = 'き'
    defalut8 = 'く'
    defalut9 = 'け'
    defalut10 = 'こ'
    defalut11 = 'さ'
    defalut12 = 'し'
    defalut13 = 'す'
    defalut14 = 'せ'
    defalut15 = 'そ'
    defalut16 = 'た'
    defalut17 = 'ち'
    defalut18 = 'つ'
    defalut19 = 'て' 
    defalut20 = 'と'
    defalut21 = 'な'
    defalut22 = 'に'
    defalut23 = 'ぬ'
    defalut24 = 'ね'
    defalut25 = 'の'
    defalut26 = 'は'
    defalut27 = 'ひ'
    defalut28 = 'ふ'
    defalut29 = 'へ'
    defalut30 = 'ほ'
    defalut31 = 'ま'
    defalut32 = 'み'
    defalut33 = 'ぬ'
    defalut34 = 'め'
    defalut35 = 'も'
    defalut36 = 'や'
    defalut37 = 'ゃ'
    defalut38 = 'ゆ'
    defalut39 = 'ゅ'
    defalut40 = 'よ'
    defalut41 = 'ょ'
    defalut42 = 'ら'
    defalut43 = 'り'
    defalut44 = 'る'
    defalut45 = 'れ'
    defalut46 = 'ろ'
    defalut47 = 'わ'
    defalut48 = 'を'
    defalut49 = 'ん'
    defalut50 = 'が'
    defalut51 = 'ぎ'
    defalut52 = 'ぐ'
    defalut52 = 'げ'
    defalut53 = 'ご'
    defalut54 = 'だ'
    defalut55 = 'ぢ'
    defalut56 = 'づ'
    defalut57 = 'で'
    defalut58 = 'ど'
    defalut59 = 'ざ'
    defalut60 = 'じ'
    defalut61 = 'ず'
    defalut62 = 'ぜ'
    defalut63 = 'ぞ'
    defalut64 = 'ば'
    defalut65 = 'び'
    defalut66 = 'ぶ'
    defalut67 = 'べ'
    defalut68 = 'ぼ'
    defalut69 = 'っ'
    defalut70 = '://'
    defalut71 = 'https'
    defalut72 = '('
    defalut73 = ')'
    defalut74 = '（'
    defalut75 = '）'
    defalut76 = '「'
    defalut77 = '」'
    defalut78 = '['
    defalut79 = ']'
    defalut80 = '.'
    defalut81 = ','
    defalut82 = ':'
    defalut83 = '。'
    defalut84 = ' '
    defalut85 = 'a'
    defalut86 = 'b'
    defalut87 = 'c'
    defalut88 = 'd'
    defalut89 = 'e'
    defalut90 = 'f'
    defalut91 = 'g'
    defalut92 = 'h'
    defalut93 = 'i'
    defalut94 = 'j'
    defalut95 = 'k'
    defalut96 = 'l'
    defalut97 = 'm'
    defalut98 = 'n'
    defalut99 = 'o'
    defalut100 = 'p'
    defalut101 = 'q'
    defalut102 = 'r'
    defalut103 = 's'
    defalut104 = 't'
    defalut105 = 'u'
    defalut106 = 'v'
    defalut107 = 'w'
    defalut108 = 'x'
    defalut109 = 'y'
    defalut110 = 'z'
    defalut111 = '、'
    defalut112 = '【'
    defalut113 = '】'
    defalut114 = '/'
    defalut115 = '・'
    defalut116 = '『'
    defalut117 = '』'
    defalut118 = '_'
    defalut119 = '…'
    defalut120 = 'まし'
    defalut121 = 'です'
    defalut122 = 'でし'
    defalut123 = 'ます'
    defalut124 = 'でき'
    defalut125 = 'たい'
    defalut126 = 'から'
    defalut127 = 'ござい'
    defalut128 = 'など'
    defalut129 = 'さん'

    stopwords = [defalut1,defalut2,defalut3,defalut4,defalut5,defalut6,defalut7,defalut8,defalut9,defalut10,defalut11,defalut12,defalut13,defalut14,defalut15,defalut16,defalut17,defalut18,defalut19,defalut20,defalut21,defalut22,defalut23,defalut24,defalut25,defalut26,defalut27,defalut28,defalut29,defalut30,defalut31,defalut32,defalut33,defalut34,defalut35,defalut36,defalut37,defalut38,defalut39,defalut40,defalut41,defalut42,defalut43,defalut44,defalut45,defalut46,defalut47,defalut48,defalut49,defalut50,defalut51,defalut52,defalut53,defalut54,defalut55,defalut56,defalut57,defalut58,defalut59,defalut60,defalut61,defalut62,defalut63,defalut64,defalut65,defalut66,defalut67,defalut68,defalut69,defalut70,defalut71,defalut72,defalut73,defalut74,defalut75,defalut76,defalut77,defalut78,defalut79,defalut80,defalut81,defalut82,defalut83,defalut84,defalut85,defalut86,defalut87,defalut88,defalut89,defalut90,defalut91,defalut92,defalut93,defalut94,defalut95,defalut96,defalut97,defalut98,defalut99,defalut100,defalut101,defalut102,defalut103,defalut104,defalut105,defalut106,defalut107,defalut108,defalut109,defalut111,defalut112,defalut113,defalut114,defalut115,defalut116,defalut117,defalut118,defalut119,defalut120,defalut121,defalut122,defalut123,defalut124,defalut125,defalut126,defalut127,defalut128,defalut129,STOPWORD1,STOPWORD2,STOPWORD3,STOPWORD4,STOPWORD5,STOPWORD6,STOPWORD7,STOPWORD8,STOPWORD9,STOPWORD10,STOPWORD11,STOPWORD12,STOPWORD13,STOPWORD14,STOPWORD15,STOPWORD16,STOPWORD17,STOPWORD18,STOPWORD19,STOPWORD20]        
    s = pd.DataFrame(a,columns=['sigeoka'])
    npt = nlplot.NLPlot(s,target_col='sigeoka')
    gram =  npt.bar_ngram(title='sige',stopwords=stopwords)
    gram

    tree = npt.treemap(
        title='Tree of Most Common Words',
        ngram=1,
        top_n=30,
        width=1300,
        height=600,
        stopwords=stopwords,
        verbose=True,
        save=False
    )
    tree

    stop_words = ['https','t','CO']
    a = "".join(a)
    wordcloud = WordCloud(
        width=900, height=600,   # default width=400, height=200
        background_color="white",   # default=”black”
        stopwords=set(stop_words),
        max_words=100,   # default=200
        min_font_size=4,   #default=4
        collocations = False   #default = True
        ).generate(a)
    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    

def page3():
    st.title('分析')
    """ 
    # 1.データの取得

    """
    if st.checkbox('Example'):
        """ 
        ##### 例                           
        ###### ・日本平ホテル・ホテル番号「13913」
        ###### ・星野リゾート 青森屋・ホテル番号 「40425」 
        ###### 
        """

    STOPWORD1 = ''
    STOPWORD2 = ''
    STOPWORD3 = ''
    STOPWORD4 = ''
    STOPWORD5 = ''
    STOPWORD6 = ''
    STOPWORD7 = ''
    STOPWORD8 = ''
    STOPWORD9 = ''
    STOPWORD10 = ''
    STOPWORD11 = ''
    STOPWORD12 = ''
    STOPWORD13 = ''
    STOPWORD14 = ''
    STOPWORD15 = ''
    STOPWORD16 = ''
    STOPWORD17 = ''
    STOPWORD18 = ''
    STOPWORD19 = ''
    STOPWORD20 = ''

    hotel_number = st.text_input('ホテル番号','')
    a=[]
    for i in range(1,20):
        try: 
            if i == 1:
                
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next=0')
                soup = BeautifulSoup(html.content,'html.parser')

                all=soup.find_all("p",attrs={"class":"jlnpc-kuchikomiCassette__postBody"})

                l=[]
                for item in all:
                    d={}
                    d=item.text
                    l.append(d)


                df=pd.DataFrame(l)





        except:
            break
            
        try: 
            if i == 2:
                number_next = 20
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})


                

    
                for item in all:
                    aa={}
                    aa=item.text
                    a.append(aa)

        
                df2=pd.DataFrame(a)
                df=pd.concat([df,df2])
                
        except:
            break
            
        try: 
            if i == 3:

                number_next = 40
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

        
                for item in all:
                    bb={}
                    bb=item.text
                    a.append(bb)

                df3=pd.DataFrame(a)
                df=pd.concat([df,df3])
                
        except:
            break
            
        try: 
            if i == 4:
                number_next = 60
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})
                for item in all:
                    ee={}
                    ee=item.text
                    a.append(ee)

                df4=pd.DataFrame(a)
                df=pd.concat([df,df4])
        except:
            break      
            
        try: 
            if i == 5:
                number_next = 80
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

        
                for item in all:
                    gg={}
                    gg=item.text
                    a.append(gg)

                df5=pd.DataFrame(a)
                df=pd.concat([df,df5])
        except:
            break
            
        try: 
            if i == 6:
                number_next = 100
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    hh={}
                    hh=item.text
                    a.append(hh)

                df6=pd.DataFrame(a)
                df=pd.concat([df,df6])
        except:
            break
            
        try: 
            if i == 7:
                number_next = 120
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    jj={}
                    jj=item.text
                    a.append(jj)

                df7=pd.DataFrame(a)
                df=pd.concat([df,df7])
        except:
            break

        try: 
            if i == 8:
                number_next = 140
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    kk={}
                    kk=item.text
                    a.append(kk)

                df8=pd.DataFrame(a)
                df=pd.concat([df,df8])
        except:
            break

        try: 
            if i == 9:
                number_next = 160
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

        
                for item in all:
                    oo={}
                    oo=item.text
                    a.append(oo)

                df9=pd.DataFrame(a)
                df=pd.concat([df,df9])
        except:
            break
            
        try: 
            if i == 10:
                number_next = 180
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    pp={}
                    pp=item.text
                    a.append(pp)

                df10=pd.DataFrame(a)
                df=pd.concat([df,df10])
        except:
            break
            
        try: 
            if i == 11:
                number_next = 200
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

        
                for item in all:
                    qq={}
                    qq=item.text
                    a.append(qq)

                df11=pd.DataFrame(a)
                df=pd.concat([df,df11])
        except:
            break
            
        try: 
            if i == 12:
                number_next = 220
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

            
                for item in all:
                    ss={}
                    ss=item.text
                    a.append(ss)

                df12=pd.DataFrame(a)
                df=pd.concat([df,df12])
        except:
            break
            
        try: 
            if i == 13:
                number_next = 240
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                t=[]
                for item in all:
                    tt={}
                    t=item.text
                    a.append(tt)

                df13=pd.DataFrame(a)
                df=pd.concat([df,df13])
        except:
            break

        try: 
            if i == 14:
                number_next = 260
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

            
                for item in all:
                    uu={}
                    uu=item.text
                    a.append(uu)

                df14=pd.DataFrame(a)
                df=pd.concat([df,df14])
        except:
            break
        
        try: 
            if i == 15:
                number_next = 280
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    vv={}
                    vv=item.text
                    a.append(vv)

                df15=pd.DataFrame(a)
                df=pd.concat([df,df15])
        except:
            break    

        try: 
            if i == 16:
                number_next = 300
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    xx={}
                    xx=item.text
                    a.append(xx)

                df16=pd.DataFrame(a)
                df=pd.concat([df,df16])


                
        except:
            break    

        try: 
            if i == 17:
                number_next = 320
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    yy={}
                    yy=item.text
                    a.append(yy)

                df17=pd.DataFrame(a)
                df=pd.concat([df,df17])


                
        except:
            break    

        try: 
            if i == 18:
                number_next = 340
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    zz={}
                    zz=item.text
                    a.append(zz)

                df18=pd.DataFrame(a)
                df=pd.concat([df,df18])


                
        except:
            break   

        try: 
            if i == 19:
                number_next = 360
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    aaa={}
                    aaa=item.text
                    a.append(aaa)

                df19=pd.DataFrame(a)
                df=pd.concat([df,df19])


                
        except:
            break     
    
        try: 
            if i ==20:
                number_next = 380
                html = requests.get(f'https://review.travel.rakuten.co.jp/hotel/voice/{hotel_number}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_version=2&f_static=1&f_point=0&f_sort=0&f_next={number_next}')
                soup = BeautifulSoup(html.content,'html.parser')
                all=soup.find_all("p",attrs={"class":"commentSentence"})

                for item in all:
                    bbb={}
                    bbb=item.text
                    a.append(bbb)

                df20=pd.DataFrame(a)
                df=pd.concat([df,df20])


                
        except:
            break  
    df = df.drop_duplicates()  
    df
    """ 
    ## 1.2データの中身

    """
    SUZI1 = len(df)
    st.write('取得口コミ数',SUZI1)
    a = df.values.tolist()
    text = list(itertools.chain.from_iterable(a))
    tokenizer = Tokenizer()

    a=[]
    for sentence in text:
    
        

        for token in tokenizer.tokenize(sentence):
            
            a.append(token.surface)
            

    """ 
    # 2.分析

    """

    if st.checkbox('defalut STOPWORD'):
        """ 
        ##### 以下の言葉は既に除外されています
        ###### ・ひらがな五十音、濁点、小文字
        ###### ・アルファベット小文字
        ###### ・[]、『』、【】や特殊記号
        ###### ・です、でし、まし、ます等
        ###### 
        ###### 
        
        """    

            
            
    STOP_COUNT = st.slider('いらない言葉の数を選択してください',0,20,0)        
    if STOP_COUNT == 0:
        st.write('いらない言葉はありません')

    elif STOP_COUNT == 1:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 2:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 3:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 4:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 5:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 6:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 7:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 8:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 9:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 10:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 11:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 12:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 13:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 13:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 14:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 15:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 16:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 17:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 18:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 19:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
        STOPWORD19 = st.text_input('19つ目のいらない言葉を入れてください','')
    elif STOP_COUNT == 20:
        STOPWORD1 = st.text_input('1つ目のいらない言葉を入れてください','')
        STOPWORD2 = st.text_input('2つ目のいらない言葉を入れてください','')
        STOPWORD3 = st.text_input('3つ目のいらない言葉を入れてください','')
        STOPWORD4 = st.text_input('4つ目のいらない言葉を入れてください','')
        STOPWORD5 = st.text_input('5つ目のいらない言葉を入れてください','')
        STOPWORD6 = st.text_input('6つ目のいらない言葉を入れてください','')
        STOPWORD7 = st.text_input('7つ目のいらない言葉を入れてください','')
        STOPWORD8 = st.text_input('8つ目のいらない言葉を入れてください','')
        STOPWORD9 = st.text_input('9つ目のいらない言葉を入れてください','')
        STOPWORD10 = st.text_input('10つ目のいらない言葉を入れてください','')
        STOPWORD11 = st.text_input('11つ目のいらない言葉を入れてください','')
        STOPWORD12 = st.text_input('12つ目のいらない言葉を入れてください','')
        STOPWORD13 = st.text_input('13つ目のいらない言葉を入れてください','')
        STOPWORD14 = st.text_input('14つ目のいらない言葉を入れてください','')
        STOPWORD15 = st.text_input('15つ目のいらない言葉を入れてください','')
        STOPWORD16 = st.text_input('16つ目のいらない言葉を入れてください','')
        STOPWORD17 = st.text_input('17つ目のいらない言葉を入れてください','')
        STOPWORD18 = st.text_input('18つ目のいらない言葉を入れてください','')
        STOPWORD19 = st.text_input('19つ目のいらない言葉を入れてください','')
        STOPWORD20 = st.text_input('20つ目のいらない言葉を入れてください','')


    defalut = ''        
    defalut1 = 'あ' 
    defalut2 = 'い'
    defalut3 = 'う'
    defalut4 = 'え'
    defalut5 = 'お'
    defalut6 = 'か'
    defalut7 = 'き'
    defalut8 = 'く'
    defalut9 = 'け'
    defalut10 = 'こ'
    defalut11 = 'さ'
    defalut12 = 'し'
    defalut13 = 'す'
    defalut14 = 'せ'
    defalut15 = 'そ'
    defalut16 = 'た'
    defalut17 = 'ち'
    defalut18 = 'つ'
    defalut19 = 'て' 
    defalut20 = 'と'
    defalut21 = 'な'
    defalut22 = 'に'
    defalut23 = 'ぬ'
    defalut24 = 'ね'
    defalut25 = 'の'
    defalut26 = 'は'
    defalut27 = 'ひ'
    defalut28 = 'ふ'
    defalut29 = 'へ'
    defalut30 = 'ほ'
    defalut31 = 'ま'
    defalut32 = 'み'
    defalut33 = 'ぬ'
    defalut34 = 'め'
    defalut35 = 'も'
    defalut36 = 'や'
    defalut37 = 'ゃ'
    defalut38 = 'ゆ'
    defalut39 = 'ゅ'
    defalut40 = 'よ'
    defalut41 = 'ょ'
    defalut42 = 'ら'
    defalut43 = 'り'
    defalut44 = 'る'
    defalut45 = 'れ'
    defalut46 = 'ろ'
    defalut47 = 'わ'
    defalut48 = 'を'
    defalut49 = 'ん'
    defalut50 = 'が'
    defalut51 = 'ぎ'
    defalut52 = 'ぐ'
    defalut52 = 'げ'
    defalut53 = 'ご'
    defalut54 = 'だ'
    defalut55 = 'ぢ'
    defalut56 = 'づ'
    defalut57 = 'で'
    defalut58 = 'ど'
    defalut59 = 'ざ'
    defalut60 = 'じ'
    defalut61 = 'ず'
    defalut62 = 'ぜ'
    defalut63 = 'ぞ'
    defalut64 = 'ば'
    defalut65 = 'び'
    defalut66 = 'ぶ'
    defalut67 = 'べ'
    defalut68 = 'ぼ'
    defalut69 = 'っ'
    defalut70 = '://'
    defalut71 = 'https'
    defalut72 = '('
    defalut73 = ')'
    defalut74 = '（'
    defalut75 = '）'
    defalut76 = '「'
    defalut77 = '」'
    defalut78 = '['
    defalut79 = ']'
    defalut80 = '.'
    defalut81 = ','
    defalut82 = ':'
    defalut83 = '。'
    defalut84 = ' '
    defalut85 = 'a'
    defalut86 = 'b'
    defalut87 = 'c'
    defalut88 = 'd'
    defalut89 = 'e'
    defalut90 = 'f'
    defalut91 = 'g'
    defalut92 = 'h'
    defalut93 = 'i'
    defalut94 = 'j'
    defalut95 = 'k'
    defalut96 = 'l'
    defalut97 = 'm'
    defalut98 = 'n'
    defalut99 = 'o'
    defalut100 = 'p'
    defalut101 = 'q'
    defalut102 = 'r'
    defalut103 = 's'
    defalut104 = 't'
    defalut105 = 'u'
    defalut106 = 'v'
    defalut107 = 'w'
    defalut108 = 'x'
    defalut109 = 'y'
    defalut110 = 'z'
    defalut111 = '、'
    defalut112 = '【'
    defalut113 = '】'
    defalut114 = '/'
    defalut115 = '・'
    defalut116 = '『'
    defalut117 = '』'
    defalut118 = '_'
    defalut119 = '…'
    defalut120 = 'まし'
    defalut121 = 'です'
    defalut122 = 'でし'
    defalut123 = 'ます'
    defalut124 = 'でき'
    defalut125 = 'たい'
    defalut126 = 'から'
    defalut127 = 'ござい'
    defalut128 = 'など'
    defalut129 = 'さん'

    stopwords = [defalut1,defalut2,defalut3,defalut4,defalut5,defalut6,defalut7,defalut8,defalut9,defalut10,defalut11,defalut12,defalut13,defalut14,defalut15,defalut16,defalut17,defalut18,defalut19,defalut20,defalut21,defalut22,defalut23,defalut24,defalut25,defalut26,defalut27,defalut28,defalut29,defalut30,defalut31,defalut32,defalut33,defalut34,defalut35,defalut36,defalut37,defalut38,defalut39,defalut40,defalut41,defalut42,defalut43,defalut44,defalut45,defalut46,defalut47,defalut48,defalut49,defalut50,defalut51,defalut52,defalut53,defalut54,defalut55,defalut56,defalut57,defalut58,defalut59,defalut60,defalut61,defalut62,defalut63,defalut64,defalut65,defalut66,defalut67,defalut68,defalut69,defalut70,defalut71,defalut72,defalut73,defalut74,defalut75,defalut76,defalut77,defalut78,defalut79,defalut80,defalut81,defalut82,defalut83,defalut84,defalut85,defalut86,defalut87,defalut88,defalut89,defalut90,defalut91,defalut92,defalut93,defalut94,defalut95,defalut96,defalut97,defalut98,defalut99,defalut100,defalut101,defalut102,defalut103,defalut104,defalut105,defalut106,defalut107,defalut108,defalut109,defalut111,defalut112,defalut113,defalut114,defalut115,defalut116,defalut117,defalut118,defalut119,defalut120,defalut121,defalut122,defalut123,defalut124,defalut125,defalut126,defalut127,defalut128,defalut129,STOPWORD1,STOPWORD2,STOPWORD3,STOPWORD4,STOPWORD5,STOPWORD6,STOPWORD7,STOPWORD8,STOPWORD9,STOPWORD10,STOPWORD11,STOPWORD12,STOPWORD13,STOPWORD14,STOPWORD15,STOPWORD16,STOPWORD17,STOPWORD18,STOPWORD19,STOPWORD20]        
    s = pd.DataFrame(a,columns=['sigeoka'])
    npt = nlplot.NLPlot(s,target_col='sigeoka')
    gram =  npt.bar_ngram(title='sige',stopwords=stopwords)
    gram

    tree = npt.treemap(
        title='Tree of Most Common Words',
        ngram=1,
        top_n=30,
        width=1300,
        height=600,
        stopwords=stopwords,
        verbose=True,
        save=False
    )
    tree

    stop_words = ['https','t','CO']
    a = "".join(a)
    wordcloud = WordCloud(
        width=900, height=600,   # default width=400, height=200
        background_color="white",   # default=”black”
        stopwords=set(stop_words),
        max_words=100,   # default=200
        min_font_size=4,   #default=4
        collocations = False   #default = True
        ).generate(a)
    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()




    
    
option = st.sidebar.selectbox(
    '1:twi2:jaran3:rakuten',
    list(range(1,4))
)   

if option == 1:
    page1()
elif option == 2:
    page2()
elif option == 3:
    page3()
