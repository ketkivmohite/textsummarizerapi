import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
        background-color: #FF4B4B;
        color: white;
    }
    .stTextArea>div>div>textarea {
        min-height: 200px;
    }
    </style>
""", unsafe_allow_html=True)

# Header with styling
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>📚 AI Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Transform long text into concise summaries using AI</p>", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Original Text")
    input_text = st.text_area("", placeholder="Paste your text here...", height=300)
    word_count = len(input_text.split())
    st.caption(f"Word count: {word_count}")

with col2:
    st.markdown("### Summary")
    if 'summary' not in st.session_state:
        st.session_state.summary = ""
        st.session_state.summary_word_count = 0
    
    summary_placeholder = st.empty()
    if st.session_state.summary:
        with summary_placeholder.container():
            st.success(st.session_state.summary)
            st.caption(f"Word count: {st.session_state.summary_word_count}")

# Center the button using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✨ Generate Summary"):
        if input_text.strip():
            with st.spinner('Generating summary...'):
                try:
                    response = requests.post(
                        "http://127.0.0.1:8000/summarize",
                        json={"text": input_text},
                        timeout=30
                    )
                    if response.status_code == 200:
                        summary = response.json()["summary"]
                        st.session_state.summary = summary
                        st.session_state.summary_word_count = len(summary.split())
                        
                        # Update the summary section
                        with summary_placeholder.container():
                            st.success(summary)
                            st.caption(f"Word count: {st.session_state.summary_word_count}")
                            
                            # Calculate and display reduction percentage
                            reduction = ((word_count - st.session_state.summary_word_count) / word_count) * 100
                            st.info(f"📊 Text reduced by {reduction:.1f}%")
                    else:
                        st.error("Failed to generate summary. Please try again.")
                except requests.exceptions.RequestException:
                    st.error("Cannot connect to the summarization service. Please make sure the backend is running.")
        else:
            st.warning("Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>Made with ❤️ by Ketki | Powered by FastAPI and Streamlit</p>",
    unsafe_allow_html=True
)
