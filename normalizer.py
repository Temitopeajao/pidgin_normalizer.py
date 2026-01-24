import re
import unicodedata

# PROJECT: Text Normalization Pipeline for Nigerian Pidgin
# AUTHOR: Temitope Ajao
# PURPOSE: To clean and standardize raw crowdsourced text data 
# before feeding it into the LLM for training.

class PidginNormalizer:
    def __init__(self):
        """
        Initialize the regex patterns for common Nigerian SMS/Pidgin shorthand.
        """
        self.slang_map = {
            r"\bu\b": "you",          # u -> you
            r"\bd\b": "the",          # d -> the
            r"\babeg+\b": "abeg",     # Handles 'abeg', 'abegg', 'abeggg'
            r"\bwetin\b": "wetin",    # Enforce standard spelling
            r"\bna\b": "na",          # Keep particle 'na'
            r"\bdey\b": "dey",        # Keep particle 'dey'
            r"\bshaa+\b": "sha",      # shaa -> sha
            r"\babi\b": "abi",
            r"\bsef\b": "sef",
            r"\bwe\b": "we",
            r"\bam\b": "am"
        }

    def remove_accents(self, text):
        """
        Removes diacritics/accents to ensure ASCII compatibility.
        """
        text = unicodedata.normalize('NFKD', text)
        return "".join([c for c in text if not unicodedata.combining(c)])

    def clean_whitespace(self, text):
        """
        Removes extra spaces, tabs, and newlines.
        Example: "Wetin    be   dis" -> "Wetin be dis"
        """
        return re.sub(r'\s+', ' ', text).strip()

    def expand_shorthand(self, text):
        """
        Standardizes specific Pidgin/SMS variations using Regex.
        Example: "I beg u" -> "I beg you"
        """
        for pattern, replacement in self.slang_map.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text

    def remove_special_chars(self, text):
        """
        Removes noisy characters but keeps basic punctuation needed for context.
        """
        # Remove anything that isn't alphanumeric or basic punctuation
        return re.sub(r'[^a-zA-Z0-9\s.,!?\'"-]', '', text)

    def normalize(self, text):
        """
        The main pipeline function.
        Run this on every row of your dataset.
        """
        if not isinstance(text, str):
            return ""
            
        text = text.lower()  # Lowercase first
        text = self.remove_accents(text)
        text = self.remove_special_chars(text)
        text = self.expand_shorthand(text)
        text = self.clean_whitespace(text)
        return text

# --- EXECUTION & TESTING ---
if __name__ == "__main__":
    # Test Data: Matches the examples in your README
    raw_inputs = [
        "Abeggg help me  check d  time!",
        "U dey go  market 2day???",
        "Wetin    be   dis one  shaa..",
        "Na so e be o."
    ]

    cleaner = PidginNormalizer()

    print(f"{'RAW INPUT':<35} | {'NORMALIZED OUTPUT'}")
    print("-" * 60)
    
    for raw in raw_inputs:
        clean = cleaner.normalize(raw)
        print(f"{raw:<35} | {clean}")
