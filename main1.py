import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image



st.set_page_config(page_title="Code with Abdullah", page_icon=":tada:", layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")
 
lottie_coding = load_lottieurl("https://lottie.host/d4ccaa48-336f-4a6d-b831-23ee7aa7dd4a/6JxjwqGm7t.json")
image_coding  =Image.open("images/wallpaperflare.com_wallpaper.jpg")
# image_coding2 = Image.open("images/laptop-2620118_1920.jpg")
with st.container():
    st.subheader("Hi, I am Abdullah :wave:")
    st.title("A Web developer from Pakistan")
    st.write("Member Of Team Anas")
    st.write("I am passionate about finding ways to use python and Vba to be more efficient and effective in it")
    st.write("[Learn More >](https://google.com)")
     
with st.container():
    st.write("---")
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my You tube channel you will find tutorials for people who:

            - are looking for a way to have power of python in their day-to-day working.
            - are struggling with use of excel and are looking for a way to use Python and in efficient way.
            - are working with Excel and thinking "There should be a better way."
            
            If this sounds intresting to you, consider subscribing my youtube and accessing my "100 days of python with Abdullah". """)
        st.write("Click Here. . ."
            "[100 day of Python>](https://youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&si=jJFn6E9l29Forle7)")

    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")
    

with st.container(): 
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_c,text_C = st.columns((1,2))
    with image_c:
      st.image(image_coding)
    with text_C:
        st.subheader("Learn Python ")
        st.write(
            """Learn How You can master Python fast. In this tutorial, I'll show you exactly how to do so.
            """
        )
        st.markdown("[Watch this video...](https://youtu.be/qxYbHzn8bbU?si=4sgG24_WTafvcsHF)")
with st.container():
    st.write("---")
    st.header("Get in Touch with me!")
    st.write("##")
    
    contact_form = """
   <form action="https://formsubmit.co/prorana193@gmail.com" method="POST">
        <label for="name">Name</label>
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <label for="email">Email</label>
        <input type="email" name="email" placeholder="Your email" required>
        <label for="message">Message</label>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
