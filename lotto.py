import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="로또 번호 생성기", layout="centered")
st.title("🎱 로또 번호 생성기")

# 번호에 따른 실제 로또 공 색상 반환
def get_ball_color(num):
    if num <= 10:
        return "#fbc400"  # 1~10: 노랑
    elif num <= 20:
        return "#69c8f2"  # 11~20: 파랑
    elif num <= 30:
        return "#ff7272"  # 21~30: 빨강
    elif num <= 40:
        return "#aaaaaa"  # 31~40: 회색
    else:
        return "#b0d840"  # 41~45: 초록

# 세션 상태에 번호 목록 저장 공간 초기화
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []

# 버튼 영역 (생성 / 초기화)
col1, col2 = st.columns([1, 1])

with col1:
    # [로또번호 생성] 버튼 클릭 이벤트
    if st.button("로또번호 생성"):
        if len(st.session_state.lotto_history) >= 5:
            st.warning("최대 5개 세트까지만 생성할 수 있습니다.")
        else:
            # 1~45 사이 중복 없는 6개 숫자 추출 및 정렬
            new_numbers = sorted(random.sample(range(1, 46), 6))
            st.session_state.lotto_history.append(new_numbers)

with col2:
    # 번호 목록 초기화 버튼
    if st.button("초기화"):
        st.session_state.lotto_history = []
        st.rerun()

st.write("---")

# 화면에 로또 번호 공 표시
for idx, numbers in enumerate(st.session_state.lotto_history, start=1):
    # 공 모양 HTML 생성
    balls_html = "".join([
        f'<div style="background-color:{get_ball_color(n)}; '
        f'width:42px; height:42px; border-radius:50%; display:inline-flex; '
        f'justify-content:center; align-items:center; color:white; '
        f'font-weight:bold; font-size:16px; margin:0 4px; box-shadow: 1px 1px 3px rgba(0,0,0,0.2);">'
        f'{n}</div>'
        for n in numbers
    ])

    # 세트 번호와 공 출력
    st.markdown(
        f'<div style="display:flex; align-items:center; margin-bottom:12px;">'
        f'<span style="font-weight:bold; margin-right:15px; width:45px;">SET {idx}</span>'
        f'{balls_html}'
        f'</div>',
        unsafe_allow_html=True
    )