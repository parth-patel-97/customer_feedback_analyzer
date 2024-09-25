from pydantic import BaseModel
from typing import List
import re
from llama_index.core.program import LLMTextCompletionProgram
from llama_index.core.output_parsers import PydanticOutputParser



class ActionableSuggestion(BaseModel):
    """Data model for an actionable suggestion."""

    suggestion: str
    reasoning: str

class FeedbackAnalysis(BaseModel):
    """Data model for an analysis."""

    key_themes: List[str]
    overall_sentiment: str
    sentiment_explanation : str
    actionable_suggestions: List[ActionableSuggestion]

# Create the parser
feedback_parser = PydanticOutputParser(FeedbackAnalysis)