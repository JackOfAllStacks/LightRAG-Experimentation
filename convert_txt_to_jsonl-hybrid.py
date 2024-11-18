import os
import json
import re

input_directory = "./working_sources/ANZSampleData-source"  # Update with your actual directory path
output_directory = "./working_sources/ANZProcessed-hybrid"  # Where the converted JSONL files will be saved

os.makedirs(output_directory, exist_ok=True)

# Use os.walk to iterate through all subdirectories and files
for root, _, files in os.walk(input_directory):
    for filename in files:
        if filename.endswith(".txt"):
            txt_file_path = os.path.join(root, filename)

            # Create an appropriate output path maintaining subfolder structure
            relative_path = os.path.relpath(root, input_directory)
            output_folder_path = os.path.join(output_directory, relative_path)
            os.makedirs(output_folder_path, exist_ok=True)
            jsonl_file_path = os.path.join(output_folder_path, filename.replace(".txt", ".jsonl"))

            sections = []
            current_paragraph = []
            current_section_title = None

            with open(txt_file_path, "r", encoding="utf-8") as txt_file:
                for line in txt_file:
                    line = line.strip()

                    # Check if the line seems like a header
                    if re.match(r"^[A-Z\s]+$|^.*Release.*|.*announcement.*|.*contact.*", line, re.IGNORECASE):
                        # Save the previous paragraph if it exists
                        if current_paragraph:
                            context = " ".join(current_paragraph)
                            sections.append(context)
                            current_paragraph = []

                        # Set the current line as a new header/section title
                        current_section_title = line

                    elif line:
                        # Add lines to the current paragraph
                        current_paragraph.append(line)
                    else:
                        # If an empty line is encountered, end the current paragraph
                        if current_paragraph:
                            context = " ".join(current_paragraph)
                            sections.append(context)
                            current_paragraph = []
                            current_section_title = None  # Reset to General after paragraph ends

                # If there is any remaining paragraph, write it out
                if current_paragraph:
                    context = " ".join(current_paragraph)
                    sections.append(context)

            # Write all sections to JSONL file with only "context" key
            with open(jsonl_file_path, "w", encoding="utf-8") as jsonl_file:
                for context in sections:
                    json_obj = {"context": context}
                    jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + "\n")

            print(f"Converted {txt_file_path} to {jsonl_file_path} with simplified context")

print("All files have been processed.")