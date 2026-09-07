import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    emails = re.findall(pattern, text)
    
    return emails


text = input("Enter a text: ")

result = find_emails(text)

print("Email addresses found:")

if result:
    for email in result:
        print(email)
else:
    print("No email address found.")