from pathlib import Path
import pandas as pd

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]

CSV_PATH = (
    PROJECT_ROOT
    / "data"
    / "policies"
    / "policy_master.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "rag"
    / "documents"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)
styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER

heading = styles["Heading2"]

normal = styles["BodyText"]

def create_policy_pdf(row):

    filename = OUTPUT_DIR / f"{row['Policy_Number']}.pdf"

    doc = SimpleDocTemplate(str(filename))

    story = []
    story.append(
        Paragraph(
            "SHA Insurance Pvt. Ltd.",
            title_style,
        )
    )

    story.append(
        Paragraph(
            "Motor Insurance Policy",
            heading,
        )
    )

    story.append(Spacer(1, 0.3 * inch))
    story.append(
        Paragraph(
            "<b>Policy Information</b>",
            heading,
        )
    )

    fields = [

        ("Policy Number", row["Policy_Number"]),

        ("Customer ID", row["Customer_ID"]),

        ("Policy Type", row["Policy_Type"]),

        ("Insurance Provider", row["Insurance_Provider"]),

        ("Premium Amount", f"₹ {row['Premium_Amount']}"),

        ("Sum Insured", f"₹ {row['Sum_Insured']}"),

        ("Deductible", f"₹ {row['Deductible']}"),

        ("Roadside Assistance", row["Roadside_Assistance"]),

        ("Engine Protection", row["Engine_Protection"]),

        ("Personal Accident Cover", row["Personal_Accident_Cover"]),

        ("Valid From", row["Valid_From"]),

        ("Valid To", row["Valid_To"]),

        ("Policy Status", row["Policy_Status"]),
    ]

    for key, value in fields:

        story.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                normal,
            )
        )

    story.append(Spacer(1, 0.3 * inch))
    story.append(
        Paragraph(
            "Coverage",
            heading,
        )
    )
    policy = row["Policy_Type"]

    if policy == "Comprehensive":

        coverage = """
• Covers accidental collision damage.<br/>
• Covers scratches and dents.<br/>
• Covers bumper, bonnet, doors and fenders.<br/>
• Covers fire and theft.<br/>
• Covers natural disasters.<br/>
"""

    elif policy == "Third Party":

        coverage = """
• Covers third-party injury.<br/>
• Covers third-party property damage.<br/>
• Does NOT cover own vehicle damage.<br/>
"""

    else:

        coverage = """
• Covers accidental damage.<br/>
• Zero depreciation benefits apply.<br/>
• Full replacement for eligible parts.<br/>
"""


    story.append(
        Paragraph(
            coverage,
            normal,
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    story.append(
        Paragraph(
            "Policy Exclusions",
            heading,
        )
    )

    exclusions = """
• Driving under alcohol influence.<br/>
• Racing or speed testing.<br/>
• Mechanical wear and tear.<br/>
• Unauthorized vehicle modifications.<br/>
• Damage due to war or nuclear risks.<br/>
"""

    story.append(
        Paragraph(
            exclusions,
            normal,
        )
    )

    story.append(Spacer(1, 0.25 * inch))
    story.append(
        Paragraph(
            "Claim Procedure",
            heading,
        )
    )

    claim = """
1. Report accident within 48 hours.<br/>
2. Upload damage photographs.<br/>
3. Submit required documents.<br/>
4. Vehicle inspection.<br/>
5. Repair estimate approval.<br/>
6. Claim settlement.<br/>
"""

    story.append(
        Paragraph(
            claim,
            normal,
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    story.append(
        Paragraph(
            "Frequently Asked Questions",
            heading,
        )
    )

    faq = f"""
<b>Q.</b> Is bumper damage covered?<br/>
<b>A.</b> {'Yes' if policy != 'Third Party' else 'No'}<br/><br/>

<b>Q.</b> Are scratches covered?<br/>
<b>A.</b> {'Yes' if policy != 'Third Party' else 'No'}<br/><br/>

<b>Q.</b> Does this policy include roadside assistance?<br/>
<b>A.</b> {row['Roadside_Assistance']}<br/><br/>

<b>Q.</b> Does this policy include engine protection?<br/>
<b>A.</b> {row['Engine_Protection']}<br/><br/>

<b>Q.</b> What is the deductible?<br/>
<b>A.</b> ₹ {row['Deductible']}<br/>
"""

    story.append(
        Paragraph(
            faq,
            normal,
        )
    )
    doc.build(story)

def main():

    df = pd.read_csv(CSV_PATH)

    for _, row in df.iterrows():

        create_policy_pdf(row)

    print("=" * 60)
    print("Policy PDFs Generated Successfully")
    print("=" * 60)
    print(f"Total PDFs : {len(df)}")
    print(f"Location   : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()