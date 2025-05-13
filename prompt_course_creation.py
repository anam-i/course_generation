def create_course(user_input):
    COURSE_TITLE = user_input['Course Title']
    SUBJECT_DOMAIN = user_input['Subject Domain']
    NUMBER_OF_MODULES = user_input['Number of Modules']
    TOTAL_HOURS = user_input['Hours']
    HOURS_PER_MODULE = user_input['Hours per Module']
    LEARNER_LEVEL = user_input['Expertise Level']
    MODE_OF_DELIVERY = user_input['Delivery Mode']
    LEARNER_TYPE = user_input['Target Audience']
    PREREQUISITE = user_input['Prerequisites']
    COURSE_DESCRIPTION =user_input['Course Description']
    LIST_OF_LEARNING_OUTCOMES =user_input['Learning Objectives']
    COURSE_OUTLINE = user_input['Course Outline']
    LIST_OF_INSTRUCTIONAL_METHODS = user_input['Preferred Content Format']
    TONE = user_input['Tone']
    ASSESSMENT_STRATEGY = user_input['Assessments']
    NUMBER_OF_KEY_CONCEPTS = user_input['Key Concepts']

    return(
        f"## SYSTEM ROLE\n"
        f"You are a veteran online course designer and instructor with over 20 years of experience "
        f"teaching {SUBJECT_DOMAIN}. Your task is to generate a comprehensive, fully written, "
        f"{NUMBER_OF_MODULES}-module course on {COURSE_TITLE} (total duration: {TOTAL_HOURS} hours, "
        f"{HOURS_PER_MODULE} hours per module). The course must be informative, engaging, and "
        f"accessible to learners at the {LEARNER_LEVEL} level. Course delivery mode will be {MODE_OF_DELIVERY}.\n\n"

        f"## USER INPUT\n"
        f"- Course Title: {COURSE_TITLE}\n"
        f"- Subject Domain: {SUBJECT_DOMAIN}\n"
        f"- Audience & Context: {LEARNER_TYPE}; {PREREQUISITE}\n"
        f"- Delivery Format: Detailed narrative course content, organized into modules, sessions, and learning activities.\n"
        f"- Total Duration: {NUMBER_OF_MODULES} modules (each {HOURS_PER_MODULE} hours; total {TOTAL_HOURS} hours)\n"
        f"- Course Description: {COURSE_DESCRIPTION}\n"
        f"- Learning Outcomes:\n{LIST_OF_LEARNING_OUTCOMES}\n"
        f"- Course Outline (aligned to textbook or structure):\n{COURSE_OUTLINE}\n"
        f"- Instructional Methods: {LIST_OF_INSTRUCTIONAL_METHODS}\n"
        f"- Tone: {TONE}\n"
        f"- Assessment Strategy: {ASSESSMENT_STRATEGY}\n"
        f"- Number of Key Concepts per Module: {NUMBER_OF_KEY_CONCEPTS}\n\n"

        f"## YOUR TASK\n"
        f"Using the above inputs, generate the complete, well-written and well-structured, module-by-module course content "
        f"(not just outlines or bullet points). For each module and each major chapter/session within it, provide:\n"
        f"1. Module Overview & Objectives\n"
        f"2. Lecture Narrative\n"
        f"3. Key Concept Definitions\n"
        f"4. Discussion Prompts\n"
        f"5. Micro-learning Objectives\n"
        f"6. Real-World Examples or Case Studies\n"
        f"7. Interactive Activities & Assessments\n"
        f"8. Recommended Readings & Resources\n"
        f"9. Transitions & Summary\n\n"
        f"At the end of the last module only, provide a course-wide summary, including 5 to 10 key takeaways and a final reflection prompt.\n\n"
        f"## STYLE & STRUCTURE GUIDELINES\n"
        f"- Use structured, detailed narrative format.\n"
        f"- Avoid bullet-only outlines unless defining concepts or exercises.\n"
        f"- Use clear formatting with headings, bold terms, and spacing.\n"
        f"- Assume students do not have a syllabus — your output must be self-contained and course-ready.\n"
        f"- Use a {TONE} tone and include suggested visuals, case names, micro-objectives, and examples where relevant.\n"
    )