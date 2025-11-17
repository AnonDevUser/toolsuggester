# StuSuggester – AI Tool Suggester for Students and Professionals

**StuSuggester** is an AI-powered tool recommendation platform that helps students, educators, developers, and professionals discover the best AI tools tailored to their role and specific requirements. The platform leverages Groq’s AI API to generate curated suggestions in real-time, making it easy to find the right tools for productivity, coding, learning, and business.



## 🚀 Features

- AI-driven tool suggestions based on **user role and requirements**  
- Supports multiple roles: students, teachers, developers, marketers, and more  
- Returns tools with **name, description, category, website, and image**  
- **Sanitized and safe URLs** to prevent malicious links  
- Responsive UI built with Django templates  
- Easy deployment with Render or other cloud providers  


## 📌 Tech Stack

- **Backend**: Python 3.11, Django 4.2  
- **AI Integration**: Groq API  
- **Frontend**: HTML, CSS, JS (static files served via Django & WhiteNoise)  
- **Database**: SQLite (default)  
- **Deployment**: Render, GitHub Actions, or any cloud platform supporting Django  



## 🌱 Getting Started

Follow these steps to clone and run the project locally.

### **1. Clone the repository**

```bash
git clone git@github.com:AnonDevUser/toolsuggester.git
cd toolsuggester
```
### **2. Create a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# OR
.venv\Scripts\activate     # Windows
```
### **3. Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### **4. Create a `.env` file**
Create a .env file in the root of the project with the following variables:
```bash
GROQ_API_KEY=your_groq_api_key_here
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,yourdomain.com
DJANGO_DEBUG=True
```
> Replace your_groq_api_key_here with your actual Groq API key. DJANGO_ALLOWED_HOSTS can include multiple hosts separated by commas.

### **5. Collect static files**
```bash
python manage.py collectstatic --noinput
```
### **6. Run the development server**
```bash
python manage.py runserver
```
## 🔑 Environment Variables

`GROQ_API_KEY`: Your API key for Groq AI integration

`DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
## 📦 Folder Structure
```bash
toolsuggester/
│
├─ suggest/            # Django app
│  ├─ templates/       # HTML templates
│  ├─ static/          # CSS, JS, images
│  ├─ views.py         # Main logic
│
├─ .env                # Local environment file (ignored)
├─ manage.py
├─ requirements.txt
├─ README.md

```

## 🌐 Keywords

AI tool suggestion, Groq AI, student productivity tools, developer AI tools, teacher AI tools, AI recommendations platform, StuSuggester, AI tool finder, Django AI app

## 📄 License

This project is licensed under the MIT License.
