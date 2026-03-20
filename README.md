# Tutur Tata Kata 📖
_A cozy, minimalist Indonesian dictionary web application designed for a focused reading room experience._
<img width="1630" height="902" alt="image" src="https://github.com/user-attachments/assets/a59f2aa6-65b4-4835-9570-f39ff283f37e" />

**Tutur Tata Kata** (Indonesian for "The Speech of Word Arrangement") is a pet project built to practice website development from scratch. This project allows users to explore the richness of the Indonesian language through random word generation, definitions, and an interactive synonym explorer.

## ✨ Features
- Word Search: Look up any Indonesian word and get its many, many definition.
- Random Word Generator: Discover new vocabulary with a single click—perfect for writers and language enthusiasts.
- Synonym Explorer: View a curated list of related words and synonyms.
- Fetch On-Demand (AJAX): To save API resources and improve performance, definitions for synonyms are fetched only when the user explicitly requests them.
- Post-Redirect-Get (PRG) Pattern: A robust backend flow that prevents "Form Resubmission" errors and allows for shareable search URLs.

## 🛠️ Tech Stack
- Backend: Flask (Python)
- Frontend: Tailwind CSS (Utility-first styling)
- Templating: Jinja2
- API Integration: Requests (Connecting to the Kateglo API)
- Interactivity: Vanilla JavaScript (Fetch API & Async/Await)

## 🏛️ Why the Design
- The UI is inspired by a vintage reading room.
- Warm Palette: Utilizing amber and stone hues to reduce eye strain.
- Classic Typography: A mix of Serif titles for elegance and clean Sans-Serif for readability.
- Centered Focus: All content is centered to provide a balanced, distraction-free environment.

## 🚀 Getting Started
**Prerequisites**
- Python 3.x
- pip (Python package manager)

**Installation**
1. Clone the repository:
```
git clone https://github.com/yourusername/tutur-tata-kata.git
cd tutur-tata-kata
```
2. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```
pip install flask requests
```
4. Run the application:
```
python app.py
```
5. Open http://127.0.0.1:5000 in your browser.

## 🧠 What I Learned
This project was a more or less 10-hour challenge focused on:
- State Management: Handling URL parameters (request.args) vs form data (request.form).
- Asynchronous JS: Managing Promises and using async/await to handle external API latency.
- DOM Manipulation: Dynamically updating parts of a page without a full refresh.
- Clean Code: Structuring a Flask app for scalability and readability.

## 📝 Credits
- Data provided by [Kateglo API](https://kateglo.lostfocus.org).
- Built as a coding exercise on making pet projects
