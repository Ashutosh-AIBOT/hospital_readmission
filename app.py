import os

from dashboard_core import ProjectConfig, run_project_app


CONFIG = ProjectConfig(
    key="Project 04",
    title="Hospital Readmission Prediction",
    subtitle="Clinical risk modeling for 30-day readmission management",
    icon="🏥",
    domain="Healthcare operations and care quality",
    objective="Estimate readmission risk to support discharge planning and care coordination.",
    business_value="Improves patient outcomes while reducing avoidable readmission penalties.",
    prediction_label="Readmission Risk",
    highlights=[
        "Applies calibrated clinical models to improve probability quality in sensitive workflows.",
        "Enables early intervention for high-risk patients via practical risk scoring.",
        "Uses transparent benchmark and notebook traceability for medical governance.",
        "Organizes model evidence to support quality and compliance conversations.",
        "Shows healthcare-aware framing of ML outcomes into operational impact.",
    ],
)


run_project_app(CONFIG, os.path.dirname(__file__))
