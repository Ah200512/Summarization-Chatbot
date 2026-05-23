import os
import streamlit as st #we are using validators to validate the url 
import validators
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, UnstructuredURLLoader

# Set User-Agent environment variable for LangChain components
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

##streamlit app
st.set_page_config(page_title="Summarization App using Langchain", page_icon="🔍")
st.title("Summarization App using Langchain")
st.subheader("Enter the URL of the website or YouTube video you want to summarize")

template = "Summarize the following text in 300 words. Content: {text}"
prompt = PromptTemplate(template=template, input_variables=["text"])

#groq api key and url to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Enter your Groq API Key", type="password")

generic_url = st.text_input("Enter the URL of the website or YouTube video")

if st.button("Summarize the content"):
    if not groq_api_key.strip() or not generic_url.strip(): 
        st.error("Please enter a valid URL and API key")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL")
    else:
        try:
            with st.spinner("Summarizing the content..."):
                # Loading the website or yt
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
                
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    # Attempt to load with standard YoutubeLoader
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=False)
                elif "unstructured" in generic_url:
                    loader = UnstructuredURLLoader(urls=[generic_url], ssl_verify=False, headers=headers)
                else:
                    loader = WebBaseLoader(web_paths=[generic_url], requests_kwargs={"headers": headers})
                
                docs = loader.load()
                
                if not docs:
                    st.error("Could not extract content from the provided URL.")
                else:
                    # Loading the llm
                    llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant", streaming=True)
                    # Loading the prompt
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    # Summarizing the content
                    summary = chain.run(docs)
                    st.write(summary)
                    st.success("Content summarized successfully")
        except Exception as e:
            error_msg = str(e)
            if "Could not retrieve a transcript" in error_msg:
                st.error("YouTube is blocking the transcript request. This often happens due to IP limits or browser-like verification requirements. You might need to use a proxy or run the app locally if you aren't already.")
            else:
                st.error(f"An error occurred: {error_msg}")