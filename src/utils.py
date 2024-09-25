import re
def preprocess_output(output: str) -> str:
    # Try to extract JSON from the output
    json_match = re.search(r'\{.*\}', output, re.DOTALL)
    if json_match:
        return json_match.group(0)
    return output