from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


styles = getSampleStyleSheet()

TITLE = styles["Title"]
TITLE.alignment = TA_CENTER

HEADING = styles["Heading1"]

BODY = styles["BodyText"]


def add_page_number(canvas, doc):
    canvas.saveState()

    canvas.setFont("Helvetica", 9)

    canvas.drawRightString(
        7.8 * inch,
        0.5 * inch,
        f"Page {doc.page}"
    )

    canvas.restoreState()


def generate_pdf(report, filename):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    story = []

    # ==================================================
    # HEADER
    # ==================================================

    story.append(
        Paragraph(
            "🚗 IntelliClaim AI",
            TITLE,
        )
    )

    story.append(
        Paragraph(
            "<b>AI Insurance Claim Assessment Report</b>",
            BODY,
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ==================================================
    # CLAIM SUMMARY
    # ==================================================

    story.append(
        Paragraph(
            "Claim Summary",
            HEADING,
        )
    )

    decision = report.get("decision", {})
    nlp = report.get("nlp", {})
    cv = report.get("cv", [])

    summary = [

        ["Claim ID", report.get("claim_id", "")],

        ["Decision", decision.get("decision", "")],

        ["Coverage", decision.get("coverage", "")],

        ["Fraud Score", str(decision.get("fraud_score", ""))],

        ["Reason", decision.get("reason", "")],

    ]

    table = Table(
        summary,
        colWidths=[150, 300],
    )

    table.setStyle(

        TableStyle(

            [

                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),

                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

                ("TOPPADDING", (0, 0), (-1, -1), 8),

            ]

        )

    )

    story.append(table)

    story.append(Spacer(1, 20))

    # ==================================================
    # COMPUTER VISION
    # ==================================================

    story.append(
        Paragraph(
            "Computer Vision Assessment",
            HEADING,
        )
    )

    if cv:

        damage = cv[0]

        cv_table = [

            ["Image", damage["image_name"]],

            ["Severity", damage["severity"]],

            ["Repairable", str(damage["repairable"])],

            ["Repair Cost", str(damage["repair_cost"])],

            ["Repair Days", str(damage["repair_days"])],

        ]

        t = Table(
            cv_table,
            colWidths=[150, 300],
        )

        t.setStyle(

            TableStyle(

                [

                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

                    ("BACKGROUND", (0, 0), (0, -1), colors.beige),

                ]

            )

        )

        story.append(t)

        story.append(
            Spacer(1, 15)
        )

        story.append(
            Paragraph(
                "<b>Detected Objects</b>",
                BODY,
            )
        )

        rows = [

            [
                "Class",
                "Confidence",
            ]

        ]

        for d in damage["detections"]:

            rows.append(

                [

                    d["class_name"],

                    f"{d['confidence']:.2f}",

                ]

            )

        det_table = Table(
            rows,
            colWidths=[250, 150],
        )

        det_table.setStyle(

            TableStyle(

                [

                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

                    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ]

            )

        )

        story.append(det_table)

    story.append(
        Spacer(1, 20)
    )

    # ==================================================
    # NLP
    # ==================================================

    story.append(
        Paragraph(
            "Natural Language Analysis",
            HEADING,
        )
    )

    nlp_table = [

        ["Accident Type", nlp.get("accident_type", "")],

        ["Vehicle Part", nlp.get("vehicle_part", "")],

        ["Weather", nlp.get("weather", "")],

        ["Severity", nlp.get("severity", "")],

        ["Cause", nlp.get("cause", "")],

    ]

    t = Table(
        nlp_table,
        colWidths=[150, 300],
    )

    t.setStyle(

        TableStyle(

            [

                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

                ("BACKGROUND", (0, 0), (0, -1), colors.lightblue),

            ]

        )

    )

    story.append(t)

    story.append(
        Spacer(1, 20)
    )

    # ==================================================
    # CREWAI SUMMARY
    # ==================================================

    story.append(
        Paragraph(
            "Executive Summary",
            HEADING,
        )
    )

    summary = f"""
    The submitted insurance claim <b>{report['claim_id']}</b> was processed using the
    IntelliClaim AI platform.

    Computer Vision identified <b>{cv[0]['severity'] if cv else 'Unknown'}</b>
    vehicle damage.

    NLP classified the accident as
    <b>{nlp.get('accident_type','Unknown')}</b>.

    Policy verification indicates the claim is
    <b>{decision.get('coverage','Unknown')}</b>.

    Fraud score is
    <b>{decision.get('fraud_score','0')}</b>.

    Based on the combined outputs of all AI modules,
    the recommended decision is

    <b>{decision.get('decision','')}</b>.
    """

    story.append(
        Paragraph(
            summary,
            BODY,
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ==================================================
    # FOOTER
    # ==================================================

    story.append(
        Paragraph(
            "<b>Generated by IntelliClaim AI</b>",
            BODY,
        )
    )

    doc.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number,
    )