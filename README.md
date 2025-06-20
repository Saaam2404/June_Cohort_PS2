# Voice-Based Medical Appointment System

A voice-controlled GUI application for collecting patient details, diagnosing basic symptoms, and automatically saving appointment data to an Excel sheet.

---

## Features

- Voice Input: Capture user speech to fill out patient details.
- NLP Extraction: Uses spaCy and regex to extract name, age, gender, address, and more.
- Symptom Analysis: Maps symptoms to medical departments automatically.
- Appointment Logging: Stores all data (including timestamp) into an Excel file.
- Persistent Storage: All records saved to `appointments.xlsx`.

---

## Modules

### `GUI.py`:
[GUI.py](https://github.com/Saaam2404/June_Cohort_PS2/blob/master/GUI.py)
- Main file that launches the Tkinter GUI.
- Uses a microphone button to trigger speech capture.Need to be pressed only once.
- Asks sequentially for:
  1. Personal Info (Name, Age, Gender, Address)
  2. Symptoms
  3. Appointment Date
- Each sequence has a time of 30sec to speak
- Asks for confirmation if the converted text is correct and then only proceeds if it is yes,else asks to speak again.
- Displays extracted and confirmed data on screen.

### `parse.py`
[parse.py](https://github.com/Saaam2404/June_Cohort_PS2/blob/master/parse.py)
- Contains:
  - `PersonalInfo.extract_info(text)`: Uses spaCy & regex to extract patient details.
  - `Diagnosis.extract_symptoms(text)`: Maps known symptoms to departments.
  - `Diagnosis.extract_appointment_date(text)`: Extracts and formats the date.

### `Speech_to_Text.py`
[Speech_to_Text.py](https://github.com/Saaam2404/June_Cohort_PS2/blob/master/Speech_to_Text.py)
- Handles speech-to-text conversion.
- Uses Google’s SpeechRecognition API.

### `database.py`
[Database.py](https://github.com/Saaam2404/June_Cohort_PS2/blob/master/database.py)
- `Appointments.save_appointment(...)`: Saves the entire record to an Excel sheet (`appointments.xlsx`).
- `Appointments.display_appointments()`: Prints all records from the file.

---
## Deployment
[Deployment Video](https://drive.google.com/drive/folders/1KiiD0MeB32g2h04x0WXqkzC7uw1SLuBx?usp=sharing)
The link contains a recording demonstating how our project works.

---

## Execution
To execute and view the project run GUI.py file. All the modules have been implemented in it.

---

## Excel Format

Saved as `appointments.xlsx` with the following columns:

- Patient Name
- Age
- Gender
- Address
- Symptoms
- Department Allotted
- Appointment Date
- Timestamp

---

## Requirements

- `Python 3.7+`
- `Tkinter`
- `SpeechRecognition`
- `openpyxl`
- `pyaudio`
- `spaCy` + `en_core_web_sm`

Install them via:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
