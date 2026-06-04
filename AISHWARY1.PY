import tkinter as tk
from tkinter import messagebox



data = {
    "fever": {
        "symptoms": "High temperature, body pain, weakness",
        "medicine": "Paracetamol (Dolo 650 / Crocin)",
        "advice": "Drink water, rest, take light food"
    },
    "cold": {
        "symptoms": "Sneezing, runny nose, cough",
        "medicine": "Cetirizine / Levocetirizine",
        "advice": "Steam inhalation, warm fluids"
    },
    "headache": {
        "symptoms": "Pain in head, stress, tiredness",
        "medicine": "Paracetamol / Ibuprofen",
        "advice": "Sleep properly, reduce screen time"
    },
    "cough": {
        "symptoms": "Dry or wet cough, throat irritation",
        "medicine": "Dextromethorphan syrup",
        "advice": "Warm water, honey, steam inhalation"
    },
    "acidity": {
        "symptoms": "Burning in stomach, gas, discomfort",
        "medicine": "Pantoprazole / Omeprazole",
        "advice": "Avoid spicy food, eat small meals"
    },
    "diarrhea": {
        "symptoms": "Loose motion, dehydration",
        "medicine": "ORS + Loperamide",
        "advice": "Drink ORS, avoid oily food"
    },
    "vomiting": {
        "symptoms": "Nausea, vomiting, weakness",
        "medicine": "Domperidone (doctor advice)",
        "advice": "Drink fluids slowly, rest"
    },
    "malaria": {
        "symptoms": "High fever, chills, sweating",
        "medicine": "Antimalarial drugs (doctor prescribed)",
        "advice": "Use mosquito net, avoid stagnant water"
    },
    "dengue": {
        "symptoms": "High fever, joint pain, low platelets",
        "medicine": "Supportive care only",
        "advice": "Drink fluids, hospital monitoring"
    },
    "typhoid": {
        "symptoms": "Fever, weakness, stomach pain",
        "medicine": "Antibiotics (doctor prescribed)",
        "advice": "Rest and hydration"
    },
    "allergy": {
        "symptoms": "Skin itching, sneezing, redness",
        "medicine": "Antihistamines",
        "advice": "Avoid allergens like dust"
    },
    "infection": {
        "symptoms": "Redness, swelling, pain",
        "medicine": "Antibiotics (doctor prescription)",
        "advice": "Keep area clean"
    },
    "body pain": {
        "symptoms": "Muscle pain, fatigue",
        "medicine": "Ibuprofen / Diclofenac gel",
        "advice": "Rest and warm compress"
    },
    "eye pain": {
        "symptoms": "Eye irritation, redness",
        "medicine": "Eye drops (doctor advice)",
        "advice": "Avoid screen overuse"
    },
    "ear pain": {
        "symptoms": "Ear infection, pain",
        "medicine": "Antibiotic ear drops",
        "advice": "Keep ear clean and dry"
    },

    "appendicitis": {
        "symptoms": "Severe right side stomach pain, vomiting",
        "medicine": "Surgery (Appendectomy)",
        "advice": "Go to hospital immediately"
    },
    "kidney stone": {
        "symptoms": "Severe back pain, painful urination",
        "medicine": "Pain relief + surgery",
        "advice": "Drink water, medical consultation"
    },
    "fracture": {
        "symptoms": "Bone pain, swelling, unable to move",
        "medicine": "Casting / Surgery",
        "advice": "Do not move injured area"
    },
    "heart attack": {
        "symptoms": "Chest pain, sweating, breathlessness",
        "medicine": "Emergency hospital treatment",
        "advice": "Call ambulance immediately"
    },
    "brain stroke": {
        "symptoms": "Face drooping, weakness, speech problem",
        "medicine": "Emergency treatment",
        "advice": "Reach hospital within minutes"
    },
    "asthma": {
        "symptoms": "Breathing difficulty, wheezing",
        "medicine": "Inhaler (Salbutamol)",
        "advice": "Avoid dust and smoke"
    },
    "bp high": {
        "symptoms": "Headache, dizziness, chest pressure",
        "medicine": "Amlodipine (doctor prescribed)",
        "advice": "Reduce salt intake"
    },
    "bp low": {
        "symptoms": "Weakness, fainting",
        "medicine": "ORS / salt sugar water",
        "advice": "Rest and hydration"
    }
}


def search_disease():
    name = entry.get().lower().strip()

    if name in data:
        result = data[name]
        output.set(
            f"Symptoms: {result['symptoms']}\n\n"
            f"Medicine/Treatment: {result['medicine']}\n\n"
            f"Advice: {result['advice']}"
        )
    else:
        messagebox.showerror("Not Found", "No data found for this disease")


root = tk.Tk()
root.title("Health Info App (200+ Medical Data)")
root.geometry("500x550")

label = tk.Label(root, text="Enter Disease Name", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

btn = tk.Button(root, text="Search", command=search_disease)
btn.pack(pady=10)

output = tk.StringVar()

result_label = tk.Label(
    root,
    textvariable=output,
    justify="left",
    wraplength=450
)
result_label.pack(pady=20)

root.mainloop()