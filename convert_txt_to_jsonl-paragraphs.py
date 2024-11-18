import os
import json

input_directory = "./working_sources/ANZSampleData-source"  # Update with your actual directory path
output_directory = "./working_sources/ANZProcessed-paragraphs"  # Where the converted JSONL files will be saved

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

            # Read the .txt file and write grouped paragraphs to .jsonl
            with open(txt_file_path, "r", encoding="utf-8") as txt_file, open(jsonl_file_path, "w", encoding="utf-8") as jsonl_file:
                paragraph = []
                
                for line in txt_file:
                    line = line.strip()
                    if line:
                        # Add non-empty lines to the current paragraph
                        paragraph.append(line)
                    else:
                        # When encountering an empty line, save the current paragraph as a context
                        if paragraph:
                            context = " ".join(paragraph)  # Join lines in the paragraph with a space
                            json_obj = {"context": context}
                            jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
                            paragraph = []  # Reset paragraph

                # Write any remaining paragraph after the loop
                if paragraph:
                    context = " ".join(paragraph)
                    json_obj = {"context": context}
                    jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + "\n")

            print(f"Converted {txt_file_path} to {jsonl_file_path}")

print("All files have been processed.")