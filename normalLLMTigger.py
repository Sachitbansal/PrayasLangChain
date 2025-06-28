#  A library is a broader, more conceptual term. It generally refers to a collection of related packages and modules (or sometimes just modules) that provide a set of functionalities for a specific purpose.


# modules are Python files that contain reusable code
# package is folder/collection of modules

# langchain is a library here which as chains as another folder which contains LLMChain module

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate # Standard way to import PromptTemplate
from dotenv import load_dotenv

load_dotenv() # Load GOOGLE_API_KEY from .env

def get_simple_joke(topic: str) -> str:

    # 1. Initialize the LLM (Gemini)
    # This is an instance of a Language Model
    llm = GoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17", # Using a general-purpose Gemini model
        temperature=0.7    # A bit higher temperature for creativity in jokes
    )

    # 2. Define the Prompt Template
    # We use .from_template() which is concise and handles variable parsing.
    # This is an instance of PromptTemplate
    prompt_template = PromptTemplate.from_template(
        "Tell me a short, funny joke about {topic}. Keep it to one or two sentences."
    )

    # 3. Create a simple chain
    # The '|' operator connects the prompt template to the LLM. It has been overridden by langchain from its conventional use in python
    # core part of LangChain Expression Language (LCEL)
    # It means: "take the output of the component on the left and feed it as the input to the component on the right."
    chain = prompt_template | llm

    # 4. Invoke the chain with the input data
    print(f"Asking Gemini for a joke about: {topic}...")
    response = chain.invoke({"topic": topic})
    

    return response

# only run when the script is executed directly, and not when it's imported as a module into another script.
# __name__ is built-in variable in Python that depends on how the script is executed.
if __name__ == "__main__":
    # Example usage
    joke_topic = "computers"
    joke = get_simple_joke(joke_topic)
    print("\n--- Gemini's Joke ---")
    print(joke)




# show experimentation with different prompts and how can we control the llm