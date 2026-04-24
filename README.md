# 🧩 BPE Tokenizer

A minimal implementation of a **Byte Pair Encoding (BPE) tokenizer** built from scratch in Python — no external NLP libraries required. This project is designed to be simple, transparent, and educational, while remaining practically usable.

---

## 🚀 Overview

BPE tokenization works in two stages:

**1. Training / Preprocessing**
- Learns merge rules from a raw text dataset
- Serializes them to disk for reuse across sessions

**2. Encoding / Decoding**
- Converts raw text → token IDs
- Converts token IDs → original text

---

## 📁 Project Structure

```
tokenizer/
│
├── __init__.py
├── bpe_preprocessing.py     # Builds merge rules from dataset
├── tokenizer_class.py       # Tokenizer implementation
├── merge_rules.pkl          # Saved merge rules (generated)
└── rev_merge_rules.pkl      # Reverse mapping for decoding (generated)
```

---

## ⚙️ How It Works

1. **Initialization** — The corpus is split into individual characters as base tokens.
2. **Pair Counting** — The frequency of every adjacent token pair is counted across the corpus.
3. **Merging** — The most frequent pair is merged into a new token. This step repeats for a set number of iterations (vocabulary size).
4. **Rule Storage** — All merge rules and their reverse mappings are saved to `.pkl` files.
5. **Encoding** — New text is tokenized by applying the learned merge rules greedily, left to right.
6. **Decoding** — Token IDs are reversed back to text using the stored reverse mappings.

---

## 🏗️ Setup & Usage

### Prerequisites

- Python 3.7+
- No external NLP libraries needed

### 1. Prepare Your Dataset

Place a plain text file named `dataset.txt` in the project root directory. This file is used to learn merge rules.

### 2. Generate Merge Rules

```bash
python bpe_preprocessing.py
```

This will produce two files inside the `tokenizer/` directory:
- `merge_rules.pkl` — ordered list of merge operations
- `rev_merge_rules.pkl` — reverse mapping used during decoding

### 3. Use the Tokenizer

```python
from tokenizer.tokenizer_class import Tokenizer

tokenizer = Tokenizer(dir_path="tokenizer")

ids   = tokenizer.encode("hello world")
text  = tokenizer.decode(ids)

print(ids)    # e.g. [31, 57, 22, ...]
print(text)   # "hello world"
```

---

## 📌 Notes

- The tokenizer is **deterministic** — encoding and decoding are fully reversible.
- Vocabulary size is controlled by the number of merge iterations in `bpe_preprocessing.py`.
- The `.pkl` files are regenerated each time preprocessing is run; delete them to retrain from scratch.
- This was project was learnt from Andrej Karpathy's Tokenizer video on youtube.
---

## 📄 License

MIT — free to use, modify, and distribute.