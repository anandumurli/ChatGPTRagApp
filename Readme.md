# ChatGPT app using StreamLit

In this project we are trying to implemet a RAG chatbot using ChatGPT API. We are implementing the chatbot using streamlit, which porvides a user friendly GUI to the bot.


## Use case - We are trying to build a chatbot that can book appointment

We are trying for the bot to be able to store the information of a customer as an SQL entry into the db and "Make an appointment virtually from anywhere".


## How to run the project
1) Clone the repo.
2) Create a virtual env (Optional step).
3) Install the requirements from the ``requirements.txt`` file.
4) Add your openAI API key in the `` .streamlit\secrets.toml `` file as ``` OPEN_API_KEY = "your_API_key" ```.
4) Run the command ``` streamlit run app.py ``` || ``` python -m streamlit run app.py ```