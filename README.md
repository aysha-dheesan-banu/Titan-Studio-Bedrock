🎨 Titan AI Studio
Titan AI Studio is a multi-skill smart assistant powered by Amazon Bedrock, offering a wide range of AI capabilities—from text and image generation to code summarization and chatbot interaction—through a user-friendly Streamlit interface.

#Models I used for this project from bedrock
Model IDs
TITAN_TEXT_MODEL = "amazon.titan-text-express-v1"
TITAN_IMAGE_MODEL = "amazon.titan-image-generator-v1"

🚀 Features
✍️ Text Generation – Generate creative text using Titan models.

📄 Summarization – Summarize long text or documents.

❓ Question Answering – Ask questions based on custom context.

📚 Story Generator – Create stories from prompts.

📧 Email Generator – Get professional emails based on the situation.

💡 Idea Generator – Receive innovative project ideas.

🖼️ Image Generation – Generate images using descriptive prompts.

🧙‍♂️ Image Variation – Upload an image and modify it with AI.

💻 Code Summarization – Get simple summaries of code snippets.

🤖 Chatbot – Talk to a smart AI assistant.

🛠️ Tech Stack
Streamlit

Amazon Bedrock – Titan Text & Image Models

Boto3

Python libraries: json, PIL, base64, io

⚙️ Setup Instructions
Download teh zip file from github

Install Dependencies
pip install -r requirements.txt
Configure AWS Credentials

Ensure your AWS credentials (with access to Bedrock) are set up:
aws configure
Or, use environment variables:
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1

Run the App
streamlit run app.py
