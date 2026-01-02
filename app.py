import streamlit as st
import google.generativeai as genai

# 1. Cấu hình giao diện Web
st.set_page_config(page_title="Trợ lý AI của Tôi", page_icon="🤖")
st.title("🤖 Trợ lý AI - Sức mạnh từ Google Gemini")
st.write("Chào bạn! Tôi có thể giúp gì cho bạn hôm nay?")

# 2. Nhập API Key (để bảo mật, khách phải nhập key hoặc bạn cài sẵn)
# Ở đây mình làm ô nhập Key để bạn test cho dễ nhé
api_key = st.sidebar.text_input("Nhập Google API Key của bạn", type="password")

# 3. Xử lý khi có Key
if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Chọn model (bạn có thể đổi thành gemini-1.5-flash cho nhanh)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Khởi tạo lịch sử chat
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Hiển thị lịch sử chat cũ
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # 4. Khu vực chat
        if prompt := st.chat_input("Nhập câu hỏi của bạn..."):
            # Hiện câu hỏi của người dùng
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            # AI trả lời
            with st.chat_message("assistant"):
                try:
                    # Gọi Google Gemini trả lời
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Lỗi rồi: {e}")

    except Exception as e:
        st.error("API Key không hợp lệ!")
else:
    st.warning("👈 Vui lòng nhập API Key ở menu bên trái để bắt đầu chat!")
