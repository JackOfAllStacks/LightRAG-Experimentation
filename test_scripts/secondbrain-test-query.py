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

WORKING_DIR = "../initialTesting_files/obsidianbrain-output"


if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete  # Use gpt_4o_mini_complete LLM model
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)

# Define the folder path
folder_path = "../initialTesting_files/Sources/secondbrain-source"  # replace with your folder path

# Perform naive search
print(rag.query("What are some lessons you think Jack could benefit from learning?", param=QueryParam(mode="naive")))

# Perform local search
print(rag.query("What are some lessons you think Jack could benefit from learning?", param=QueryParam(mode="local")))

# Perform global search
print(rag.query("What are some lessons you think Jack could benefit from learning?", param=QueryParam(mode="global")))

# Perform hybrid search
print(rag.query("What are some lessons you think Jack could benefit from learning?", param=QueryParam(mode="hybrid")))