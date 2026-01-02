import streamlit as st
import google.generativeai as genai

# CẤU HÌNH TRANG WEB
st.set_page_config(page_title="App AI Của Tôi")
st.title("🤖 Chat với AI")

# BÍ KÍP CỦA BẠN (Dán nội dung vào giữa 2 dấu ngoặc kép bên dưới)
# Lưu ý: Không xóa 3 dấu ngoặc kép ở đầu và cuối!
my_instruction = """
Tôi muốn tạo một App về Prompt Generator. Tôi sẽ đưa cho bạn ý tưởng, vài ý kiến, bạn sẽ giúp tôi viết tạo ra một prompt chuẩn chuyên nghiệp như một chuyên gia viết prompt với 20 năm kinh nghiệm, dùng tạo ảnh, tạo video, tạo bài biết... Giao diện hiện đại, phong cách tương tai.
Gemini 3 Flash Preview
Ran for 9s
lightbulb
Thought for 9 seconds
metadata.json
check_circle
index.html
check_circle
index.tsx
check_circle
types.ts
check_circle
constants.tsx
check_circle
geminiService.ts
check_circle
App.tsx
check_circle
User
Thêm nút để tạo ra ảnh, video, bài viết và vừa tạo ra prompt đó. Click on để view large on new tap, và có nút để tải ảnh, video, bài viết đó xuống
Gemini 3 Flash Preview
Ran for 142s
lightbulb
Thought for 7 seconds
I will now update the application to include direct generation capabilities for images, videos, and articles, along with the professional prompt generation.
Specification of Updates:
AI Integration:
Images: Integrated gemini-2.5-flash-image to generate visual assets based on the engineered prompt.
Videos: Integrated veo-3.1-fast-generate-preview for high-quality video generation (including mandatory API key selection check for Veo models).
Articles: Enhanced text generation for full-length content.
User Interface Enhancements:
Added an "Execute Construction" button that performs both prompt engineering and asset generation in one workflow.
Created a Preview Gallery to showcase the generated image or video.
Implemented "View Fullscreen" for images/videos and "Download Asset" buttons.
Added a Progress System for video generation with reassuring status messages (since video takes longer).
Functionality:
Automatic triggering of the openSelectKey() dialog for video generation if a key hasn't been selected.
Safe handling of base64 data for downloads.
Direct link to billing documentation as required by the Veo guidelines.
Implementation:
geminiService.ts
check_circle
App.tsx
check_circle
Analyzed errors for 79 seconds
lightbulb
Thought for 76 seconds
App.tsx
check_circle
geminiService.ts
check_circle
User
tạo một nút riêng để cho generator hình, video, bài viết, và nút riêng để tạo prompt
Gemini 3 Flash Preview
Ran for 33s
lightbulb
Thought for 5 seconds
App.tsx
check_circle
User
chỉnh lại, hình không có xuất hiện ở tap mới, khi bấm vào
Gemini 3 Flash Preview
Ran for 31s
lightbulb
Thought for 24 seconds
Để giải quyết vấn đề hình ảnh không hiển thị khi mở tab mới (thường do trình duyệt chặn mở trực tiếp URL Base64 dung lượng lớn), tôi sẽ cập nhật logic để chuyển đổi dữ liệu hình ảnh sang Blob URL. Đồng thời, tôi sẽ tinh chỉnh giao diện để tách biệt rõ ràng hai nút: Engineer Prompt (Xây dựng kịch bản) và Asset Synthesis (Tạo sản phẩm cuối).
Các thay đổi chính:
Logic Hình ảnh: Trong geminiService.ts, hàm generateImage giờ đây sẽ trả về một Object URL thay vì chuỗi Base64. Điều này giúp trình duyệt xử lý việc hiển thị ở tab mới và tải xuống ổn định hơn.
Giao diện Nút bấm: Tách biệt hoàn toàn hai khối chức năng. Người dùng có thể chọn chỉ tạo Prompt để tinh chỉnh thủ công, hoặc nhấn nút Tạo để AI thực hiện sản phẩm (Ảnh/Video/Bài viết) dựa trên Prompt đã có hoặc ý tưởng gốc.
Tính năng Xem/Tải: Đảm bảo nút "Mở toàn màn hình" hoạt động mượt mà cho cả Ảnh và Video bằng cách sử dụng Blob.
geminiService.ts
check_circle
App.tsx
check_circle
User
thêm một phần để tôi tải ảnh lên, sau đó bạn sẽ phân tích tấm hình đó và generate ra prompt
Gemini 3 Flash Preview
Ran for 17s
lightbulb
Thought for 9 seconds
Tôi sẽ nâng cấp hệ thống để tích hợp thêm bộ giải mã hình ảnh (Visual Decoder). Bạn có thể tải ảnh lên, AI sẽ phân tích mọi chi tiết từ phong cách, ánh sáng đến bố cục để tạo ra một bản thiết kế (Prompt) chuyên nghiệp nhất.
Các cập nhật chính:
Hệ thống tải tệp: Thêm khu vực kéo thả hoặc chọn ảnh với hiệu ứng radar quét đặc trưng của tương lai.
Visual Intelligence: Sử dụng model gemini-3-flash-preview để phân tích ảnh đầu vào và chuyển đổi thành mô tả kỹ thuật cao.
Bố cục giao diện: Khu vực tải ảnh được đặt ngay trên phần nhập liệu văn bản, cho phép bạn kết hợp cả ảnh và mô tả để tạo ra Prompt tối ưu nhất.
geminiService.ts
check_circle
App.tsx
check_circle
User
Please implement the following improvements to the app based on previous feedback:
Standardize output prompt format: Ensure that all generated prompts follow a consistent schema with clearly labeled sections in this order: [SUBJECT], [STYLE], [LIGHTING], [COMPOSITION], [CAMERA / RENDER], [MOOD], [NEGATIVE PROMPT], [ASPECT RATIO / QUALITY]. The generated prompt should always include these sections, even if some are empty, to provide predictable structure for users and compatibility with Midjourney/Veo/Sora.
Enhance Visual Decoder: When analyzing an uploaded image, separate the output into two distinct categories: (a) Observed description (what the image visibly shows) and (b) Inferred details (likely style, lens/camera, estimated lighting setup). Include fields such as "INFERRED STYLE", "LIKELY CAMERA", and "ESTIMATED LIGHT SETUP". Also add a toggle allowing the user to choose between "Literal analysis" (strictly based on visible details) and "Creative reconstruction" (allows AI to creatively infer style and composition beyond what's visible). The default should be Literal analysis.
Restructure the UI into a three-step wizard:
Step 1 – Input: User enters text and optionally uploads an image. Provide clear fields for each input and hints where appropriate.
Step 2 – Engineer Prompt: Display the engineered prompt in the standardized format from step 1. Allow the user to edit or copy the prompt here.
Step 3 – Generate Asset: User chooses to generate an image, video, or article using the engineered prompt. Separate this final generation step from the prompt engineering.
Input validation and hints: Add validation to check if the input text is too short (e.g., fewer than a few keywords) and warn users. If a video mode is selected but the prompt lacks motion-related keywords, automatically add a default camera movement suggestion and inform the user. If an image is uploaded without selecting a template, provide a hint to choose an appropriate template.
System Template presets and locking: Make system templates read-only and provide preset descriptions (e.g., "Midjourney Expert – hyper-realistic, cinematic, print-ready", "Visual Narrative – complex camera angles, visual storytelling", etc.). Users should select from presets but not modify the core template text.
Prompt history: Keep a local history of the 10–20 most recent prompts generated (can be stored in localStorage). Provide a simple list or dropdown where users can select a previous prompt to reload it.
Please update the codebase to incorporate these improvements, maintaining the existing functionality while enhancing the user experience for both novice and advanced users.
Gemini 3 Flash Preview
Ran for 7s
lightbulb
Thought for 7 seconds
types.ts
check_circle
geminiService.ts
check_circle
App.tsx
check_circle
constants.tsx
check_circle
User
Please modify the app so that after an asset (e.g., an image) has been generated in Step 3, the user can still return to Step 1 and edit the raw idea text. Do not disable the raw idea input after generation; allow users to revise their initial idea and regenerate a new prompt and asset as needed. The UI should keep the original input accessible and editable even after a generation cycle.
Gemini 3 Flash Preview
Ran for 45s
lightbulb
Thought for 13 seconds
App.tsx
check_circle
lightbulb_tips
Suggestions
"""

# NHẬP KHÓA API
api_key = st.text_input("Dán mã API Key của bạn vào đây:", type="password")

if api_key:
    try:
        # KẾT NỐI GOOGLE
        genai.configure(api_key=api_key)
        
        # TẠO AI VỚI BÍ KÍP
        model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction=my_instruction
        )

        # KHUNG CHAT
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Hiện tin nhắn cũ
        for role, text in st.session_state.chat_history:
            st.chat_message(role).write(text)

        # Nhập tin nhắn mới
        if prompt := st.chat_input("Hỏi gì đi bạn..."):
            st.chat_message("user").write(prompt)
            st.session_state.chat_history.append(("user", prompt))
            
            # AI Trả lời
            response = model.generate_content(prompt)
            st.chat_message("ai").write(response.text)
            st.session_state.chat_history.append(("ai", response.text))

    except Exception as e:
        st.error(f"Có lỗi xảy ra: {e}")
