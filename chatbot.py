from logic import load_faq_data, respond_to_input
import streamlit as st

# 1. FAQデータの初期化
if "faq_data" not in st.session_state:
    st.session_state.faq_data = load_faq_data()

# 2. 会話履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. FAQデータを展開
questions, answers = st.session_state.faq_data

# 4. ユーザー入力を受け付ける（チャットUI）
user_input = st.chat_input("Ask a question")

# 5. ユーザー入力があれば処理（まず追加してから表示）
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = respond_to_input(user_input, questions, answers)
    st.session_state.messages.append({"role": "ai", "content": response})

# 6. 会話履歴を毎回全て再表示（ここが重要！）
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
