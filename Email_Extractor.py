import re
import os

def extract_emails(input_filename, output_filename):
    # 1. os module: Verify the input file actually exists before trying to read it
    if not os.path.exists(input_filename):
        print(f"Error: The file '{input_filename}' was not found in this directory.")
        print("Please create it and add some text with emails to test the script.")
        return

    print(f"Scanning '{input_filename}' for email addresses...")

    # 2. File Handling (Read): Open and extract the raw text
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            text_content = file.read()
    except Exception as e:
        print(f"Failed to read the input file: {e}")
        return

    # 3. Regular Expressions (re): Define the pattern and find all matches
    # This pattern looks for: [characters] @ [characters] . [2+ characters]
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    extracted_emails = re.findall(email_pattern, text_content)

    # Clean the data: Convert to a set to remove duplicates, then back to a sorted list
    unique_emails = sorted(list(set(extracted_emails)))

    if not unique_emails:
        print("Task finished: No email addresses were found in the document.")
        return

    # 4. File Handling (Write): Save the extracted emails to a new file
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(f"Found {len(unique_emails)} Unique Email Addresses:\n")
            file.write("=" * 35 + "\n")
            for email in unique_emails:
                file.write(email + "\n")
                
        print(f"Success! Extracted {len(unique_emails)} unique email(s).")
        print(f"Results cleanly saved to '{output_filename}'.")
        
    except Exception as e:
        print(f"Failed to save the output file: {e}")

# Run the automation script
if __name__ == "__main__":
    # To test this, you will need a file named 'raw_data.txt' in the same folder.
    extract_emails("raw_data.txt", "cleaned_emails.txt")