# Project 4 — Hospital Readmission Prediction (Healthcare ML)

## Problem Statement
In the US, hospitals face financial penalties if diabetic patients are readmitted within
30 days of discharge — this costs the healthcare system $26 billion annually. This project
predicts the probability of 30-day readmission for diabetic patients using clinical data:
diagnosis codes, medication changes, lab results, and hospital visit history. Directly
applicable to Indian healthtech companies like Practo, PharmEasy, and Apollo Health.

## Dataset
- **Name:** Diabetes 130-US Hospitals for Years 1999-2008
- **Source:** https://www.kaggle.com/datasets/brandao/diabetes
- **Size:** 101,766 records × 50 features
- **Target:** readmitted (<30, >30, NO) → binary: readmitted within 30 days (Yes/No)
- **Class balance:** ~11% readmitted within 30 days (imbalanced)

## Files to Download from Kaggle
```
diabetic_data.csv      → main dataset
IDs_mapping.csv        → maps admission_type_id, discharge_disposition_id, admission_source_id
```

## Feature Description (key ones)
```
encounter_id           → unique visit ID
patient_nbr            → patient ID (some patients appear multiple times)
race, gender, age      → demographics
admission_type_id      → emergency, urgent, elective etc.
discharge_disposition_id → where patient went after discharge
time_in_hospital       → days admitted (1-14)
num_lab_procedures     → count of lab tests done
num_medications        → number of medications prescribed
number_diagnoses       → total diagnoses recorded
diag_1, diag_2, diag_3 → ICD-9 primary and secondary diagnoses
A1Cresult              → HbA1c test result (None, Norm, >7, >8)
insulin, metformin     → medication change (No, Steady, Up, Down)
readmitted             → target: <30, >30, NO
```

## ML Models Used
| Model | Purpose |
|-------|---------|
| Logistic Regression | Clinical baseline + calibration |
| Decision Tree | Interpretable rules for clinicians |
| Random Forest | Ensemble baseline |
| LightGBM (lgb.LGBMClassifier) | Primary model — best AUROC |

## Key Techniques
- ICD-9 diagnosis code grouping: 700+ codes → 9 clinical categories (Circulatory, Respiratory, Diabetes, etc.)
- Heavy missing value treatment: ? values in race, diag columns
- Handle duplicate patients: keep only first encounter per patient
- SMOTE for class imbalance + class_weight comparison
- Probability calibration: Platt scaling (sigmoid) for reliable risk scores
- SHAP force plots: per-patient risk explanation for clinicians
- Threshold tuning: optimise for recall (missing a readmission is costly)

## Evaluation Metrics
- Primary: **AUROC** (standard clinical ML metric)
- Secondary: Calibration curve (reliability diagram), Precision-Recall AUC
- Clinical metric: Sensitivity at 80% Specificity operating point

## Expected Output / Insights
1. Calibration curve — proves model probabilities are reliable, not just rankings
2. SHAP: top drivers of readmission (num_medications, time_in_hospital, A1Cresult)
3. Risk score distribution: what % of patients fall in high/medium/low risk bands
4. Comparison: model with ICD-9 grouping vs raw codes

## Resume Bullet
> Developed a clinical readmission prediction model on 100k+ diabetic patient records using
> LightGBM with ICD-9 diagnosis grouping and probability calibration (Platt scaling), achieving
> 0.67 AUROC. Applied SMOTE for class imbalance and delivered SHAP-based per-patient
> risk explanations for clinical interpretability.

## How to Run
```bash
make train        # runs full pipeline
make evaluate     # generates reports/figures/
make predict      # score new patients
```
