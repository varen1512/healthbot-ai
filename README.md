# 🛡️ HealthBot AI (MedGuard Prototype)

HealthBot AI is a secure, multi-modal conversational assistant designed to explain medical terminology, drug purposes, active ingredients, and potential drug-to-drug interactions. Built using **Streamlit** and powered by the **Google GenAI SDK (Gemini 2.5 Flash)**, this application demonstrates strict system-level prompt engineering and safety guardrails.

---

## 🚀 Key Engineering Features
* **Multi-modal Analysis:** Accepts text queries or images (such as medicine strips or prescription sheets) using PIL processing.
* **Rigid System Guardrails:** Programmed to strictly refuse diagnostic requests or medication prescriptions, redirecting users to licensed healthcare practitioners.
* **Production State Configuration:** Configured to read environment keys safely via `st.secrets` instead of hardcoding sensitive API credentials.

## 🛠️ Tech Stack & Architecture
* **Frontend UI:** Streamlit
* **Core Engine:** Google GenAI SDK (`gemini-2.5-flash`)
* **Image Processing:** Pillow (PIL)
* **Environment Management:** Python Secrets Architecture

---

## 💻 Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/varen1512/healthbot-ai.git](https://github.com/varen1512/healthbot-ai.git)
   cd healthbot-ai