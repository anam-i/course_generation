# -*- coding: utf-8 -*-
"""
Created on May 2025

@author: M2M team for KEA
"""

import streamlit as st
import course_content_generation as gen
import course_details as cd
import prompt_course_creation as prompt_creation
import sample_prompts as prompts
import open_ai
from fpdf import FPDF
import io

def save_to_pdf_button():
    if st.session_state['result'] is None:
        content = ''
    else:
        content = st.session_state['result'].strip()

    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("DejaVu", "", "fonts/DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)

    # Output as bytes (string) and encode as BytesIO for download
    pdf_bytes = pdf.output(dest='S').encode('latin-1')  # 'S' returns as string
    pdf_output = io.BytesIO(pdf_bytes)

    if content:
        st.download_button(
            label="Download Lesson as PDF",
            data=pdf_output,
            file_name="lesson.pdf",
            mime="application/pdf"
        )

sample_prompt_dict = {
    None: "",
    "Supervised Machine Learning": prompts.sample_prompt_machine_learning(),
    "Deep Learning Introduction": prompts.sample_prompt_deep_learning(),
    "Business Strategy Basics": prompts.sample_prompt_business_strategy(),
    "Creative Writing Characters": prompts.sample_prompt_creative_writing(),
    "Introduction to Environmental Science": prompts.sample_prompt_environmental_science(),
    "AI Ethics and Responsibility": prompts.sample_prompt_ai_ethics()
}

if __name__ == "__main__":
    # initialize session state
    if 'result' not in st.session_state:
            st.session_state['result'] = ''
    if 'prompt' not in st.session_state:
        st.session_state['prompt'] = ''
    # setting header, description and citation
    st.set_page_config(page_title="Course Content Generation")

    st.header("Generate Lesson")
    st.write('''
    Course Generation Software created by the M2M students.
    ''')

    course_input = cd.get_user_input()
    prompt = prompt_creation.create_course(course_input)

    st.subheader(":books: Course Settings")
    cd.display_course(course_input)
    
    input_prompt = st.text_area("Prompt:", value=prompt, help="Make sure to separate your prompts with ';'")

    st.divider()

    st.subheader(":wrench: AI Settings")

    input_api_key = st.text_input('Enter your API Key:')

    ai_model = st.radio(
        "AI Model",
        ["OpenAI", "Gemini"],
        index=None,
    )

    input_temperature = st.number_input(label='Set creativity (temperature 0.0 - 1.0):', min_value=0.0, max_value=1.0, value=0.7)

    if st.button("Generate Lessons", type="primary"):
        if ai_model == "Gemini":
            st.session_state['result'] = gen.generate_lessons(api_key=input_api_key, full_prompts=input_prompt, temperature=input_temperature)
        else:
            st.session_state['result'] = open_ai.call_gpt(input_api_key, course_input)

    result_prompt = st.text_area("Result:", value=st.session_state['result'])

    save_to_pdf_button()

