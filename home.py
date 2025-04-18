# home.py
import streamlit as st
st.set_page_config(page_title="제니앱", page_icon="🏠", layout="wide")

from shared import show_menu

show_menu("home")

# 홈 타이틀 영역에 좌측 정렬된 로고 표시 (1.5배 확대)
st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
        <img src="https://raw.githubusercontent.com/clavef/jeniapp/main/logo.png" alt="Jeniapp Logo" style="height: 60px;">
    </div>
""", unsafe_allow_html=True)

# 소개 문구
st.markdown("생활과 업무를 편리하게 만들어주는 다양한 도구들을 제니앱에서 만나보세요.")
st.markdown("\n---")

# 인스타 언팔체크 섹션
st.markdown("### 📱 인스타 언팔체크")
st.write("인스타그램에서 다운로드한 JSON 데이터를 분석해, 내가 팔로우하지만 나를 팔로우하지 않는 계정을 찾아줍니다.")
if st.button("▶️ 인스타 언팔체크 실행하기"):
    st.switch_page("pages/check.py")

# 카드값 계산기 섹션
st.markdown("### 💳 카드값 계산기")
st.write("여러 카드사에서 받은 월별 이용내역을 업로드하면 하나의 통합표로 정리해줍니다.")
if st.button("▶️ 카드값 계산기 실행하기"):
    st.switch_page("pages/cards.py")

# 정산 도우미 섹션
st.markdown("### 📊 정산 도우미")
st.write("엑셀 파일을 업로드해 MBL별 금액 누락 및 불일치를 자동으로 비교합니다.")
if st.button("▶️ 정산 도우미 실행하기"):
    st.switch_page("pages/audit.py")

# 하단 정보 영역
st.markdown("\n---")
st.markdown("""
<div style="font-size: 1rem; line-height: 1.8;">
    🪄 향후 다양한 도구들이 계속 추가될 예정입니다.<br>
    🚀 간편주소(<a href="https://jeni.kr" target="_blank" style="text-decoration: none; color: #ff477a;">https://jeni.kr</a>)로 빠르게 접속해보세요!<br>
    🔷 jeniapp™은 Snowflake®의 지원을 받고 있습니다.<br><br>
    <div style="background-color: #f0f2f6; padding: 0.6em 1em; border-radius: 6px; display: inline-block;">
        © 2025 jeniapp™. All rights reserved.
    </div>
</div>
""", unsafe_allow_html=True)
