# Gen AI Application with Groq

This **Generative AI chatbot** is built using **Streamlit**, **LangChain**, and **Groq API** to provide natural, human-like conversational interactions. It supports **multi-session chat history**, a user-friendly **sidebar for chat management**, and **clean AI response formatting**.

## 🚀 Features

✅ **Conversational AI** – Provides natural, human-like responses using Groq API.  
✅ **Multi-Session Chat** – Allows users to store and access previous chat histories.  
✅ **Optimized UI** – Features a sidebar for chat selection with truncated chat titles.  
✅ **Efficient Chat Storage** – Uses `deque` for optimized memory management.  
✅ **Custom Styling** – CSS-enhanced UI for an interactive experience. 

---

## 🛠 Tech Stack Used

### 🎨 Frontend & UI Framework
- **Streamlit** – Used to build the interactive web application interface.

### ⚙️ Backend & Processing
- **LangChain** – Manages chat prompts and model interactions.
- **Groq API** – Provides the AI model for generating responses.
- **Python** – The core programming language used for development.

### 🗄 Data Handling & Storage
- **`deque` (from `collections`)** – Optimized data structure for efficient chat history management.

### 🔐 Environment Management
- **`dotenv`** – Loads environment variables securely (e.g., API keys).

### 🎨 Styling & Customization
- **CSS (inside Streamlit markdown)** – Custom styles for the sidebar and UI elements.

This stack ensures smooth AI-powered chatbot interactions with multi-session support and an optimized user experience. 🚀

---

## 📸 Screenshots  

### 🏠 Home Screen  
Displays the application interface when first launched.  
![Home Screen](Screenshot%202025-03-16%20120226.png)

### 💬 Chat Interface  
Shows real-time interaction between user and AI.  
![Chat Interface](Screenshot%202025-03-16%20120309.png)

### 📂 Sidebar with Chat History  
Allows users to manage multiple chat sessions.  
![Sidebar](Screenshot%202025-03-16%20120444.png)

---

## 🔧 Installation Guide  

1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/MeeturiAjay/GenAI_app_using_groq.git
cd GenAI_app_using_groq
