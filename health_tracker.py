# health_tracker.py
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Optional

@dataclass
class Patient:
    id: str
    name: str
    age: int
    conditions: List[str]
    medications: List[str]

class HealthTracker:
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
    
    def add_patient(self, patient: Patient):
        self.patients[patient.id] = patient
        print(f"Added patient: {patient.name}")
    
    def get_patient_summary(self, patient_id: str) -> str:
        if patient := self.patients.get(patient_id):
            summary = [
                f"\nPatient Summary",
                f"Name: {patient.name}",
                f"Age: {patient.age}",
                f"\nConditions:",
                *[f"- {condition}" for condition in patient.conditions],
                f"\nMedications:",
                *[f"- {medication}" for medication in patient.medications]
            ]
            return "\n".join(summary)
        return "Patient not found"

def main():
    # Create a health tracker instance
    tracker = HealthTracker()
    
    # Add a test patient
    test_patient = Patient(
        id="P001",
        name="John Doe",
        age=45,
        conditions=["Diabetes Type 2", "Hypertension"],
        medications=["Metformin", "Lisinopril"]
    )
    
    # Add patient to tracker
    tracker.add_patient(test_patient)
    
    # Print patient summary
    print(tracker.get_patient_summary("P001"))

if __name__ == "__main__":
    main()