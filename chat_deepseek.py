import streamlit as st
from langchain_ollama import ChatOllama

#Connection LLM
llm = ChatOllama(model="deepseek-r1:1.5b", base_url="http://localhost:11434")

#Context Window
CONTEXT_WINDOW = 4

#Chat Interface
st.set_page_config(page_title="Chat DeepSeek", layout='centered')
st.title('Converse com o ChatDeepSeek!')


#Session State
if "mensagens" not in st.session_state:
    st.session_state['mensagens'] = []
    
mensagens = st.session_state['mensagens']
for tipo, conteudo in mensagens:
    chat = st.chat_message(tipo)
    chat.markdown(conteudo)



prompt = st.chat_input('Envie sua mensagem para o ChatDeepSeek ...')

if prompt:
    mensagens.append(('human', prompt))
    
    #Return message human
    chat = st.chat_message('human')
    chat.markdown(prompt)
    
    #Invoke LLM
    resposta = llm.invoke(mensagens[-CONTEXT_WINDOW:]).content
    mensagens.append(('ai', resposta))
    
    #Return messagem ai
    chat = st.chat_message('ai')
    chat.markdown(resposta)