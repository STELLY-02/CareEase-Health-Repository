import os
import yaml
import csv
from pathlib import Path
from models.disease import Disease

def flatten_disease(disease: Disease) -> dict:
    return {
        "name": disease.name,
        "description": disease.description,
        "tags": ",".join(disease.tags),
        "symptoms": ",".join(disease.symptoms),
        "triggers": ",".join(disease.triggers),
        "severity": disease.severity,
        "duration": disease.duration,
        "ageRange": disease.biologicalFilters.ageRange,
        "gender": disease.biologicalFilters.gender,
        "medicalConditions": ",".join(disease.biologicalFilters.medicalConditions),
        "medications": ",".join(disease.biologicalFilters.medications),
        "familyHistory": ",".join(disease.biologicalFilters.familyHistory),
        "lifestyle": ",".join(disease.biologicalFilters.lifestyle),
        "pastHospitalizations": ",".join(disease.biologicalFilters.pastHospitalizations),
        "explanation": disease.response.explanation,
        "suggestedSpecialist": disease.response.suggestedSpecialist,
        "careTips": ",".join(disease.response.careTips)
    }

def main():
    diseases_folder = Path("diseases")
    output_csv = Path("diseases.csv")
    all_rows = []

    for file in diseases_folder.glob("*.yaml"):
        with open(file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            try:
                disease = Disease(**data)
                flat_data = flatten_disease(disease)
                all_rows.append(flat_data)
                print(f"✅ Parsed {file.name}")
            except Exception as e:
                print(f"❌ Error in {file.name}: {e}")

    if all_rows:
        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=all_rows[0].keys())
            writer.writeheader()
            writer.writerows(all_rows)
        print(f"📄 Created/updated: {output_csv}")
    else:
        print("⚠️ No valid YAML files found.")

if __name__ == "__main__":
    main()
