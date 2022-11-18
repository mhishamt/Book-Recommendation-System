#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import streamlit as st
import numpy as np



st.header('FIND YOUR NEXT READ!📚')
st.subheader("FOR THE BOOK WORMS📖")
model = pickle.load(open("C:/Users/DELL/OneDrive/Desktop/BIG DATA FILES/semester 3/upasana ML2/project/books_recommender_system-main/artifacts/model.pkl",'rb'))
book_names = pickle.load(open("C:/Users/DELL/OneDrive/Desktop/BIG DATA FILES/semester 3/upasana ML2/project/books_recommender_system-main/artifacts/books_name.pkl",'rb'))
final_rating = pickle.load(open("C:/Users/DELL/OneDrive/Desktop/BIG DATA FILES/semester 3/upasana ML2/project/books_recommender_system-main/artifacts/final_rating.pkl",'rb'))
book_pivot = pickle.load(open("C:/Users/DELL/OneDrive/Desktop/BIG DATA FILES/semester 3/upasana ML2/project/books_recommender_system-main/artifacts/book_pivot.pkl",'rb'))

if "button_clicked" not in st.session_state:
  st.session_state.button_clicked = False
def callback():
  st.session_state.button_clicked = True

col13,col14 = st.columns(2)
with col13:
  st.image("https://data.whicdn.com/images/352432682/original.gif")
  if st.button('ABOUT THE WEBSITE'):
    st.markdown("HEY THERE BOOK WORMS! GIVE THE NAME OF THE BOOK AND GET RECOMMENDATIONS BASED ON IT. **THE FEATURES OF GIVEN BOOKS ARE COMPARED WITH THE HELP OF **MACHINE LEARNING**. THEN THE BOOKS ARE RECOMMENDED AND THE ACCOMPANIED DATA IS FETCHED FROM THE DATASET. DEVELOPED BY -- **M HISHAM T**.")
  if (
    st.button('CONNECT WITH US !', on_click=callback)
  or st.session_state):


    st.markdown('**M HISHAM T**')
    st.markdown('📞 +917034000712' )
    if st.button('E-MAIL'):
        st.markdown('🖄 mhishamt98@gmail.com')
    
    if st.button('LINKEDIN'):
      st.markdown('🗟https://www.linkedin.com/in/muhammed-hisham-t-/')
   
    if st.button('INSTAGRAM'):
      st.markdown('⧇https://www.instagram.com/m_hisham_t/')
    
with col14:
    st.image("https://64.media.tumblr.com/1e849fee1deeb3473af5fa4c3a6220de/985055fe9383fe39-7a/s400x600/a9efbb0bfef460b628f0cdca91bd93b1437614ac.gifv")  
    st.image('https://static.arocdn.com/Sites/50/imperialhotels2022/uploads/images/panelimagessquare45/panelimagessquaresmall31/Charles_Dickens_Museum_3.jpg')
    

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url



def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list , poster_url       



selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    st.balloons()
    recommended_books,poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])
    


# In[ ]:




