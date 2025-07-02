# 🤖 DSA Genie – Turn Problem Statements into Optimized Code

Welcome to **DSA Genie**, an AI-powered web app that converts Data Structures & Algorithms (DSA) problem statements into clean, testable, and optimized Python code using a multi-agent architecture (AutoGen + Docker).

---

## 📺 Demo Video

👉 ![Video] (https://streamable.com/7umfjj)

---

## 📸 Screenshots

_Add your screenshots below to showcase the UI and results._

![HomePage]<img width="955" alt="image" src="https://github.com/user-attachments/assets/23954d9c-6460-461e-b6e2-35057b9c5287" />

![Generated Code]<img width="940" alt="image" src="https://github.com/user-attachments/assets/85edabb4-9461-47a7-884c-b412bfe46a9b" />


---

## 🚀 Features

- 🧠 Converts natural language problem statements into optimized Python code.
- 👨🏻‍💻 Uses a multi-agent setup with AutoGen (DSAProblemSolverAgent & CodeExecutorAgent).
- 🐳 Docker container support for isolated execution.
- 📄 Automatically saves output to `solution.py` and allows downloading.
- 📦 Test cases included in each solution.
- 🎨 Polished Streamlit UI with avatars and chat interface.

---

## 🧰 Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [AutoGen by Microsoft](https://github.com/microsoft/autogen)
- Docker (via `docker_utils`)
- asyncio (for async message streaming)

---

## 📂 Folder Structure

```
📁 AiInterviewAgent/
├── .aivenv/                   # Python virtual environment (created locally)
├── DSA_Genie/                 # Streamlit frontend and interaction logic
│   └── app.py                 # Main UI code
├── config/
│   └── docker_utils.py        # Docker start/stop utilities
├── teams/
│   └── dsa_team.py            # AutoGen team config for DSA
├── temp/
│   └── solution.py            # Auto-saved output file
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 🐳 Prerequisites

- Docker installed and running
- Python 3.10+ installed

### 🧪 Local Installation

```bash
# Clone the repository
git clone https://github.com/yourname/dsa-genie.git
cd dsa-genie

# Create virtual environment (WSL or Linux recommended)
python3 -m venv .aivenv
source .aivenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run DSA_Genie/app.py
```

---

## 🧠 Agents Behavior Summary

### 🧞 DSAProblemSolverAgent

- Accepts problem statement
- Explains the approach
- Generates Python code with at least 3 test cases
- Responds with code blocks

### 🧪 CodeExecutorAgent

- Executes the code inside Docker container
- Returns output, errors, or retries
- Saves solution as `solution.py` if successful

---

## 📥 Output

- File: `temp/solution.py`
- Shown in the UI inside a collapsible block
- Downloadable via Streamlit button

---

## 📌 To Do

- [ ] Add GPT-4o / custom model toggle
- [ ] Add solution complexity analysis
- [ ] Add example problem bank dropdown
- [ ] Host online (e.g., on EC2 or Streamlit Community Cloud)

---

## 🧑‍💻 Author

**Arun Shukla** – [LinkedIn](https://www.linkedin.com/in/arun-shukla-1399a9196/)

---

## 📄 License

MIT License. See `LICENSE` file for details.
