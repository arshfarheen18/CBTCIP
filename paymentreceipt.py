from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_receipt(customer_name, payment_date, payment_amount, payment_method, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    c.drawString(250, 750, "PAYMENT RECEIPT")
    c.drawString(220, 730, "--------------------------------------------------")
    c.drawString(100, 700, f"Customer Name   : {customer_name}")
    c.drawString(100, 680, f"Payment Date    : {payment_date}")
    c.drawString(100, 660, f"Payment Amount  : Rs.{payment_amount:.2f}")
    c.drawString(100, 640, f"Payment Method  : {payment_method}")
    c.drawString(100, 620, "Thank you for your payment!")

    c.save()

    print(f"Receipt saved to {pdf_filename}")

# Get user input for creating the receipt
customer_name = input("Enter customer name: ")
payment_date = input("Enter payment date: ")
payment_amount = float(input("Enter payment amount: "))
payment_method = input("Enter payment method: ")

pdf_filename = "payment_receipt.pdf"

# Create the receipt as a PDF
create_receipt(customer_name, payment_date, payment_amount, payment_method, pdf_filename)
