import streamlit as st


def footer_home():
    

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:white;"><p>Created with <span style="color: red;">❤️</span> by Biswajit Dhar</p></p>
            
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    

        st.markdown(f"""
    <div style="
        margin-top: 2rem;
        display: flex;
        justify-content: center;
        align-items: center;
    ">
        <p style="font-weight: bold; color: white; margin: 0;">
            Created with <span style="color: red;">❤️</span> by Biswajit Dhar
        </p>
    </div>
""", unsafe_allow_html=True)