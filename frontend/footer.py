import streamlit as st

def fixed_footer():
    footer_style = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #ffffff;
        color: black;
        text-align: center;
        padding: 10px;
        z-index: 999; /* Ensures it stays on top of other elements */
    }
    </style>
    """
    st.markdown(footer_style, unsafe_allow_html=True)


    text_footer = """
        <div class="footer">
            <p>Do not use GenderMe for any kind of research or commercial purpose.</p>
            <p>App hosted on StreamLit, backend on Render.com.</p>
        </div>
    """

    st.markdown(
        text_footer,
        unsafe_allow_html=True
    )