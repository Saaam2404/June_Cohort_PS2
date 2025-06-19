import re
import spacy
import time
from Speech_to_Text import Voice

nlp = spacy.load("en_core_web_sm")

class PersonalInfo:
    @staticmethod
    def extract_info(text):
        doc = nlp(text)

        name = None
        age = None
        phone = None
        gender = None
        address = None

        # Name Extraction
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                name = ent.text.title()
                break

        # Age Extraction
        age_match = re.search(r'\b(\d{1,3})\s*(years old|yrs|yo|y/o)?\b', text, re.IGNORECASE)
        if age_match:
            age = age_match.group(1)

        # Phone Extraction
        phone_match = re.search(r'\b\d{10}\b', text)
        if phone_match:
            phone = phone_match.group(0)

        # Gender Extraction
        gender_match = re.search(r'\b(Male|Female|Other)\b', text, re.IGNORECASE)
        if gender_match:
            gender = gender_match.group(0).capitalize()

        # Address Extraction
        address_keywords = [
            "address", "resides at", "lives at", "located at", "home is", "at",
            "stays at", "house is at", "house address", "residence", "home address",
            "they live at", "staying at", "currently at", "present address",
            "permanent address", "current location","i live in","i live at","lives in","leaves at"
        ]
        for keyword in address_keywords:
            if keyword in text.lower():
                start_index = text.lower().find(keyword)
                address = text[start_index + len(keyword):].split('.')[0].strip()
                break
        return {
            "Name": name or "Unknown",
            "Age": age or "Unknown",
            "Phone": phone or "Unknown",
            "Gender": gender or "Unknown",
            "Address": address or "Unknown"
        }


class Diagnosis:
    symptom_department_map = {
        "fever": "General Medicine",
        "cough": "Pulmonology",
        "chest pain": "Cardiology",
        "shortness of breath": "Pulmonology",
        "headache": "Neurology",
        "dizziness": "Neurology",
        "abdominal pain": "Gastroenterology",
        "diarrhea": "Gastroenterology",
        "vomiting": "Gastroenterology",
        "rash": "Dermatology",
        "joint pain": "Orthopedics",
        "back pain": "Orthopedics",
        "sore throat": "ENT",
        "ear pain": "ENT",
        "vision loss": "Ophthalmology",
        "fatigue": "General Medicine",
        "weight loss": "Endocrinology",
        "high blood sugar": "Endocrinology",
        "low blood pressure": "Cardiology",
        "heart problem":"Cardiology"
    }

    @staticmethod
    def extract_symptoms(text):
        found = []
        for symptom, department in Diagnosis.symptom_department_map.items():
            if symptom in text.lower():
                found.append((symptom, department))
        return found

    @staticmethod
    def extract_appointment_date(text):
        date_patterns = [
            r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b",
            r"\b(\d{1,2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4})\b",
            r"\b((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? ?\d{4})\b"
        ]
        for pattern in date_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(0)
        return "Not specified"