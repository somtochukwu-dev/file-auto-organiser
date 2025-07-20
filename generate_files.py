import os
import random

# Folder to generate files in
folder = 'business-folder'

file_prefixes = [
    'Contract', 'Invoice', 'Report', 'Summary', 'MeetingNotes',
    'ClientFeedback', 'Receipt', 'DesignDraft', 'MarketingPlan', 'FinancialStatement'
]
file_extensions = ['.pdf', '.docx', '.xlsx', '.txt', '.png', '.jpg']

# Create the folder if it doesn't exist
os.makedirs(folder, exist_ok=True)

# Generate 100 fake files
for i in range(1, 101):
    prefix = random.choice(file_prefixes)
    ext = random.choice(file_extensions)
    filename = f"{prefix}_{random.randint(1000, 9999)}{ext}"
    filepath = os.path.join(folder, filename)
    open(filepath, 'w').close()  # Create an empty file

print("✅ 100 fake business files created!")
