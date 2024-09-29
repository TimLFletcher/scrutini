# analyse/analyser.py

def analyse_text(content):
    """Analyzes the content of a file and returns metrics."""
    metrics = {
        "word_count": get_word_count(content),
        "heading_count": get_heading_count(content),
        # Add more metrics here as needed
    }
    return metrics

def get_word_count(content):
    """Counts the number of words in the content."""
    return len(content.split())

def get_heading_count(content):
    """Counts the number of headings in the content (Markdown style)."""
    return sum(1 for line in content.splitlines() if line.startswith("#"))
