# AI Chatbot with Web-Scraped Data

A simple AI-powered chatbot that scrapes content from a website, stores it as structured data, and answers user questions using retrieval-augmented generation (RAG) powered by the Groq API.

## 🚀 Features
- Scrapes text content from a live webpage
- Stores scraped data in JSON format
- Uses sentence embeddings to find relevant context for any question
- Generates natural language answers using Groq's LLaMA model
- Runs entirely from the command line

## 🛠️ Tech Stack
- **Python 3**
- **BeautifulSoup4** – web scraping
- **Sentence-Transformers** – text embeddings
- **Scikit-learn** – similarity search
- **Groq API** – LLM-powered responses (LLaMA 3.1)

## 📂 Project Structure
## ⚙️ Setup Instructions

1. Clone this repository:
```bash
git clone https://github.com/HAROON0N05/ai-chatbot.git
cd ai-chatbot
```

2. Install dependencies:
```bash
pip install requests beautifulsoup4 sentence-transformers scikit-learn groq
```

3. Get a free API key from [Groq Console](https://console.groq.com) and set it as an environment variable:
```bash
setx GROQ_API_KEY "your_api_key_here"
```

4. Run the scraper to collect data:
```bash
python scraper.py
```

5. Run the chatbot:
```bash
python chatbot.py
```

## 💬 Example Usage
Ask: What is artificial intelligence?

Artificial intelligence is the simulation of human intelligence processes by machines..
## 📌 Notes
- The scraper currently targets a Wikipedia article as a data source (can be modified for any website).
- API key is loaded securely via environment variables, never hardcoded.

## 👤 Author
Haroon — BS Artificial Intelligence Student, PAF-IAST