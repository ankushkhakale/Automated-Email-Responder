# Automated Email Responder

An intelligent, AI-powered email response generator that helps you craft professional email replies in seconds. Built with modern Python frameworks and powered by the DeepSeek-R1 language model through Ollama, this tool streamlines your email workflow by generating context-aware, polite, and professional responses tailored to your preferred tone.

## 🌟 Overview

In today's fast-paced digital world, responding to emails quickly and professionally is crucial but time-consuming. **Automated Email Responder** solves this challenge by leveraging artificial intelligence to generate thoughtful email responses automatically. Whether you need a formal business reply or a casual friendly response, this tool has you covered.

The project offers two distinct implementations:
- **Gradio Interface** ([email responder.py](email responder.py)) - An intuitive web-based UI for interactive use
- **FastAPI Backend** ([app.py](app.py)) - A RESTful API service for integration with other applications

## ✨ Features

- **AI-Powered Generation**: Utilizes DeepSeek-R1 model via Ollama for intelligent, context-aware responses
- **Tone Customization**: Choose between formal and informal tones to match your communication style
- **Dual Interface Options**:
  - **Interactive Web UI**: User-friendly Gradio interface for direct interaction
  - **REST API**: FastAPI endpoint for programmatic access and integration
- **Real-time Processing**: Generate responses instantly without streaming delays
- **Professional Quality**: Ensures all responses are polite, clear, and professionally structured
- **Easy to Deploy**: Simple setup with minimal dependencies

## 🛠️ Technology Stack

- **Python 3.8+**: Core programming language
- **Gradio**: Modern web interface framework for the UI version
- **FastAPI**: High-performance web framework for the API version
- **Ollama**: Local LLM runtime for AI model inference
- **DeepSeek-R1**: Advanced language model for generating responses
- **Requests**: HTTP library for Ollama API communication

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.8 or higher**
   ```bash
   python --version
   ```

2. **Ollama** with DeepSeek-R1 model
   - Download and install Ollama from [ollama.ai](https://ollama.ai)
   - Pull the DeepSeek-R1 model:
   ```bash
   ollama pull deepseek-r1
   ```

3. **Verify Ollama is running**:
   ```bash
   ollama serve
   ```
   The service should be accessible at `http://localhost:11434`

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ankushkhakale/Automated-Email-Responder.git
   cd Automated-Email-Responder
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install gradio requests fastapi uvicorn
   ```

## 💻 Usage

### Option 1: Gradio Web Interface

The Gradio interface provides an intuitive, browser-based UI perfect for direct user interaction.

**Launch the application**:
```bash
python "email responder.py"
```

**Access the interface**: Open your browser and navigate to the local URL displayed in the terminal (typically `http://127.0.0.1:7860`)

**How to use**:
1. Paste the email you want to respond to in the "Email Content" text box
2. Select your preferred response tone (Formal or Informal)
3. Click "Submit" to generate the response
4. Copy the generated response from the output box

### Option 2: FastAPI REST API

The FastAPI version offers a programmatic interface ideal for integrating with other applications or services.

**Start the API server**:
```bash
uvicorn app:app --reload
```

## 📝 Example Use Case

**Input Email**:
```
Subject: Meeting Request

Hi,

I hope this email finds you well. I would like to schedule a meeting 
to discuss our upcoming project. Please let me know your availability.

Best regards,
John Doe
```

**Generated Response** (Formal Tone):
```
Subject: Re: Meeting Request

Dear John,

Thank you for reaching out. I appreciate your interest in discussing 
the upcoming project.

I would be happy to schedule a meeting with you. I am available next 
Tuesday and Thursday afternoon, or Wednesday morning. Please let me 
know which time works best for you, and I will send a calendar invite.

I look forward to our discussion.

Best regards
```

## 🏗️ Project Structure

```
Automated-Email-Responder/
├── app.py                 # FastAPI REST API implementation
├── email responder.py     # Gradio web interface implementation
└── README.md             # Project documentation
```

**Ideas for contributions**:
- Add support for multiple languages
- Implement email template libraries
- Add more tone options (e.g., enthusiastic, empathetic, concise)
- Create batch processing capabilities
- Add email classification features
- Implement user preference saving

## 🙏 Acknowledgments

- **Ollama Team** - For providing an excellent local LLM runtime
- **DeepSeek** - For the powerful DeepSeek-R1 language model
- **Gradio** - For the intuitive interface framework
- **FastAPI** - For the modern, fast web framework

## 📚 Future Enhancements

- [ ] Add support for email thread context awareness
- [ ] Implement sentiment analysis for incoming emails
- [ ] Create custom tone presets and user-defined styles
- [ ] Add email signature templates
- [ ] Implement multi-language support
- [ ] Create browser extension for Gmail/Outlook integration
- [ ] Add response quality rating system
- [ ] Implement email categorization and auto-routing

---

**Made with ❤️ by Ankush Khakale** | [Report Bug](https://github.com/ankushkhakale/Automated-Email-Responder/issues) | [Request Feature](https://github.com/ankushkhakale/Automated-Email-Responder/issues)