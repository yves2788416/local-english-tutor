"""说英语 · 本地英语陪练 —— 应用入口。

运行方式（项目根目录）：
    .venv\\Scripts\\python.exe -m streamlit run streamlit_app.py
或者直接双击 start.bat
"""

from __future__ import annotations

import streamlit as st

st.set_page_config(
    page_title="说英语 · 本地英语陪练",
    page_icon=":material/record_voice_over:",
    layout="wide",
    initial_sidebar_state="expanded",
)

from core import config, db, llm, seed, ui  # noqa: E402

db.init_db()
seed.ensure_seeded()
ui.init_state()

st.logo(str(config.BASE_DIR / "assets" / "logo.png"), size="large")

settings = config.load_settings()
if not config.SETTINGS_PATH.exists():
    config.save_settings(settings)  # 第一次运行落盘一份，方便用户直接看/改
st.session_state["level"] = settings.get("level", "A1")
st.session_state["settings"] = settings


@st.cache_data(ttl=45, show_spinner=False)
def _model_health() -> dict:
    return llm.health()


pages = {
    "学习": [
        st.Page("app_pages/home.py", title="今日学习", icon=":material/home:", default=True),
        st.Page("app_pages/conversation.py", title="情景对话", icon=":material/forum:"),
    st.Page("app_pages/freetalk.py", title="自由聊", icon=":material/chat:"),
        st.Page("app_pages/pronunciation.py", title="发音纠音", icon=":material/record_voice_over:"),
    ],
    "训练": [
        st.Page("app_pages/vocabulary.py", title="背单词", icon=":material/style:"),
        st.Page("app_pages/idioms.py", title="地道口语", icon=":material/tips_and_updates:"),
        st.Page("app_pages/interview.py", title="面试口试", icon=":material/badge:"),
        st.Page("app_pages/reading.py", title="精读听写", icon=":material/menu_book:"),
    ],
    "资料": [
        st.Page("app_pages/wordbank.py", title="分级词库", icon=":material/library_books:"),
    st.Page("app_pages/library.py", title="精读文库", icon=":material/local_library:"),
        st.Page("app_pages/errors.py", title="错题本", icon=":material/report:"),
    st.Page("app_pages/history.py", title="历史记录", icon=":material/history:"),
    ],
    "系统": [
        st.Page("app_pages/settings.py", title="设置", icon=":material/settings:"),
        st.Page("app_pages/help.py", title="使用说明", icon=":material/help:"),
    ],
}

page = st.navigation(pages, position="sidebar", expanded=True)

with st.sidebar:
    st.caption("本地大模型陪练 · 数据不出本机")

    stats = db.word_stats()
    today = db.get_daily()
    streak_days = db.streak()
    bank = db.wordbank_count()

    with st.container(horizontal=True):
        st.metric("连续学习", f"{streak_days} 天", border=True)
        st.metric("待复习", f"{stats['due']} 词", border=True)

    health = _model_health()
    if health["model_ready"]:
        st.caption(f":green-badge[模型在线] {health['model']}")
    elif health["ok"]:
        st.caption(f":orange-badge[模型未就绪] {health['model']}")
    else:
        st.caption(":red-badge[模型离线]")
        st.caption("Ollama 没连上，点下面「设置」看看。")

    st.caption(
        f"今日：复习 {today['reviews']} · 跟读 {today['pron']} · "
        f"对话 {today['messages']} 轮"
    )
    st.caption(f"词库 {bank} 词 · 我的生词 {stats['total']} 个")

page.run()

ui.tick_study_time()