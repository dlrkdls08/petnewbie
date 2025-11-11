import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="펫뉴비 | PetNewbie", page_icon="🐾", layout="wide")

# 폰트 & 스타일
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    html, body, [class*="css"] {
        font-family: 'Jua', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 64px;
        color: #FF7F50;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    .section-title {
        font-size: 28px;
        color: #333333;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    .app-button {
        background-color: #FFF8F0;
        border: 2px solid #FFB6A3;
        border-radius: 20px;
        text-align: center;
        padding: 20px;
        font-size: 20px;
        transition: 0.2s;
        cursor: pointer;
    }
    .app-button:hover {
        background-color: #FFE4D6;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "input"

# -----------------------------
# 페이지 전환 함수
# -----------------------------
def go_to(page_name):
    st.session_state.page = page_name

# -----------------------------
# 1️⃣ 반려동물 정보 입력 페이지
# -----------------------------
if st.session_state.page == "input":
    st.markdown("<h1 class='main-title'>🐾 PetNewbie 🐾</h1>", unsafe_allow_html=True)
    st.markdown("### 반려동물의 모든 순간을 함께하는 스마트 파트너 🐶🐱")

    st.divider()
    st.markdown("<h3 class='section-title'>반려동물 정보 입력</h3>", unsafe_allow_html=True)

    with st.form("pet_info_form"):
        name = st.text_input("이름을 입력하세요 🐾")
        species = st.selectbox("종을 선택하세요", ["강아지", "고양이", "토끼", "기타"])
        age = st.number_input("나이 (년 단위)", min_value=0, max_value=50, step=1)
        personality = st.text_input("성격을 입력해주세요 (예: 활발함, 차분함 등)")
        health = st.selectbox("현재 건강 상태", ["좋음", "보통", "관리 필요"])
        submitted = st.form_submit_button("완료 ✅")

    if submitted:
        st.session_state.pet_info = {
            "이름": name, "종": species, "나이": age,
            "성격": personality, "건강": health
        }
        go_to("home")

# -----------------------------
# 2️⃣ 홈 화면 (앱 아이콘)
# -----------------------------
elif st.session_state.page == "home":
    pet = st.session_state.pet_info
    st.markdown(f"<h1 class='main-title'>🐾 {pet['이름']}의 펫홈 🐾</h1>", unsafe_allow_html=True)
    st.markdown("### 원하는 기능을 선택하세요!")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🩺 예방접종/건강 알림"):
            go_to("health")
        if st.button("📸 반려일기 / 사진 앨범"):
            go_to("album")
    with col2:
        if st.button("🍖 체중/식사 기록"):
            go_to("meal")
        if st.button("💬 초보자 커뮤니티"):
            go_to("community")
    with col3:
        if st.button("🏥 병원 방문 & 영수증 관리"):
            go_to("hospital")
        if st.button("👩‍⚕️ 전문가 상담 연결"):
            go_to("expert")

    st.divider()
    if st.button("🔙 정보 수정하기"):
        go_to("input")

# -----------------------------
# 3️⃣ 개별 기능 페이지
# -----------------------------

# 🩺 건강 알림
elif st.session_state.page == "health":
    st.header("🩺 예방접종 및 건강검진 알림")
    st.info("등록된 반려동물의 나이와 종에 맞춰 예방접종 및 건강검진 일정을 추천해드립니다.")
    if st.button("🏠 홈으로"):
        go_to("home")

# 🍖 체중/식사 기록
elif st.session_state.page == "meal":
    st.header("🍖 체중 및 식사 기록")
    weight = st.number_input("오늘의 체중 (kg)", min_value=0.0, step=0.1)
    meal = st.text_input("오늘의 식사 내용")
    if st.button("기록 저장"):
        st.success("기록이 저장되었습니다!")

    st.subheader("📈 체중 변화 그래프 (예시)")
    df = pd.DataFrame({"날짜": ["1일", "2일", "3일"], "체중": [3.5, 3.6, 3.7]})
    plt.plot(df["날짜"], df["체중"], marker="o")
    plt.title("체중 변화")
    st.pyplot(plt)

    if st.button("🏠 홈으로"):
        go_to("home")

# 🏥 병원 방문 기록
elif st.session_state.page == "hospital":
    st.header("🏥 병원 방문 기록 & 영수증 관리")
    st.file_uploader("영수증을 업로드하세요")
    st.text_area("진료 내용 기록")
    if st.button("저장"):
        st.success("기록이 저장되었습니다.")
    if st.button("🏠 홈으로"):
        go_to("home")

# 📸 반려일기 / 사진 앨범
elif st.session_state.page == "album":
    st.header("📸 반려일기 / 사진 앨범")
    uploaded = st.file_uploader("사진을 업로드하세요", accept_multiple_files=True)
    if uploaded:
        for img in uploaded:
            st.image(img, width=250)
    if st.button("🏠 홈으로"):
        go_to("home")

# 💬 커뮤니티
elif st.session_state.page == "community":
    st.header("💬 초보자 커뮤니티")
    post = st.text_area("게시글 작성")
    if st.button("등록"):
        st.success("게시글이 등록되었습니다!")
    st.write("📋 최근 게시글 (예시)")
    st.info("🐾 [사용자A] 산책 후 아이가 피곤해해요... 조언 부탁드려요!")
    st.info("🐾 [사용자B] 첫 목욕은 언제 하는 게 좋을까요?")
    if st.button("🏠 홈으로"):
        go_to("home")

# 👩‍⚕️ 전문가 상담
elif st.session_state.page == "expert":
    st.header("👩‍⚕️ 전문가 상담 연결")
    st.markdown("""
    - 🏥 **수의사 상담** : 010-1234-5678  
    - 🧠 **반려동물 심리상담사** : 010-2345-6789  
    - 💇‍♀️ **미용 전문가** : 010-3456-7890  
    """)
    st.info("복사하려면 번호를 선택 후 Ctrl+C 하세요.")
    if st.button("🏠 홈으로"):
        go_to("home")
