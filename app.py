import streamlit as st
import google.generativeai as genai

# CẤU HÌNH TRANG WEB
st.set_page_config(page_title="App AI Của Tôi")
st.title("🤖 Chat với AI")

# BÍ KÍP CỦA BẠN (Dán nội dung vào giữa 2 dấu ngoặc kép bên dưới)
my_instruction = """
Bạn là một trợ lý ảo thông minh. Trả lời ngắn gọn.
"""

# NHẬP KHÓA API
api_key = st.text_input("Dán mã API Key của bạn vào đây:", type="password")

if api_key:
    try:
        # KẾT NỐI GOOGLE
        genai.configure(api_key=api_key)
        
        # SỬ DỤNG MODEL MỚI NHẤT ĐỂ TRÁNH LỖI 404
        model = genai.GenerativeModel(
            'ggemini-2.5-flash',  # <--- Đã sửa tên model ở đây
            system_instruction=my_instruction
        )

        # KHUNG CHAT
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        for role, text in st.session_state.chat_history:
            st.chat_message(role).write(text)

        if prompt := st.chat_input("Hỏi gì đi bạn..."):
            st.chat_message("user").write(prompt)
            st.session_state.chat_history.append(("user", prompt))
            
            response = model.generate_content(prompt)
            st.chat_message("ai").write(response.text)
            st.session_state.chat_history.append(("ai", response.text))

    except Exception as e:
        st.error(f"Có lỗi xảy ra: {e}")
