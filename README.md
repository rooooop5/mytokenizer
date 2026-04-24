### Project overview
This project implements a simple byte-pair encoding (BPE) tokenizer in Python.

- bpe_preprocessing.py: builds BPE merge rules from a dataset, then saves:
  - merge_rules.pkl
  - rev_merge_rules.pkl
- tokenizer_class.py: defines a `Tokenizer` class that loads the saved rules and performs:
  - `encode(text)` → token id sequence
  - `decode(ids)` → reconstructed string
- __init__.py: empty package initializer

---

### Files

- __init__.py
- bpe_preprocessing.py
- merge_rules.pkl
- rev_merge_rules.pkl
- tokenizer_class.py

---

### Usage

1. Generate merge rules
   - Provide `dataset.txt` in the same directory
   - Run bpe_preprocessing.py
   - This creates merge_rules.pkl and rev_merge_rules.pkl

2. Use the tokenizer
```python
from tokenizer.tokenizer_class import Tokenizer

tokenizer = Tokenizer(dir_path="tokenizer")
ids = tokenizer.encode("hello world")
text = tokenizer.decode(ids)
print(ids)
print(text)
```

---
