
#import packages
import os
from dotenv import load_dotenv, find_dotenv

#load environment and try to fing the .env file
def load_env():
    dotenv_path = find_dotenv()
    #print(f"Loading .env from: {dotenv_path}")  # Debugging: Check if .env is found
    if not dotenv_path:
        print("⚠️ .env file not found!")
    else:
        load_dotenv(dotenv_path, override=True)
#get the openAi key from the .env file and return it to the calling function in the main file
def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    #if openai_api_key:
        #print(f"✅ API Key Loaded: {openai_api_key}")
    #else:
        #print("⚠️ OPENAI_API_KEY not found or not loaded!")

    return openai_api_key

# Test function
#get_openai_api_key()
