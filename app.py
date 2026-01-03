import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Kiểm tra Model", page_icon="🛠")
st.title("🛠 Công cụ kiểm tra Model Google")

api_key = st.text_input("Nhập API Key của bạn để kiểm tra:", type="password")

if api_key:
    try:
        # 1. Kết nối thử
        genai.configure(api_key=api_key)
        st.info("Đang kết nối tới Google...")
        
        # 2. Lấy danh sách Model thực tế
        models = genai.list_models()
        
        found_models = []
        st.write("### 👇 Danh sách Model mà Key của bạn nhìn thấy:")
        
        # Lọc ra các model dùng để chat
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                model_name = m.name.replace('models/', '')
                st.success(f"✅ Tìm thấy: {model_name}")
                found_models.append(model_name)
        
        if not found_models:
            st.error("❌ Không tìm thấy model nào hỗ trợ Chat! (Có thể Key bị lỗi hoặc chưa kích hoạt)")
        else:
            st.write("---")
            st.write("### 🧪 Test thử Chat với model đầu tiên:")
            # Tự động chọn cái đầu tiên tìm được để chạy thử
            test_model_name = found_models[0]
            st.write(f"Đang thử gọi model: `{test_model_name}`")
            
            try:
                # Thử gọi không dùng system_instruction trước để loại trừ lỗi thư viện
                model = genai.GenerativeModel(test_model_name)
                response = model.generate_content("Chào bạn, bạn có khỏe không?")
                st.balloons()
                st.write("🤖 AI Trả lời thành công:", response.text)
                st.success(f"CHÚC MỪNG! Tên model chính xác bạn cần dùng là: '{test_model_name}'")
            except Exception as e_chat:
                st.error(f"Lỗi khi chat thử: {e_chat}")

    except Exception as e:
        st.error(f"Lỗi kết nối nghiêm trọng: {e}")
        st.warning("Gợi ý: Kiểm tra lại file requirements.txt xem đã có dòng 'google-generativeai>=0.7.0' chưa?")
