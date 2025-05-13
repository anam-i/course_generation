import streamlit as st

# List of all the course topics from the table
COURSE_TOPICS = [
    "Management of Food and Beverage Operations",
    "Managing Front Office Operations",
    "Managing Housekeeping Operations",
    "Managing Beverage Service",
    "Managing Hospitality Human Resources",
    "Hospitality Facilities Management and Design",
    "Revenue Management",
    "Security and Loss Prevention Management",
    "Hospitality Sales and Marketing",
    "Convention Management and Service",
    "Basic Hotel and Restaurant Accounting",
    "Introduction to Travel and Tourism: An International Approach",
    "Supervision in the Hospitality Industry",
    "Managing Technology in the Hospitality Industry",
    "Service Excellence",
    "Hospitality Today"
]

# Course Codes
COURSE_CODES = [
    "HOSP 241", "HOSP 333", "HOSP 338", "HOSP 323", "HOSP 357", "HOSP 281", 
    "HOSP 374", "HOSP 387", "HOSP 472", "HOSP 378", "HOSP 261", "HOSP 101", 
    "HOSP 250", "HOSP 468", "HOSP 299", "HOSP 103"
]

# Career Occupation list
CAREER_OCCUPATIONS = [
    "Rooms Division: Front Desk Agent", "Reservation Agent", "Night Auditor", "Switch Board Operator", "Bell Person", 
    "Concierge", "Room Attendant", "Laundry Attendant", "House Person", "Room Service Attendant", "Restaurant/Bar/Lounge Server",
    "Banquets’ Server", "Sales/Marketing Coordinator", "Catering/Banquets Coordinator"
]

# Target Audience options
TARGET_AUDIENCE_OPTIONS = [
    "Undergraduate students", "Professionals", "Career changers", "Aspiring hospitality managers", "Tourism enthusiasts", "Executives", "Interns", "None"
]

EXPERTISE_LEVEL_OPTIONS = [
    "Beginner", "Intermediate", "Advanced", "None"
]

# Tone options
TONE_OPTIONS = [
    "Formal", "Informal", "Friendly", "Conversational", "Beginner-friendly", "Technical", "None"
]

# Input form for course details
def get_user_input():
    st.sidebar.header("Course Configuration")       

    # Course title topic selection
    course_title = st.sidebar.selectbox("Course Title & Topic", ["None"] + COURSE_TOPICS, placeholder='Enter the course title', help="The full title of the course")
    subject_domain = st.sidebar.text_input("Subject Domain", placeholder='Enter the subject domain', help="The academic or professional discipline the course belongs to")
    instructor = st.sidebar.text_input("Instructor", placeholder="Enter the instructor's name", help="Provide the instructor's name (optional)")
    course_code = st.sidebar.selectbox("Course Code", ["None"] + COURSE_CODES, help="Select a unique course code")
    number_of_modules = st.sidebar.number_input("How many modules", min_value=1, max_value=200, value=20, help="Total number of modules the course will contain")
    hours = st.sidebar.number_input("How many hours", min_value=1, max_value=200, value=20, help="Total instructional hours across the course")
    hours_per_module = st.sidebar.number_input("How many hours per module", min_value=1, max_value=200, value=20, help="Number of hours allocated to each module")
    duration = st.sidebar.text_input("Duration", placeholder='Enter the duration', help="Select the course duration")
    delivery_mode = st.sidebar.text_input("Delivery Mode", placeholder='Enter the delivery mode', help="Select how the course will be delivered (default is Online)")
    course_description = st.sidebar.text_area("Course Description", placeholder="Provide a brief course description", help="Write a brief overview of the course")
    industry_certifications = st.sidebar.text_area("Industry-Specific Certifications", placeholder="List any relevant industry certifications", help="Include certifications or codes related to the industry")
    career_occupation = st.sidebar.selectbox("Career Occupation", ["None"] + CAREER_OCCUPATIONS, help="Select career occupations associated with this course")
    
    learning_objectives = st.sidebar.text_area("Learning Objectives", placeholder="Enter clear learning objectives", help="Specific knowledge, skills, and abilities learners will gain.")
    number_of_key_concepts = st.sidebar.number_input("Key Concepts", min_value=1, max_value=200, value=20, help="Total number of key concepts in each module.")
    
    assessments = st.sidebar.text_area("Activities & Assessments", placeholder="Describe the activities and assessments", help="Mention methods of evaluation like essays, projects, exams, etc.")
    
    prerequisites = st.sidebar.text_area("Prerequisites", placeholder="Mention any prerequisites for this course", help="Indicate any prior knowledge or courses needed")
    co_requisites = st.sidebar.text_area("Co-requisites (optional)", placeholder="Mention any co-requisites", help="List any courses to be taken alongside this one (optional)")
    
    course_outline = st.sidebar.text_area("Course Outline", placeholder="Provide the course outline", help="Provide the course outline with modules and subtopics")
    
    target_audience = st.sidebar.selectbox("Target Audience", ["None"] + TARGET_AUDIENCE_OPTIONS, help="Description of the target audience")
    expertise_level = st.sidebar.selectbox("Expertise Level", ["None"] + EXPERTISE_LEVEL_OPTIONS, help="Intended learner level?")
    tone = st.sidebar.selectbox("Tone & Style", ["None"] + TONE_OPTIONS, placeholder='Enter the tone of delivery', help="Select the tone of delivery (formal, informal, etc.)")
    
    preferred_content_format = st.sidebar.text_input('Preferred content format', placeholder='Enter the preferred content format', help="Teaching strategies used to deliver content (e.g., lectures, simulations, case studies).")
    
    student_engagement_methods = st.sidebar.text_input("Student Engagement Methods", placeholder='Enter the student engagement method', help="Select methods for engaging students in the course")
    
    instructor_guest_speaker = st.sidebar.text_area("Guest Speaker", placeholder="Enter name of guest speakers or industry experts", help="Mention any special guest speakers or notable instructors")
    references = st.sidebar.text_area("References & Examples", placeholder="Provide references or case studies", help="List any case studies, research papers, or reference materials")
    
    example_course_file = st.sidebar.file_uploader("Example Course File", type=["pdf", "docx", "pptx", "txt"], help="Upload a sample course or guide document (optional)")

    notes = st.sidebar.text_area("Notes/Additional Information", placeholder="Include any additional information or notes", help="Add any extra details that should be included in the course")

    return {
        "Course Title": course_title,
        "Subject Domain": subject_domain,
        "Instructor": instructor,
        "Course Code": course_code,
        "Hours": hours,
        "Number of Modules": number_of_modules,
        "Hours per Module": hours_per_module,
        "Duration": duration,
        "Delivery Mode": delivery_mode,
        "Course Description": course_description,
        "Industry Certifications": industry_certifications,
        "Career Occupation": career_occupation,
        "Learning Objectives": learning_objectives,
        "Key Concepts": number_of_key_concepts,
        "Assessments": assessments,
        "Prerequisites": prerequisites,
        "Co-requisites": co_requisites,
        "Course Outline": course_outline,
        "Target Audience": target_audience,
        "Expertise Level": expertise_level,
        "Tone": tone,
        "Preferred Content Format": preferred_content_format,
        "Student Engagement Methods": student_engagement_methods,
        "Guest Speaker": instructor_guest_speaker,
        "References": references,
        "Example Course File": example_course_file,
        "Notes": notes
    }

