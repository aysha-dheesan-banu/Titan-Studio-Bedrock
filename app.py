import streamlit as st
import boto3
import json
import base64
from PIL import Image
from io import BytesIO

# AWS Bedrock Client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# Page Configuration
st.set_page_config(page_title="Titan AI Studio", page_icon="🧠", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        h1 { color: #343a40; text-align: center; }
        h4 { color: #6c757d; text-align: center; font-weight: normal; }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 0.6rem;
        }
        .stButton>button {
            border-radius: 10px;
            background-color: #0d6efd;
            color: white;
            font-weight: bold;
            padding: 0.5em 1em;
            margin-top: 10px;
        }
        .stButton>button:hover {
            background-color: #0b5ed7;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🎨 Titan AI Studio</h1>", unsafe_allow_html=True)
st.markdown("<h4>Multi-Skill Smart Assistant Powered by Amazon Bedrock</h4>", unsafe_allow_html=True)
st.markdown("---")

# Model IDs
TITAN_TEXT_MODEL = "amazon.titan-text-express-v1"
TITAN_IMAGE_MODEL = "amazon.titan-image-generator-v1"

# Text Generator Helper
def generate_text(prompt, max_tokens=250):
    payload = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": max_tokens,
            "temperature": 0.7,
            "topP": 0.9
        }
    }
    response = bedrock.invoke_model(
        body=json.dumps(payload),
        modelId=TITAN_TEXT_MODEL,
        accept="application/json",
        contentType="application/json"
    )
    result = json.loads(response['body'].read())
    return result["results"][0]["outputText"]

# Image Generator
def generate_image(prompt):
    payload = {
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {"text": prompt},
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "quality": "standard",
            "height": 512,
            "width": 512,
            "cfgScale": 8.0,
            "seed": 42
        }
    }
    response = bedrock.invoke_model(
        body=json.dumps(payload),
        modelId=TITAN_IMAGE_MODEL,
        accept="application/json",
        contentType="application/json"
    )
    result = json.loads(response['body'].read())
    base64_img = result['images'][0]
    return Image.open(BytesIO(base64.b64decode(base64_img)))

# Code Summarization
def summarize_code(code):
    return generate_text(f"Summarize the following code:\n\n{code}", max_tokens=150)

# Chatbot
def chatbot_conversation(user_input):
    return generate_text(f"Answer the following or chat: {user_input}", max_tokens=150)

# Sidebar
st.sidebar.header("🛠️ AI Skills")
option = st.sidebar.radio("Choose an AI Feature:", [
    "Text Generation", "Summarization", "Question Answering", "Story Generation",
    "Email Generator", "Idea Generator", "Image Generation",
    "Image Variation", "Code Summarization", "Chatbot"
])

# Skill Modules
st.markdown(f"<h3 style='color:#495057;'>🧠 {option}</h3>", unsafe_allow_html=True)

if option == "Text Generation":
    prompt = st.text_area("🔤 Enter a creative prompt:")
    if st.button("🚀 Generate Text"):
        st.success(generate_text(prompt))

elif option == "Summarization":
    input_text = st.text_area("📄 Paste text to summarize:")
    if st.button("🧠 Summarize"):
        st.success(generate_text(f"Summarize this:\n\n{input_text}"))

elif option == "Question Answering":
    context = st.text_area("📘 Context:")
    question = st.text_input("❓ Your question:")
    if st.button("🎯 Get Answer"):
        st.success(generate_text(f"Context:\n{context}\n\nQ: {question}"))

elif option == "Story Generation":
    topic = st.text_input("📚 Enter your story idea:")
    if st.button("📝 Generate Story"):
        st.success(generate_text(f"Write a story about: {topic}", max_tokens=300))

elif option == "Email Generator":
    purpose = st.text_input("📧 Email purpose (e.g., leave request):")
    if st.button("✉️ Generate Email"):
        st.success(generate_text(f"Write a professional email for: {purpose}"))

elif option == "Idea Generator":
    niche = st.text_input("💡 Enter a domain (e.g., edtech):")
    if st.button("⚡ Get Ideas"):
        st.success(generate_text(f"Give 5 project ideas for: {niche}"))

elif option == "Image Generation":
    img_prompt = st.text_input("🖼️ Describe the image:")
    if st.button("🎨 Generate Image"):
        img = generate_image(img_prompt)
        st.image(img, caption="AI-Generated Image", use_container_width=True)

elif option == "Image Variation":
    uploaded_file = st.file_uploader("📤 Upload an image (jpg or png)", type=["jpg", "png"])
    var_prompt = st.text_input("✏️ Describe how to vary the image:",
                               placeholder="e.g., Add dreamy sunset colors and a foggy forest")
    if st.button("🔁 Generate Variation"):
        if uploaded_file and var_prompt:
            st.image(uploaded_file, caption="📷 Original Image", use_container_width=True)
            st.info("Generating variation based on your prompt...")
            new_img = generate_image(var_prompt)
            st.image(new_img, caption="🖼️ AI-Modified Image", use_container_width=True)
        else:
            st.warning("Please upload an image and enter a variation prompt.")

elif option == "Code Summarization":
    code_input = st.text_area("💻 Paste your code here:")
    if st.button("📄 Summarize Code"):
        st.success(summarize_code(code_input))

elif option == "Chatbot":
    user_input = st.text_input("💬 Talk to Titan:")
    if st.button("🤖 Respond"):
        st.success(chatbot_conversation(user_input))








