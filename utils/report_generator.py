from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(insights):

    path = "executive_report.pdf"

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("SkyCity Channel Analytics Report", styles['Title'])
    )

    for i in insights:
        story.append(Paragraph(i, styles['Normal']))

    doc = SimpleDocTemplate(path)

    doc.build(story)

    return path