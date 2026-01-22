import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_email_response(email_content, tone="formal"):
    prompt = f"Generate a {tone} email response to the following email:\n\n{email_content}\n\nEnsure the response is polite, clear and professional."
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error generating response"

#Gradio Interface
interface = gr.Interface(
    fn = generate_email_response,
    inputs=[
        gr.Textbox(lines=5, placeholder="Paste the email content here...", label="Email Content"),
        gr.Radio("Formal", ["formal", "informal"], label="Response Tone")
    ],
    outputs=gr.Textbox(lines=10, label="Generated Email Response"),
    title="Automated Email Responder",
    description="Generate polite and professional email responses using AI. Paste the email content and select the desired tone."
)

#Launch the Gradio app
if __name__ == "__main__":
    interface.launch()

# # Test AI response generation
# if __name__ == "__main__":
#     test_email = """\
#     Subject: Meeting Request

#     Hi,

#     I hope this email finds you well. I would like to schedule a meeting to discuss our upcoming project. Please let me know your availability.

#     Best regards,
#     John Doe
#     """
    
#     print(generate_email_response(test_email, tone="formal"))