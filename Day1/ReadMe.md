# LLM Trigger - LangChain with Google Gemini

This project demonstrates how to use LangChain with Google's Gemini AI model to generate jokes based on user-specified topics.

## Overview

The `llmTigger.py` file contains a simple implementation that:
- Connects to Google's Gemini AI model
- Uses LangChain's Expression Language (LCEL) to create a chain
- Generates jokes based on user-provided topics
- Demonstrates proper environment variable handling

## Line-by-Line Code Explanation

### Comments and Documentation (Lines 1-6)
```python
#  A library is a broader, more conceptual term. It generally refers to a collection of related packages and modules (or sometimes just modules) that provide a set of functionalities for a specific purpose.

# modules are Python files that contain reusable code
# package is folder/collection of modules

# langchain is a library here which as chains as another folder which contains LLMChain module
```
- **Lines 1-2**: Explains the concept of libraries in programming
- **Line 4**: Defines what a module is in Python
- **Line 5**: Defines what a package is in Python
- **Line 6**: Specific explanation of how LangChain is structured

### Import Statements (Lines 8-11)
```python
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate # Standard way to import PromptTemplate
from dotenv import load_dotenv

load_dotenv() # Load GOOGLE_API_KEY from .env
```
- **Line 8**: Imports the GoogleGenerativeAI class from LangChain's Google GenAI integration
- **Line 9**: Imports PromptTemplate from LangChain core for creating structured prompts
- **Line 10**: Imports load_dotenv function to handle environment variables
- **Line 11**: Loads environment variables from a `.env` file (specifically for GOOGLE_API_KEY)

### Function Definition (Line 13)
```python
def get_simple_joke(topic: str) -> str:
```
- Defines a function named `get_simple_joke`
- Takes a parameter `topic` of type string
- Returns a string value
- Uses type hints for better code documentation

### LLM Initialization (Lines 15-20)
```python
    # 1. Initialize the LLM (Gemini)
    # This is an instance of a Language Model
    llm = GoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17", # Using a general-purpose Gemini model
        temperature=0.7    # A bit higher temperature for creativity in jokes
    )
```
- **Line 15-16**: Comments explaining this step initializes the Language Model
- **Line 17**: Creates an instance of GoogleGenerativeAI
- **Line 18**: Specifies the Gemini model version to use
- **Line 19**: Sets temperature to 0.7 for creative responses (higher values = more random/creative)

### Prompt Template Creation (Lines 22-27)
```python
    # 2. Define the Prompt Template
    # We use .from_template() which is concise and handles variable parsing.
    # This is an instance of PromptTemplate
    prompt_template = PromptTemplate.from_template(
        "Tell me a short, funny joke about {topic}. Keep it to one or two sentences."
    )
```
- **Line 22-24**: Comments explaining the prompt template creation
- **Line 25**: Creates a PromptTemplate using the `from_template()` method
- **Line 26**: Defines the prompt text with a placeholder `{topic}` for variable substitution

### Chain Creation (Lines 29-35)
```python
    # 3. Create a simple chain
    # The '|' operator connects the prompt template to the LLM. It has been overridden by langchain from its conventional use in python
    # core part of LangChain Expression Language (LCEL)
    # It means: "take the output of the component on the left and feed it as the input to the component on the right."
    chain = prompt_template | llm
```
- **Line 29-33**: Comments explaining the chain creation and LCEL concept
- **Line 34**: Creates a chain by connecting the prompt template to the LLM using the `|` operator
- This is the core of LangChain Expression Language (LCEL)

### Chain Execution (Lines 37-40)
```python
    # 4. Invoke the chain with the input data
    print(f"Asking Gemini for a joke about: {topic}...")
    response = chain.invoke({"topic": topic})
    
    return response
```
- **Line 37**: Comment explaining the execution step
- **Line 38**: Prints a status message showing what topic is being processed
- **Line 39**: Invokes the chain with a dictionary containing the topic
- **Line 41**: Returns the generated response

### Main Execution Block (Lines 43-49)
```python
# only run when the script is executed directly, and not when it's imported as a module into another script.
# __name__ is built-in variable in Python that depends on how the script is executed.
if __name__ == "__main__":
    # Example usage
    joke_topic = "computers"
    joke = get_simple_joke(joke_topic)
    print("\n--- Gemini's Joke ---")
    print(joke)
```
- **Line 43-44**: Comments explaining the `__name__` variable and when this block executes
- **Line 45**: Checks if the script is being run directly (not imported)
- **Line 46**: Comment indicating example usage
- **Line 47**: Sets the topic to "computers"
- **Line 48**: Calls the function and stores the result
- **Line 49**: Prints a header for the joke output
- **Line 50**: Prints the generated joke

### Final Comment (Line 52)
```python
# show experimentation with different prompts and how can we control the llm
```
- Indicates future experimentation possibilities with different prompts and LLM control

## Prerequisites

1. **Google API Key**: You need a Google API key for Gemini
2. **Environment Setup**: Create a `.env` file with your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Dependencies

Install the required packages:
```bash
pip install langchain-google-genai langchain-core python-dotenv
```

## Usage

Run the script directly:
```bash
python llmTigger.py
```

Or import and use the function in another script:
```python
from llmTigger import get_simple_joke

joke = get_simple_joke("pizza")
print(joke)
```

## Key Concepts Demonstrated

1. **LangChain Expression Language (LCEL)**: Using the `|` operator to chain components
2. **Prompt Templates**: Structured way to create prompts with variables
3. **Environment Variables**: Secure handling of API keys
4. **Type Hints**: Modern Python code documentation
5. **Modular Design**: Function can be imported and reused

## Expected Output

When run with the topic "computers", you should see output similar to:
```
Asking Gemini for a joke about: computers...

--- Gemini's Joke ---
[Generated joke about computers]
``` 
