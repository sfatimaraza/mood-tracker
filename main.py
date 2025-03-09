import streamlit as st # for creating web interface
import pandas as pd #for data manipulation
import datetime # for handling dates
import csv # for reading and writing to CSV file
import os # for file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create empty DataFrame with columns
        return pd.DataFrame(columns=["Date", "Mood",])
        # Read and return existing mood data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
       # Open file in append mode
    with open(MOOD_FILE, "a") as file:

 # Create CSV writer
        writer = csv.writer(file)

  # Add new mood entry
        writer.writerow([date, mood])

# Streamlit app title
st.title("Mood Tracker ❤️")

# Get today's date
from datetime import datetime
today = datetime.today()

# Create subheader for mood input
st.subheader("How are you feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select you mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):

 # Save mood when button is clicked
    save_mood_data(today, mood)

 # Show success message
    st.success("Mood logged successfully!")

# Load mood data
data = load_mood_data()

# Check if data is not empty
if not data.empty:

      # Create section for Visualization
    st.subheader("Mood Trends Over Time")

      # Create section for Visualization
    data["Date"] = pd.to_datetime(data["Date"])

         # Count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)

# Build with love by Fatima Raza
    st.write("Build with ❤️ by [Fatima Raza] (https://github.com/sfatimaraza)")