import os
import glob
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete, gpt_4o_complete

os.environ["OPENAI_API_KEY"] = "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"

#########
# Uncomment the below two lines if running in a jupyter notebook to handle the async nature of rag.insert()
# import nest_asyncio 
# nest_asyncio.apply() 
#########

WORKING_DIR = "../initialTesting_files/ANZDATA-output"


if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete  # Use gpt_4o_mini_complete LLM model
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)

# Define the folder path
folder_path = "../working_sources/ANZSampleData-source"  # replace with your folder path

# Use glob to find all .txt files within the folder and its subfolders
file_paths = glob.glob(os.path.join(folder_path, '**', '*.txt'), recursive=True)

# Check if any files were found
if not file_paths:
    print("No .txt files found in the specified directory and subdirectories.")
else:
    # Loop through each file and read its content
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Processing file: {file_path}")
                print(f"Content preview: {content[:100]}")  # Show the first 100 characters for debugging
                rag.insert(content)
        except UnicodeDecodeError as e:
            print(f"Could not read {file_path} due to encoding error: {e}")

# Perform naive search
# print(rag.query("What are the top themes in this story?", param=QueryParam(mode="naive")))

# Perform local search
# print(rag.query("What are the top themes in this story?", param=QueryParam(mode="local")))

# Perform global search
# print(rag.query("What are the top themes in this story?", param=QueryParam(mode="global")))

# Perform hybrid search
# print(rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid")))