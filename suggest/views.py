from django.shortcuts import render
from dotenv import load_dotenv
from urllib.parse import urlparse
load_dotenv()
import json
import re
import os
from groq import Groq

SAFE_URL_SCHEMES = {"http", "https"}
# Create your views here.
def Index(request):
    return render(request, "suggest/main.html")

def sanitize_text(value: str, max_length: int = 200) -> str:
    if not value:
        return ""
    cleaned = re.sub(r"[^a-zA-Z0-9 ,.\-?!]", "", value)
    return cleaned[:max_length]


def sanitize_tools(tools):
    if not isinstance(tools, list):
        return []
    sanitized = []
    for tool in tools:
        if not isinstance(tool, dict):
            continue
        website = tool.get("website_url", "")
        parsed = urlparse(website) if website else None
        if not parsed or parsed.scheme.lower() not in SAFE_URL_SCHEMES:
            tool = {**tool, "website_url": ""}
        sanitized.append(tool)
    return sanitized


def suggest_output(request):
    if request.method == "POST":
        ROLE_MAP = {
        "std": "Student",
        "hstd": "High School Student",
        "cstd": "College Student",
        "unir": "University Researcher",
        "phdr": "PhD Researcher",
        "teachlect": "Teacher / Lecturer",
        "edutrain": "Educator / Trainer",
        "sfed": "Software Engineer / Developer",
        "fed": "Frontend Developer",
        "bed": "Backend Developer",
        "fsd": "Full Stack Developer",
        "s": "Data Scientist",
        "aie": "AI/ML Engineer",
        "devops": "DevOps Engineer",
        "pmt": "Product Manager (Tech)",
        "gde": "Graphic Designer",
        "uide": "UI/UX Designer",
        "ved": "Video Editor",
        "ani": "Animator",
        "3dmod": "3D Artist / Modeler",
        "wriauger": "Writer / Author / Blogger",
        "cc": "Content Creator / Social Media Creator",
        "dm": "Digital Marketer",
        "seospe": "SEO Specialist",
        "smm": "Social Media Manager",
        "sales": "Salesperson / Account Manager",
        "ent": "Entrepreneur / Startup Founder",
        "busanaly": "Business Analyst / Consultant",
        "pmg": "Project Manager",
        "researcac": "Researcher / Academic",
        "freegig": "Freelancer / Gig Worker",
        "offad": "Office Worker / Admin",
        "passist": "Personal Assistant / Executive Assistant",
        "bloginf": "Blogger / Influencer",
        }
        role = ROLE_MAP.get(request.POST.get("role")) or "General User"
        urreq = request.POST.get("urreq", "")
        safe_requirements = sanitize_text(urreq)
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        prompt = f"""
            You are an AI tool recommendation expert. Suggest 6 real AI tools that match the user's needs. 
            Do NOT include tools without AI capabilities.

            User Role: {role}
            Requirements: {safe_requirements}

            Instructions:
            - Return exactly 6 tools.
            - Each tool must be a JSON object with these fields: 
            "name", "description", "image_url", "website_url", "category".
            - "description" must be concise: no more than 15 words.
            - Only include tools with real AI functionality (e.g., code generation, AI assistants, AI analysis).
            - Return valid JSON array only — no explanations, text, or formatting outside the array.

            Example output:
            [
                {{
                    "name": "GitHub Copilot",
                    "description": "AI-powered code completion and suggestions in your IDE",
                    "image_url": "https://github.com/copilot.png",
                    "website_url": "https://github.com/features/copilot",
                    "category": "Code Assistant"
                }}
            ]
            """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        result = result.replace("“", '"').replace("”", '"')
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
             json_text = re.search(r"\[.*\]", result, re.DOTALL)
             result = json.loads(json_text.group()) if json_text else []

        result = sanitize_tools(result)

        return render(
            request,
            "suggest/main.html",
            {
                "result": result,
                "role": role,
                "urreq": safe_requirements,
            },
        )
    return render(request, "suggest/main.html")