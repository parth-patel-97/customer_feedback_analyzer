def generate_feedback_analysis_prompt(reviews):
    """
    Generate a feedback analysis prompt from a list of reviews.

    Parameters:
    reviews (list): A list of dictionaries, each containing 'feedback' and 'datetime' keys.

    Returns:
    str: A formatted prompt for LLM analysis.
    """
    prompt = "You are an intelligent feedback analysis tool. Analyze the following customer reviews and provide a summary of key themes, sentiments, and actionable suggestions for improvement.\n\nHere are the reviews:\n"

    for i, review in enumerate(reviews, start=1):
        prompt += f"{i}. Review at {review['datetime']}: \"{review['feedback']}\"\n"

    prompt += "Please provide a concise summary and specific suggestions based on the reviews above. Respond in a json format: {\"key_themes\": [], \"overall_sentiment\": \"\", \"sentiment_explanation\": \"\", \"actionable_suggestions\": [{\"suggestion\": \"\", \"reasoning\": \"\"}]}.\n\n"
    return prompt