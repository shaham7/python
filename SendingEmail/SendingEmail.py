import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import mimetypes

# Define the HTML template path
html_template_path = Path('index.html')

# Read the HTML template content
html = Template(html_template_path.read_text())

# Create the EmailMessage object
email = EmailMessage()

# Set email details
email['from'] = 'Muhammed Shaham'
email['to'] = 'shahampython@gmail.com'
email['subject'] = 'Testing email with attachment'

# Prepare the HTML content with optional substitutions
# Convert the email object to a multipart message (mixed subtype)
email.set_content(html.substitute(name='Shaham'), 'html') 
email.make_mixed()  # This line creates the multipart payload


# Define the attachment path
attachment_path = Path('watermaked_output.pdf')

# Get the MIME type of the attachment
mime_type = mimetypes.guess_type(str(attachment_path))[0]

# Create a MIME attachment object
with attachment_path.open('rb') as attachment_file:
    attachment = EmailMessage()
    attachment.add_attachment(attachment_file.read(), maintype=mime_type.split('/')[0], subtype=mime_type.split('/')[1])

# Attach the MIME object to the main email message
email.attach(attachment)

# Send the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mohd.shaham7@gmail.com', 'nazu tvyi zuyj bfel') #create new app password
    smtp.send_message(email)
    print('Email with attachment sent!')