# 🛠️ GitHub Repository Setup Guide

This guide provides simple instructions to publish your **Summarization Project** as a standalone repository on GitHub.

---

## 📝 Repository Metadata

Use these details when creating the repository on GitHub:

- **Repository Name**: `summarization-project` or `summarization-app-langchain`
- **Description**: `A Streamlit-based text and video summarization application using LangChain and Groq LLM.`
- **Visibility**: `Public` (recommended) or `Private`
- **Initialize Repository**: **Do NOT** check any checkboxes (like *Add a README*, *Add .gitignore*, or *Choose a license*) because we have already created these files locally!

---

## 💻 Step-by-Step CLI Instructions

Since your parent directory `gen ai projects` is already a Git repository, you need to initialize a independent repository inside the `summarization project` subdirectory:

### Step 1: Open a terminal inside the project folder
Ensure you are in the correct directory:
```bash
cd "c:\Users\LENOVO\Desktop\gen ai projects\summarization project"
```

### Step 2: Initialize Git locally
Initialize a new local Git repository in this folder:
```bash
git init
```

### Step 3: Add and Commit Files
Stage all your files and make your first commit:
```bash
git add .
git commit -m "Initial commit: Streamlit Summarizer App using Langchain & Groq"
```

### Step 4: Create the Repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Enter the Repository Name: **`summarization-project`**.
3. Enter the Description.
4. Click **Create repository**.

### Step 5: Link Local Repo to GitHub & Push
Copy the commands from the GitHub instruction page or run the following (replace `<your-username>` with your GitHub username, which is `Ah200512`):

```bash
git branch -M main
git remote add origin https://github.com/Ah200512/summarization-project.git
git push -u origin main
```

---

## 🎉 Done!
Your project is now live on GitHub with a premium README, full dependency mapping, and neat ignore rules!
