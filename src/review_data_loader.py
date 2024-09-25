import pandas as pd

def load_reviews_from_csv(file_path):
    """
    Loads customer reviews from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing reviews.

    Returns:
    list: A list of dictionaries containing 'feedback' and 'datetime' keys.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Ensure the required columns exist
    if 'feedback' not in df.columns or 'datetime' not in df.columns:
        raise ValueError("CSV file must contain 'feedback' and 'datetime' columns.")

    # Convert the DataFrame to a list of dictionaries, ignoring 'user_id'
    reviews = df[['feedback', 'datetime']].to_dict(orient='records')
    return reviews
