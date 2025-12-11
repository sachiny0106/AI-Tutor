# 🎓 AI Tutor - Your Personal Study Buddy

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-00B894.svg)](https://ollama.ai/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🔒 **100% Private** - An intelligent tutoring app that runs completely offline on your machine.

![AI Tutor Demo](/image.png)

---

## 🌟 Why AI Tutor?

Traditional online tutoring platforms send your data to external servers. **AI Tutor** is different:

- ✅ **Complete Privacy** - Your questions never leave your computer
- ✅ **No Subscriptions** - Free forever, no hidden costs
- ✅ **Works Offline** - Learn anywhere without internet
- ✅ **Customizable** - Choose your AI model and learning level

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| 📚 **Smart Explanations** | Get step-by-step breakdowns tailored to your education level |
| 🧪 **Quiz Generator** | Create custom MCQ quizzes on any topic instantly |
| 🎯 **Multi-Subject** | Math, Physics, Chemistry, Biology, History, CS |
| 🤖 **Model Flexibility** | Use Gemma3, Llama3, DeepSeek, or any Ollama model |
| 💬 **Chat Interface** | Natural conversation with context awareness |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed

### Quick Setup

```bash
# 1. Clone this repository
git clone https://github.com/sachiny0106/AI-Tutor.git
cd AI-Tutor

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Download an AI model (Gemma3 recommended)
ollama pull gemma3

# 4. Launch the app
streamlit run app.py
```

Open http://localhost:8501 in your browser and start learning! 🎉

---

## 📖 Usage Guide

### Step 1: Configure Preferences
Use the sidebar to set:
- **Education Level**: School → PG/PhD
- **Subject**: Choose from 6 subjects
- **Mode**: Explanation or Quiz

### Step 2: Start Learning
Type your question or topic in the chat box:

| Mode | Example Prompts |
|------|-----------------|
| Explain | "What is photosynthesis?" |
| Explain | "How do neural networks work?" |
| Quiz | "Test me on calculus derivatives" |
| Quiz | "Create a quiz about World War 2" |

---

## 🏗️ Project Structure

```
AI-Tutor/
├── app.py              # Main application (Streamlit)
├── requirements.txt    # Dependencies
├── config/
│   └── models.yaml     # Model preferences
├── docs/
│   ├── installation.md
│   ├── usage.md
│   └── troubleshooting.md
└── tests/
    └── test_app.py
```

---

## 🔧 Configuration

### Recommended Models

| Model | Best For | Command |
|-------|----------|---------|
| Gemma3 | General Education | `ollama pull gemma3` |
| DeepSeek Coder | Programming/CS | `ollama pull deepseek-coder` |
| Llama3 | Complex Topics | `ollama pull llama3` |

---

## 🐛 Common Issues

| Problem | Solution |
|---------|----------|
| "No models found" | Run `ollama serve` then `ollama pull gemma3` |
| Connection error | Check if Ollama is running on port 11434 |
| Slow responses | Try a smaller model like `gemma2:2b` |

See [troubleshooting guide](docs/troubleshooting.md) for more help.

---

## 🗺️ Roadmap

- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Progress tracking & analytics
- [ ] Export study notes as PDF
- [ ] Mobile-friendly PWA

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## 📬 Contact

- **GitHub**: [@sachiny0106](https://github.com/sachiny0106)
- **Issues**: [Report a bug](https://github.com/sachiny0106/AI-Tutor/issues)

---

<div align="center">
  <b>Built with ❤️ by Sachin Yadav</b>
  <br><br>
  ⭐ Star this repo if you find it useful!
</div>
