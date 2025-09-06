# auth_utils_test.py - Test version without Firebase dependencies
import streamlit as st

def check_login():
    """テスト用ログイン関数 - 常にTrue"""
    # セッション状態を初期化
    if 'user' not in st.session_state:
        st.session_state.user = {'uid': 'test-user', 'email': 'test@example.com'}
    if 'remaining_uses' not in st.session_state:
        st.session_state.remaining_uses = 10
    if 'plan' not in st.session_state:
        st.session_state.plan = 'Pro'
    return True

def update_user_uses_in_firestore(user):
    """テスト用使用回数更新関数"""
    if st.session_state.remaining_uses > 0:
        st.session_state.remaining_uses -= 1
        return True
    return False

def upload_image_to_firebase_storage(user, image_bytes, filename):
    """テスト用画像アップロード関数"""
    return f"https://example.com/images/{filename}"

def add_diagnosis_record_to_firestore(user, data):
    """テスト用診断記録関数"""
    return True