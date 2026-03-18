from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from utils.helpers import advanced_insights
def generate_report(df):
    
    insights=advanced_insights(df)
    path = "executive_report.pdf"

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("SkyCity Channel Analytics Report", styles['Title'])
    )

    for i in insights:
        story.append(Paragraph(i, styles['Normal'],bulletText="•"))

    doc = SimpleDocTemplate(path)

    doc.build(story)

    return path
