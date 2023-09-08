#! usr/bin/env python3


import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

"""PDF report to send to supplier indicating that data is correctly processed"""



def generate_report(filename, title, add_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["Body"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])