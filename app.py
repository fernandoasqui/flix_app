import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from home.page import show_home
from login.page import show_login


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix APP')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início', 'Gênero', 'Atore/Atrizes', 'Filmes', 'Avaliações']
        )

        if menu_option == 'Início':
            show_home()

        if menu_option == 'Gênero':
            show_genres()

        if menu_option == 'Atore/Atrizes':
            show_actors()

        if menu_option == 'Filmes':
            show_movies()

        if menu_option == 'Avaliações':
            show_reviews()


if __name__ == '__main__':
    main()
