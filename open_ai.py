from openai import OpenAI
import tempfile

def call_gpt(api_key, user_input):
    client = OpenAI(api_key)

    uploaded_file = user_input['Example Course File']

    if uploaded_file is not None:
        # Save to a temporary local file
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded_file.name}") as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            temp_path = tmp_file.name

        # Open from disk and upload to OpenAI
        with open(temp_path, "rb") as f:
            openai_file = client.files.create(
                file=f,
                purpose="assistants"
            )
            file_id = openai_file.id
    else:
        file_id = None

    prompt = (
        f"Use the uploaded course file as a reference. "
        f"Now generate a beginner-friendly course titled '{user_input['Course Title']}' "
        f"targeted at {user_input['Target Audience']}, taught by {user_input['Instructor']}. "
        f"Include learning objectives like {user_input['Learning Objectives']} and cover key concepts such as {user_input['Key Concepts']}."
    )

    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_id": file_id,
                    },
                    {
                        "type": "input_text",
                        "text": prompt,
                    },
                ]
            }
        ]
    )
    print(response.output_text)
    return response.output_text