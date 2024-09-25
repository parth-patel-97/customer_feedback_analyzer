import json
from llama_index.llms.gemini import Gemini
from src.prompts import generate_feedback_analysis_prompt
from src.config import load_config
from src.output_parser import feedback_parser

def analyze_reviews(reviews):
    """
    Analyzes customer reviews by generating a response using the Gemini LLM.

    Parameters:
    reviews (list): A list of dictionaries containing 'feedback' and 'datetime' keys.

    Returns:
    str: The generated analysis response.
    """
    # Generate the prompt for the reviews
    prompt = generate_feedback_analysis_prompt(reviews)

    # Generate the response using the Gemini model
    response = Gemini().complete(prompt)

    #Parse the response
    try:
        parsed_output = feedback_parser.parse(response.text.strip())
        return parsed_output
    except Exception as e:
        print(f"Error parsing output: {e}")
        return None
    