# Biometric Authentication using Fingerprint Hashing

## 🔍 Overview
This project demonstrates a secure authentication system using fingerprint hashing.
Instead of storing raw fingerprint images, the system stores a SHA-256 hash derived
from processed fingerprint data.

## ⚙️ Features
- Fingerprint preprocessing using OpenCV
- SHA-256 hashing for template security
- Simple command-line register & login system
- JSON-based user storage

## 🧠 Tech Stack
Python, OpenCV, Numpy, Hashlib

## ▶️ Run
```bash
pip install -r requirements.txt
python app.py
```

## 📁 Structure
- `app.py`: main logic
- `fingerprint_utils.py`: preprocessing & hashing
- `users.json`: stores user hash values

## 👨‍💻 Author
Created by **Mangalesh P**
