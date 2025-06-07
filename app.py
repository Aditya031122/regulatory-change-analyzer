import streamlit as st
from change_detector import detect_changes
from llm_analysis import analyze_with_llm
import json

st.set_page_config(page_title="Regulatory Change Analyzer", layout="wide")

st.title("📄 Regulatory Change Analyzer")
st.markdown("Upload **two text files** (before and after a regulatory update) and click **Analyze Changes** to see added, deleted, and modified sections with AI-powered analysis.")

# File Uploads
col1, col2 = st.columns(2)
with col1:
    file1 = st.file_uploader("📤 Upload OLD version (text_v1.txt)", type='txt')
with col2:
    file2 = st.file_uploader("📥 Upload NEW version (text_v2.txt)", type='txt')

# Analyze Button
if st.button("🔍 Analyze Changes") and file1 and file2:
    text1 = file1.read().decode()
    text2 = file2.read().decode()
    changes = detect_changes(text1, text2)

    st.markdown("---")

    # Added Sections
    st.subheader("🟢 Added Sections")
    if changes['added']:
        for i, line in enumerate(changes['added'], 1):
            with st.expander(f"➕ Added #{i}: {line[:80]}..."):
                st.code(line, language='markdown')
                st.markdown("**LLM Analysis:**")
                llm_result = analyze_with_llm(line)
                try:
                    parsed = json.loads(llm_result)
                    st.json(parsed)
                except:
                    st.warning("⚠️ Couldn't parse LLM response as JSON")
                    st.text(llm_result)
    else:
        st.info("No added sections found.")

    # Deleted Sections
    st.subheader("🔴 Deleted Sections")
    if changes['deleted']:
        for i, line in enumerate(changes['deleted'], 1):
            with st.expander(f"❌ Deleted #{i}: {line[:80]}..."):
                st.code(line, language='markdown')
    else:
        st.info("No deleted sections found.")

    # Modified Sections
    st.subheader("🟡 Modified Sections")
    if changes['modified']:
        for i, (old, new) in enumerate(changes['modified'], 1):
            with st.expander(f"✏️ Modified #{i}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Before:**")
                    st.code(old, language='markdown')
                with col2:
                    st.markdown("**After:**")
                    st.code(new, language='markdown')
                st.markdown("**LLM Analysis of New Version:**")
                llm_result = analyze_with_llm(new)
                try:
                    parsed = json.loads(llm_result)
                    st.json(parsed)
                except:
                    st.warning("⚠️ Couldn't parse LLM response as JSON")
                    st.text(llm_result)
    else:
        st.info("No modified sections found.")