# Function to display the entered course details
def display_course(course):
    st.markdown(f"**Course Title:** {course['Course Title']}")
    st.markdown(f"**Course Code:** {course['Course Code']}")
    st.markdown(f"**Instructor:** {course['Instructor']}")
    st.markdown(f"**Duration:** {course['Duration']}")
    st.markdown(f"**Delivery Mode:** {course['Delivery Mode']}")
    st.markdown(f"**Hours:** {course['Hours']} hours")

    # st.subheader("🔵 Course Description")
    # st.write(course["Course Description"])

    # st.subheader("🔵 Industry-Specific Certifications")
    # st.write(course["Industry Certifications"])

    # st.subheader("🔵 Career Occupation")
    # st.write(course["Career Occupation"]);

    # st.subheader("🔵 Learning Objectives")
    # st.write(course["Learning Objectives"])

    # st.subheader("🔵 Key Concepts")
    # st.write(course["Key Concepts"])

    # st.subheader("🔵 Assessments")
    # st.write(course["Assessments"])

    # st.subheader("🔵 Prerequisites")
    # st.write(course["Prerequisites"])

    # st.subheader("🔵 Co-requisites")
    # st.write(course["Co-requisites"])

    # st.subheader("🔵 Course Outline")
    # st.write(course["Course Outline"])

    # st.subheader("🔵 Target Audience")
    # st.write(course["Target Audience"])

    # st.subheader("🔵 Tone & Style")
    # st.write(course["Tone"])

    # st.subheader("🔵 Preferred Content Format")
    # st.write(", ".join(course["Preferred Content Format"]) if course["Preferred Content Format"] and "None" not in course["Preferred Content Format"] else "N/A")

    # st.subheader("🔵 Student Engagement Methods")
    # st.write(", ".join(course["Student Engagement Methods"]) if course["Student Engagement Methods"] and "None" not in course["Student Engagement Methods"] else "N/A")

    # st.subheader("🔵Guest Speaker")
    # st.write(course["Guest Speaker"])

    # st.subheader("🔵References & Examples")
    # st.write(course["References"])

    # if course["Example Course File"]:
    #     st.subheader("🔵 Example Course File")
    #     st.download_button("Download Example Course File", course["Example Course File"])

    # st.subheader("🔵 Notes / Additional Information")
    # st.write(course["Notes"])
