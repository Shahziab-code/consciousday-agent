# 🌅 ConsciousDay Agent – Journaling & Day-Planning AI Assistant  

ConsciousDay Agent is a **journaling-based AI assistant** that helps users reflect on their emotions, interpret dreams, and plan their day effectively. Built with **LangChain**, **Streamlit**, and **OpenRouter**, it’s a simple yet powerful daily companion.  

---

## **✨ Features**

✅ **Google OAuth Login** (secure authentication)  
✅ **Daily Journal Form**:  
   - Morning Journal (free-form)  
   - Dream (free-form)  
   - Intention of the Day  
   - Top 3 Priorities  

✅ **AI-Powered Reflection**:  
   - Inner Reflection Summary  
   - Dream Interpretation  
   - Energy/Mindset Insight  
   - Suggested Day Strategy (time-aligned tasks)  

✅ **Data Storage in SQLite**: Saves all journal entries locally in `entries.db`  
✅ **View Past Entries by Date**  
✅ **Clean UI**: Cards, icons, columns & colors  
✅ **Modular Codebase**: Separated into `agent/`, `db/`, and main `app.py`  
✅ **Deployable on Streamlit Cloud**  

---

## **🖼️ UI Preview**

> Add screenshots here:
> ```
> ![Login Page](screenshots/login.png)
> ![Journal Form](screenshots/journal_form.png)
> ![Past Entries](screenshots/past_entries.png)
> ```

---

## **🛠 Tech Stack**

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/)  
- **AI & LLM Integration:** [LangChain](https://www.langchain.com/)  
- **LLM API Provider:** [OpenRouter](https://openrouter.ai/)  
- **Database:** SQLite (local `entries.db`)  
- **Authentication:** Google OAuth (via [Authlib](https://docs.authlib.org/))  
- **Environment Variables:** `python-dotenv`  

---

## **📂 Project Structure**

