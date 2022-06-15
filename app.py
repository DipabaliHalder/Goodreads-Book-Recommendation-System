import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import pickle
import pandas as pd

def fetch_poster(isbn):
    url = "http://covers.openlibrary.org/b/isbn/{}-M.jpg".format(isbn)
    return url

def fetch_book_link(isbn):
    url="https://www.goodreads.com/book/isbn/{}?format=json".format(isbn)
    return url
def top_15_books(books):
    names=[]
    img=[]
    link=[]
    for i in range(17):
        index=books[books['average_rating']>=4.74].index[i]
        isbn=books.iloc[index].isbn13
        img.append(fetch_poster(isbn))
        names.append(books.iloc[index].title)
        link.append(fetch_book_link(isbn))
    return names,img,link

def recommend_books(bk):
    index = books[books['title'] == bk].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    recommended_book_posters = []
    recommended_links=[]
    for i in distances[1:6]:
        isbn = books.iloc[i[0]].isbn13
        recommended_book_posters.append(fetch_poster(isbn))
        recommended_book_names.append(books.iloc[i[0]].title)
        recommended_links.append(fetch_book_link(isbn))
    return recommended_book_names, recommended_book_posters,recommended_links

books=pd.read_pickle('book_list.pkl.pkl')
#books=pickle.load(open('book_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
st.set_page_config(page_title='Book Recommender Engine',page_icon='data:image/png;base64,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')

with st.sidebar:
    selected = option_menu("MAIN MENU", ["Home","Recommend","About","Github Repository"],
        icons=["house", "search", "person-square","github",], menu_icon="cast", default_index=0)

#selected = option_menu(None, ["Home","Recommend","About","Github Repo"],
#        icons=["house", "search", "person-square","github",], menu_icon="cast", default_index=0,
#        orientation="horizontal")

if selected=="Home" or selected=="About" or selected=="Github Repository":
    st.header("Top 15 Books loved by Readers....")
    names, img, link = top_15_books(books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(names[0])
        html = f"<a href='{link[0]}'><img src='{img[0]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col2:
        st.write(names[1])
        html = f"<a href='{link[1]}'><img src='{img[1]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col3:
        st.write(names[2])
        html = f"<a href='{link[2]}'><img src='{img[2]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col4:
        st.write(names[3])
        html = f"<a href='{link[3]}'><img src='{img[3]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col5:
        st.write(names[4])
        html = f"<a href='{link[4]}'><img src='{img[4]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(names[5])
        html = f"<a href='{link[5]}'><img src='{img[5]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col2:
        st.write(names[6])
        html = f"<a href='{link[6]}'><img src='{img[6]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col3:
        st.write(names[8])
        html = f"<a href='{link[8]}'><img src='{img[8]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col4:
        st.write(names[9])
#        st.image(img[9])
#        st.markdown("*[Show Details -->>](%s)*" % link[9])
        html = f"<a href='{link[9]}'><img src='{img[9]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col5:
        st.write(names[10])
#        st.image(img[10])
#        st.markdown("*[Show Details -->>](%s)*" % link[10])
        html = f"<a href='{link[10]}'><img src='{img[10]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(names[11])
#        st.image(img[11])
#        st.markdown("*[Show Details -->>](%s)*" % link[11])
        html = f"<a href='{link[11]}'><img src='{img[11]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col2:
        st.write(names[12])
#        st.image(img[12])
#        st.markdown("*[Show Details -->>](%s)*" % link[12])
        html = f"<a href='{link[12]}'><img src='{img[12]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col3:
        st.write(names[13])
#        st.image(img[13])
#        st.markdown("*[Show Details -->>](%s)*" % link[13])
        html = f"<a href='{link[13]}'><img src='{img[13]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col4:
        st.write(names[14])
#        st.image(img[14])
#        st.markdown("*[Show Details -->>](%s)*" % link[14])
        html = f"<a href='{link[14]}'><img src='{img[14]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
    with col5:
        st.write(names[15])
#        st.image(img[16])
#        st.markdown("*[Show Details -->>](%s)*" % link[16])
        html = f"<a href='{link[15]}'><img src='{img[15]}' width='130' heaight='100'></a>"
        st.markdown(html, unsafe_allow_html=True)
if selected=="Recommend":
    col1, col2 = st.columns(2)
    with col1:
        st.title("BOOK RECOMMENDER SYSTEM")
    with col2:
        st.image("https://cdn.dribbble.com/users/200045/screenshots/13995181/media/2f2d2082928319cb3bcca17be3b1ecf4.gif")
    book_names = np.sort(books['title'].unique())
    book_names = np.insert(book_names, 0, '')
    select_book = st.selectbox("Please type or select a book:", book_names)
    if(st.button('Show Recommendations>>')):
        if(select_book==''):
            st.subheader("*No Book Selected!! Please select a book from the list...*")
        else:
            recommended_book_names, recommended_book_posters,recommended_book_link = recommend_books(select_book)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.write(recommended_book_names[0])
#                st.image(recommended_book_posters[0])
                html = f"<a href='{recommended_book_link[0]}'><img src='{recommended_book_posters[0]}' width='130' heaight='100'></a>"
                st.markdown(html, unsafe_allow_html=True)
#                st.markdown("*[Show Details -->>](%s)*"%recommended_book_link[0])
            with col2:
                st.write(recommended_book_names[1])
#                st.image(recommended_book_posters[1])
                html = f"<a href='{recommended_book_link[1]}'><img src='{recommended_book_posters[1]}' width='130' heaight='100'></a>"
                st.markdown(html, unsafe_allow_html=True)
#                st.markdown("*[Show Details -->>](%s)*"%recommended_book_link[1])
            with col3:
                st.write(recommended_book_names[2])
#                st.image(recommended_book_posters[2])
#                st.markdown("*[Show Details -->>](%s)*"%recommended_book_link[2])
                html = f"<a href='{recommended_book_link[2]}'><img src='{recommended_book_posters[2]}' width='130' heaight='100'></a>"
                st.markdown(html, unsafe_allow_html=True)
            with col4:
                st.write(recommended_book_names[3])
#                st.image(recommended_book_posters[3])
#                st.markdown("*[Show Details -->>](%s)*"%recommended_book_link[3])
                html = f"<a href='{recommended_book_link[3]}'><img src='{recommended_book_posters[3]}' width='130' heaight='100'></a>"
                st.markdown(html, unsafe_allow_html=True)
            with col5:
                st.write(recommended_book_names[4])
                html = f"<a href='{recommended_book_link[4]}'><img src='{recommended_book_posters[4]}' width='130' heaight='100'></a>"
                st.markdown(html, unsafe_allow_html=True)
#                st.image(recommended_book_posters[4])
#                st.markdown("*[Show Details -->>](%s)*"%recommended_book_link[4])

if selected=="About":
    with st.sidebar:
        st.subheader("This is 4th year Btech final year project. This project is a content based book recommendation system implemented using KNN algorithm.")

if selected=="Github Repository":
    with st.sidebar:
        st.subheader("*Click on this [link](https://github.com/DipabaliHalder/Book-Recommender-Engine) for more reference...*")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.write("")
        with col2:
            st.image("https://raw.githubusercontent.com/gist/ManulMax/2d20af60d709805c55fd784ca7cba4b9/raw/bcfeac7604f674ace63623106eb8bb8471d844a6/github.gif",width=150)
        with col3:
            st.write("")

