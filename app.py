from PIL import Image
import streamlit as st
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro-vision')
apikey = 'AIzaSyD2_BY1YIYvhxEw7lMk0XuDzA3pwHV4nYU'

genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-pro-vision')



def generate_caption(image):
    # Add your caption generation logic here
    caption = "Generated caption for the image"
    return caption

def main():
    st.title("Caption Generation Website")
    st.write("Upload an image and get a caption!")
    social_network = st.selectbox("Select a social network", ["Facebook", "Twitter", "Instagram"])
    description = st.text_input("Enter a description")
    

    # Rest of the code...

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Generate Caption"):
            caption = generate_caption(image)
            st.write("Caption:", caption)
            response = model.generate_content(image)

            response = model.generate_content([f"generate a caption for this image for posting it on social media with hashtags and emojis for ${social_network}", image], stream=True)
            response.resolve()
            st.write(response.text)

if __name__ == "__main__":
    main()