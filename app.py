import os
import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import home, accounts, recommendations, reviews, your_reviews, about
load_dotenv()

st.set_page_config(
        page_title="MovieMate",
)

st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
    """, unsafe_allow_html=True)
print(os.getenv('analytics_tag'))


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title=' MovieMate ',
                options=['Home','Account','Recommendations','Reviews','Your Reviews','About'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
        
        if app == "Home":
            home.app()
        if app == "Account":
            accounts.app()    
        if app == "Recommendations":
            recommendations.app()        
        if app == 'Reviews':
            reviews.app()
        if app == 'Your Reviews':
            your_reviews.app()    
        if app=='About':
            about.app()    
                     
    run()            
         
