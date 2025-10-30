import streamlit as st
from transformers import pipeline

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

# Load the summarization model (cached to avoid reloading)
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Header with styling
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>📚 AI Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Transform long text into concise summaries using AI</p>", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Original Text")
    input_text = st.text_area("Input Text", placeholder="Paste your text here...", height=300, label_visibility="collapsed")
    word_count = len(input_text.split()) if input_text else 0
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
            with st.spinner('Loading AI model and generating summary...'):
                try:
                    summarizer = load_summarizer()
                    # Split text if it's too long
                    max_chunk = 1024
                    if len(input_text) > max_chunk:
                        # Simple chunking
                        chunks = [input_text[i:i+max_chunk] for i in range(0, len(input_text), max_chunk)]
                        summaries = []
                        for chunk in chunks[:3]:  # Limit to 3 chunks
                            result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
                            summaries.append(result[0]['summary_text'])
                        summary = " ".join(summaries)
                    else:
                        result = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
                        summary = result[0]['summary_text']
                    
                    st.session_state.summary = summary
                    st.session_state.summary_word_count = len(summary.split())
                    
                    # Update the summary section
                    with summary_placeholder.container():
                        st.success(summary)
                        st.caption(f"Word count: {st.session_state.summary_word_count}")
                        
                        # Calculate and display reduction percentage
                        reduction = ((word_count - st.session_state.summary_word_count) / word_count) * 100
                        st.info(f"📊 Text reduced by {reduction:.1f}%")
                except Exception as e:
                    st.error(f"Error generating summary: {str(e)}")
        else:
            st.warning("Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>Made with ❤️ by Ketki | Powered by Hugging Face and Streamlit</p>",
    unsafe_allow_html=True
)
