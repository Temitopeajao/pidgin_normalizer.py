# 🧹 Pidgin Text Normalizer  
## Data Cleaning & Standardization for Nigerian Pidgin NLP

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![NLP](https://img.shields.io/badge/Focus-NLP-orange)
![Regex](https://img.shields.io/badge/Technique-Regex-yellow)
![Domain](https://img.shields.io/badge/Domain-African%20Languages-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

> A lightweight preprocessing pipeline that cleans and normalizes noisy Nigerian Pidgin text for LLM training.

---

## 📋 Overview

The **Pidgin Normalizer** is a specialized text preprocessing tool designed to standardize **Nigerian Pidgin (Naija)** before it enters NLP or LLM training pipelines.

Crowdsourced and low-resource language datasets often contain:

- SMS shorthand  
- Inconsistent spelling  
- Slang variations  
- Noise artifacts  
- Mixed orthography  

These inconsistencies significantly reduce model performance.

This project applies **regex-based normalization rules** to produce **clean, consistent, model-ready text**.

---

## ✨ Features

### 🔤 Shorthand Expansion
Converts SMS slang into standard forms:

```
u   → you
d   → the
abt → about
```

### 🧼 Noise Removal
- Extra spaces
- Tabs
- Special characters
- Non-alphanumeric artifacts

### 🪶 Diacritic Stripping
Ensures ASCII compatibility for training stability.

### 📏 Standardization
Enforces consistent spelling for common tokens:

- wetin  
- dey  
- abi  
- sha  
- na  

### ⚡ Lightweight & Fast
Pure Python + Regex → zero heavy dependencies.

---

## 🛠️ Why This Matters

### The Problem
Low-resource language data is messy.

Messy data → confused models → worse outputs.

### The Fix
Clean inputs → better tokenization → stronger training → better translations.

### The Result
✔ Higher quality datasets  
✔ Reduced hallucination  
✔ More consistent embeddings  
✔ Better downstream performance  

---

## 🧱 Architecture

```
Raw Text
   │
   ▼
Regex Cleaning
   │
   ├── Shorthand expansion
   ├── Noise removal
   ├── Spelling normalization
   └── Whitespace cleanup
   ▼
Normalized Text
   │
   ▼
LLM / NLP Pipeline
```

---

## ⚙️ Installation

### Clone repository

```bash
git clone https://github.com/yourusername/pidgin-normalizer.git
cd pidgin-normalizer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run demo script

```bash
python normalizer.py
```

### Python example

```python
from normalizer import normalize_text

text = "how u dey 2day?? abeg reply me"
clean = normalize_text(text)

print(clean)
```

### Output

```
how you dey today abeg reply me
```

---

## 🧪 Example Use Cases

- LLM pretraining
- Fine-tuning datasets
- Translation systems
- Speech-to-text cleanup
- Chatbot preprocessing
- African NLP research

---

## 🧰 Built With

- Python
- Regular Expressions (Regex)
- Text preprocessing techniques
- NLP data cleaning practices

---

## 📂 Project Structure

```
pidgin-normalizer/
│
├── normalizer.py      # Core cleaning logic
├── rules.py           # Regex rules
├── data/              # Sample raw texts
├── tests/             # Unit tests
├── requirements.txt
└── README.md
```

---


## 🔬 Roadmap

- [ ] Batch file processing
- [ ] CLI tool
- [ ] HuggingFace dataset integration
- [ ] Yoruba/Hausa/Igbo normalization
- [ ] Web demo
- [ ] Benchmark metrics

---

## 🤝 Contributing

Pull requests and suggestions are welcome.

You can contribute:
- More normalization rules
- Slang dictionaries
- Additional languages
- Performance optimizations

---

## 👤 Author

**Temitope Ajao**  
AI Engineer & LLM Specialist  

[LinkedIn](www.linkedin.com/in/temitope-ajao-4a8670302) • [Email](mailto:topekele@gmail.com)

---

## 📜 License

MIT License

---

## ⭐ If this project helps you
Give it a star — it supports African NLP research ✨
