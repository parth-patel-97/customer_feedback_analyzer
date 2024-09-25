from src.review_analyzer import analyze_reviews
from src.review_data_loader import load_reviews_from_csv

if __name__ == "__main__":
    # Specify the path to the CSV file (update with your actual file path)
    csv_file_path = '/home/fx/Downloads/Projects/customer_feedback_analyzer/data/reviews.csv'  # Update this path

    # Load reviews from the CSV file
    try:
        reviews = load_reviews_from_csv(csv_file_path)
        
        # Analyze the reviews
        analysis_result = analyze_reviews(reviews)
        if analysis_result:
            print("Key Themes:", analysis_result.key_themes)
            print("Overall Sentiment:", analysis_result.overall_sentiment)
            print("Sentiment Explanation:", analysis_result.sentiment_explanation)
            print("\nActionable Suggestions:")
            for suggestion in analysis_result.actionable_suggestions:
                print(f"- Suggestion: {suggestion.suggestion}")
                print(f"  Reasoning: {suggestion.reasoning}\n")
        else:
            print("Failed to generate or parse the analysis.")

    except Exception as e:
        print(f"Error loading reviews: {e}")
