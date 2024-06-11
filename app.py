from openai import OpenAI, RateLimitError
import streamlit as st
import time
#function to handle any sort of error
def response_error_handler(var: Exception):
    word = ""
    # condition for RateLimitError
    # This error occurs when All tokens have been used or
    # The API key does not have billing details attached
    if(type(var) == RateLimitError):
        word = "Rate Limit Reached. Could not generate responses. :/"

    yield word
    time.sleep(0.05)


# function to handle all responses from the client
def response_stream_generator(_client: OpenAI):
    try:
        stream = _client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
    except Exception as e:
        stream = response_error_handler(e)

    return stream

st.title("ChatGPT APP")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = response_stream_generator(client)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
    