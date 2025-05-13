import streamlit as st
import requests

def generate_lessons(api_key, full_prompts, temperature):
    """Generate lessons based on the prompts provided."""
    if not api_key:
        st.error('Missing API key')
        return
    if not full_prompts:
        st.error('Missing prompt')
        return

    prompts = full_prompts.strip().split(";")

    for i, prompt in enumerate(prompts):
        prompt = prompt.strip()
        if not prompt:
            continue

        try:
            return call_google_ai(api_key, prompt, temperature)
        except Exception as e:
            st.error(str(e))
            return

def call_google_ai(api_key, prompt, temperature, top_p=1.0, max_tokens=1024, frequency_penalty=0.0, stop_sequences=None):
    """Send a request to the Google Gemini API to generate content.

    Parameters:
    - api_key (str): Your API key for Google Gemini.
    - prompt (str): The input prompt.
    - temperature (float): Controls randomness in output.
    - top_p (float): Controls nucleus sampling (top-p sampling).
    - max_tokens (int): Maximum number of tokens to generate.
    - frequency_penalty (float): Penalizes new tokens based on frequency.
    - stop_sequences (list): List of strings where the model will stop generating further tokens.
    """

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}

    generation_config = {
        "temperature": temperature,
        "topP": top_p,
        "maxOutputTokens": max_tokens,
        "frequencyPenalty": frequency_penalty
    }

    if stop_sequences:
        generation_config["stopSequences"] = stop_sequences

    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": generation_config
    }
    response = requests.post(url, headers=headers, params=params, json=body)

    if response.status_code != 200:
        print(f"Request failed: {response.status_code} - {response.text}")
        raise Exception(response.reason)

    try:
        response_json = response.json()
    except Exception:
        raise Exception(f"Invalid JSON response: {response.text}")

    try:
        generated_text = response_json['candidates'][0]['content']['parts'][0]['text']
        return generated_text
    except (KeyError, IndexError, TypeError) as e:
        raise Exception(f"Unexpected response structure: {response_json}")