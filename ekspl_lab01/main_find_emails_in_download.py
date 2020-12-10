from email_finder import read_emails_from_download
from io_functions import write_emails_to_csv

emails = read_emails_from_download()
print(emails)

write_emails_to_csv(emails, "emails")
