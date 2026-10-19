<div align="center">

# Q-TIP

### Your TIP Assistant

An intent-classification chatbot that answers questions about enrollment, admissions, tuition, payment, programs, accreditation, and contact information at the Technological Institute of the Philippines (TIP).

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Intent%20Classifier-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scoring-013243?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Dataset-150458?style=for-the-badge&logo=pandas&logoColor=white)

![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Chat%20UI-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

</div>

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [1. Get the code](#1-get-the-code)
  - [2. Create the virtual environment](#2-create-the-virtual-environment)
  - [3. Activate the virtual environment](#3-activate-the-virtual-environment)
  - [4. Install the dependencies](#4-install-the-dependencies)
  - [5. Run Q-TIP](#5-run-q-tip)
  - [6. Open it in your browser](#6-open-it-in-your-browser)
  - [7. Stop the server](#7-stop-the-server)
- [Understanding the Virtual Environment](#understanding-the-virtual-environment)
- [Retraining the Model](#retraining-the-model)
- [Customizing Replies](#customizing-replies)
- [Terminal Test Mode](#terminal-test-mode)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Project Creators](#project-creators)

---

## About the Project

**Q-TIP** ("Your TIP Assistant") is a web-based chatbot that helps prospective and current students get quick, accurate answers about TIP. Instead of searching through multiple pages, a student can type a question (or tap a quick question button) and get an answer right away.

Q-TIP began as a desktop app and was rebuilt as a Flask web application. It appears as a floating **Q** button on the page, which opens a chat window styled in TIP's black and yellow colors.

## Features

- **Intent classification.** A trained machine learning model figures out what the student is asking and picks the matching verified reply.
- **Floating chat widget.** A launcher button opens and closes the chat window without leaving the page.
- **Quick question buttons.** One-tap shortcuts for *Enrollment*, *Contact Info*, and *Admission Requirements*.
- **Typing indicator and word-by-word replies** for a natural chat feel.
- **Clickable links.** URLs in replies are turned into links automatically.
- **Fallback handling.** Questions the model is not confident about get a helpful "try asking about..." reply instead of a wrong answer.
- **Responsive and accessible.** Works on small screens, respects reduced-motion settings, and supports keyboard use (Esc closes the window).

## How It Works

```
Student types a question
        |
        v
  script.js  --POST /api/chat-->  app.py (Flask)
                                     |
                                     v
                       Q-TIP_Intent_Classifier.joblib
                       (predicts the intent + confidence)
                                     |
                      below threshold? --> UNKNOWN reply
                                     |
                                     v
                       replies.py (verified reply text)
                                     |
        <------------ JSON reply ----+
        |
        v
 Reply shown in the chat window
```

1. The browser sends the message to the Flask backend at `/api/chat`.
2. The backend feeds the text to the trained classifier, which scores every known intent.
3. If the best score clears the confidence threshold, the matching reply from `replies.py` is returned. Otherwise a fallback reply is used.
4. The frontend displays the reply.

## Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python 3.10+ |
| Web framework | Flask |
| Machine learning | scikit-learn |
| Numerics / data | NumPy, pandas |
| Model storage | joblib |
| Frontend | HTML5, CSS3, vanilla JavaScript |
| Fonts | Archivo (Google Fonts) |

## Project Structure

```
Q-TIP/
├── static/
│   ├── img/
│   │   └── bg.png                       # Page background (TIP website mockup)
│   ├── script.js                        # Chat widget logic and quick questions
│   └── style.css                        # Black and yellow chat styling
├── index.html                           # Chat page (see note below)
├── app.py                               # Flask server: serves the page and /api/chat
├── training.py                          # Trains the intent classifier from the dataset
├── replies.py                           # Verified reply text for each intent
├── terminal_test.py                     # Text-only chat loop for quick testing
├── DATASET_QTIP.csv                     # Training data (example questions per intent)
├── Q-TIP_Intent_Classifier.joblib       # The trained model
├── requirements.txt                     # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

> **Note:** If your `index.html` lives in a `templates/` folder instead of the project root, adjust the tree above to match your repository.

---

## Getting Started

Follow these steps in order. They work the same on any computer; only the activation command in step 3 differs between Windows and macOS/Linux.

### Prerequisites

Make sure you have these installed before you begin:

| Tool | Version | Check with |
| --- | --- | --- |
| Python | 3.10 or newer | `python --version` |
| pip | Comes with Python | `pip --version` |
| Git (optional) | Any recent version | `git --version` |

> **Windows tip:** When installing Python, tick **"Add python.exe to PATH"** on the first installer screen. If `python` is not recognized later, this is almost always why.

### 1. Get the code

Clone the repository (or download it as a ZIP and extract it):

```bash
git clone <your-repository-url>
cd Q-TIP
```

Replace `<your-repository-url>` with the actual link to the repository.

### 2. Create the virtual environment

A virtual environment (`.venv`) is a private folder that holds this project's Python packages, so they do not clash with other projects on your computer. From inside the `Q-TIP` folder, run:

```bash
python -m venv .venv
```

This creates a `.venv` folder. You only need to do this **once per computer**.

### 3. Activate the virtual environment

You must activate the environment **every time you open a new terminal** to work on Q-TIP.

**Windows (PowerShell or the VS Code terminal):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```bat
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

When it works, your terminal prompt starts with `(.venv)`, like this:

```
(.venv) PS C:\Users\you\Q-TIP>
```

> **PowerShell says "running scripts is disabled"?** Run this once, then try activating again:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

### 4. Install the dependencies

With `(.venv)` showing in your prompt, install everything Q-TIP needs:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` yet, install the packages directly and then generate one:

```bash
pip install flask scikit-learn numpy pandas joblib requests
pip freeze > requirements.txt
```

> **Important:** The model file was trained with a specific scikit-learn version. If you see a warning or error about "InconsistentVersionWarning" when the app starts, either install the same scikit-learn version used for training or retrain the model (see [Retraining the Model](#retraining-the-model)).

### 5. Run Q-TIP

Still inside the activated environment, start the Flask server:

```bash
python app.py
```

You should see output similar to this:

```
Loading Q-TIP model...
Model loaded successfully!
 * Running on http://127.0.0.1:5000
```

Leave this terminal open. The server runs for as long as the window stays open.

### 6. Open it in your browser

Go to:

```
http://127.0.0.1:5000
```

(`http://localhost:5000` works too.) Click the yellow **Q** button in the bottom-right corner to open the chat, then type a question or tap one of the quick question buttons.

> If your terminal shows a different port, use that one instead.

### 7. Stop the server

Click the terminal running the server and press **Ctrl + C**. To leave the virtual environment, type:

```bash
deactivate
```

---

## Understanding the Virtual Environment

If environments and packages are new to you, here is the short version.

**What is `.venv`?**
It is a folder containing its own copy of Python plus only the packages Q-TIP needs (Flask, scikit-learn, and so on). When it is *activated*, the `python` and `pip` commands in your terminal use this private copy instead of the one installed system-wide.

**Why use one?**
- Different projects can use different package versions without breaking each other.
- Anyone who clones the repository can recreate the exact same setup.
- Your global Python stays clean.

**What is `requirements.txt`?**
A plain list of the packages (and versions) the project depends on. `pip install -r requirements.txt` reads that list and installs everything in one go. After adding a new package, update it with:

```bash
pip freeze > requirements.txt
```

**Why is `.venv` not in the repository?**
The folder is large and specific to each computer, so it is listed in `.gitignore` and is never uploaded. Each person creates their own with steps 2 to 4 above. If `.venv/` is missing from your `.gitignore`, add the line:

```
.venv/
```

**"Environment variables"?**
Q-TIP does not require any. Everything runs with the defaults. (If you later add secrets such as API keys, store them in a `.env` file, add it to `.gitignore`, and never commit it.)

**Common mistake:** installing packages or running `python app.py` *without* `(.venv)` active. If you get `ModuleNotFoundError: No module named 'flask'`, your environment is not activated, so go back to step 3.

## Retraining the Model

The classifier learns from `DATASET_QTIP.csv`. After adding or editing example questions, retrain it:

```bash
python training.py
```

This regenerates `Q-TIP_Intent_Classifier.joblib`. Restart `python app.py` afterward so the server loads the new model.

Tips for better accuracy:
- Add several differently phrased examples for each intent, including Filipino and Taglish phrasing.
- Keep the intent labels in the dataset identical to the keys in `replies.py`.

## Customizing Replies

All reply text lives in `replies.py` inside the `INTENT_RESPONSES` dictionary. Each key is an intent label from the dataset, and each value is the message shown to the student. To add a new topic:

1. Add example questions with a new intent label in `DATASET_QTIP.csv`.
2. Add a matching entry in `INTENT_RESPONSES` in `replies.py`.
3. Run `python training.py` to retrain.
4. Restart `python app.py`.

The three quick question buttons are defined in `index.html` using `data-question` attributes. Edit those to change what each button asks.

## Terminal Test Mode

To test the classifier without the browser, run:

```bash
python terminal_test.py
```

Type a question and it prints the detected intent and reply. Type `exit` to quit.

## Troubleshooting

| Problem | Likely cause and fix |
| --- | --- |
| `python` is not recognized | Python is not on your PATH. Reinstall it and tick "Add to PATH", or try `py` instead of `python` on Windows. |
| `ModuleNotFoundError: No module named 'flask'` | The virtual environment is not activated, or dependencies are not installed. Redo steps 3 and 4. |
| PowerShell blocks `Activate.ps1` | Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, then activate again. |
| `Address already in use` / port 5000 busy | Another program is using the port. Close it, or change the port in the `app.run(...)` line of `app.py`. |
| Page loads but the background image is missing | Check that `static/img/bg.png` exists and that the CSS path is `url("img/bg.png")`. Hard refresh with **Ctrl + Shift + R**. |
| Changes to CSS or JS do not show up | The browser cached the old file. Hard refresh with **Ctrl + Shift + R**. |
| Chat says "I couldn't reach the server" | The Flask server is not running. Start it with `python app.py`. |
| Replies always say "I can't quite understand" | The question is outside the trained intents or below the confidence threshold. Add examples to the dataset and retrain. |
| Version warning when loading the model | scikit-learn version differs from the one used to train. Retrain with `python training.py`. |

## License

This project is distributed under the terms of the license in the [LICENSE](LICENSE) file.

---

## Project Creators

<div align="center">

![Lance Chester V. Bolito](https://img.shields.io/badge/Bolito%2C%20Lance%20Chester%20V.-FFC20E?style=for-the-badge&logo=github&logoColor=black)
![Ross Andrew Bulaong](https://img.shields.io/badge/Bulaong%2C%20Ross%20Andrew-FFC20E?style=for-the-badge&logo=github&logoColor=black)
![Serge V. Esguerra](https://img.shields.io/badge/Esguerra%2C%20Serge%20V.-FFC20E?style=for-the-badge&logo=github&logoColor=black)
![Sean Bryan V. Ingles](https://img.shields.io/badge/Ingles%2C%20Sean%20Bryan%20V.-FFC20E?style=for-the-badge&logo=github&logoColor=black)

</div>
