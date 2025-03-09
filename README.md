Mood Tracker ❤️

A simple mood tracking application built with Python, UV, and Streamlit.


Getting Started
1️⃣ Install UV
First, install UV (if not already installed):


curl -LsSf https://astral.sh/uv/install.sh | sh
For Windows:


powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Verify installation:


uv --version
2️⃣ Create and Initialize the Project
uv init mood-tracker
cd mood-tracker

3️⃣ Install Sreamlit (Dependency)
uv add streamlit pandas

4️⃣ Activate UV Virtual Environment (Windows)
.venv\Scripts\activate
For Linux/macOS:

source .venv/bin/activate

5️⃣ Run Mood Tracker
streamlit run main.py
🎉 That’s it! Your Mood Tracker is ready to use 🚀