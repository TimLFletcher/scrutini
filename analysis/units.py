import re
import os
import textstat
import statistics  # For calculating variance and standard deviation

class TextStatisticsAnalyzer:
    def __init__(self):
        # A list to store report data for all files analyzed
        self.report_data = []

    def analyze(self, file_path, content):
        """Analyze the content of a file and store statistics."""
        word_count = self.get_word_count(content)
        words_per_sentence = self.get_words_per_sentence(content)
        avg_word_length = self.get_average_word_length(content)
        flesch_kincaid_grade = self.get_flesch_kincaid_grade(content)
        flesch_reading_ease = self.get_flesch_reading_ease(content)

        # Store the report for this file
        self.report_data.append({
            "file_path": file_path,
            "file_name": os.path.basename(file_path),
            "word_count": word_count,
            "words_per_sentence": words_per_sentence,
            "average_word_length": avg_word_length,
            "flesch_reading_ease": flesch_reading_ease
        })

    def get_word_count(self, content):
        """Return the number of words in the content."""
        words = re.findall(r'\b\w+\b', content)
        return len(words)

    def get_words_per_sentence(self, content):
        """Return the average number of words per sentence."""
        sentences = re.split(r'[.!?]', content)
        sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty sentences
        word_count = self.get_word_count(content)
        return word_count / len(sentences) if sentences else 0

    def get_average_word_length(self, content):
        """Return the average length of each word in the content."""
        words = re.findall(r'\b\w+\b', content)
        if words:
            return sum(len(word) for word in words) / len(words)
        return 0

    def get_flesch_kincaid_grade(self, content):
        """Return the Flesch-Kincaid grade level of the content."""
        return textstat.flesch_kincaid_grade(content)

    def get_flesch_reading_ease(self, content):
        """Return the Flesch-Kincaid grade level of the content."""
        return textstat.flesch_reading_ease(content)

    def get_report(self):
        """Return the internal report for all analyzed files."""
        return self.report_data

    def print_report(self):
        """Print the report in a readable format."""
        for entry in self.report_data:
            print(f"File: {entry['file_name']}")
            print(f"  Path: {entry['file_path']}")
            print(f"  Word Count: {entry['word_count']}")
            print(f"  Words per Sentence: {entry['words_per_sentence']:.2f}")
            print(f"  Average Word Length: {entry['average_word_length']:.2f}")
            print(f"  Flesch-Kincaid Grade: {entry['flesch_reading_ease']:.2f}")
            print()

    def print_summary(self):
        """Print the summary with mean, standard deviation, min, and max values."""
        
        if not self.report_data:
            print("No data to summarize.")
            return

        # Extract statistics from report_data
        word_counts = [entry['word_count'] for entry in self.report_data]
        words_per_sentence = [entry['words_per_sentence'] for entry in self.report_data]
        avg_word_lengths = [entry['average_word_length'] for entry in self.report_data]
        flesch_reading_eases = [entry['flesch_reading_ease'] for entry in self.report_data]

        # Calculate mean, standard deviation, min, and max for each stat
        def calculate_statistics(data):
            return {
                "mean": statistics.mean(data),
                "std_dev": statistics.stdev(data) if len(data) > 1 else 0,
                "min": min(data),
                "max": max(data)
            }

        word_count_stats = calculate_statistics(word_counts)
        words_per_sentence_stats = calculate_statistics(words_per_sentence)
        avg_word_length_stats = calculate_statistics(avg_word_lengths)
        flesch_reading_ease_stats = calculate_statistics(flesch_reading_eases)

        # Print summary with additional statistics
        print("\nSummary of all files analyzed:")
        
        print("\nWord Count:")
        print(f"  Mean: {word_count_stats['mean']:.2f}")
        print(f"  Std Dev: {word_count_stats['std_dev']:.2f}")
        print(f"  Min: {word_count_stats['min']}")
        print(f"  Max: {word_count_stats['max']}")
        
        print("\nWords per Sentence:")
        print(f"  Mean: {words_per_sentence_stats['mean']:.2f}")
        print(f"  Std Dev: {words_per_sentence_stats['std_dev']:.2f}")
        print(f"  Min: {words_per_sentence_stats['min']:.2f}")
        print(f"  Max: {words_per_sentence_stats['max']:.2f}")

        print("\nAverage Word Length:")
        print(f"  Mean: {avg_word_length_stats['mean']:.2f}")
        print(f"  Std Dev: {avg_word_length_stats['std_dev']:.2f}")
        print(f"  Min: {avg_word_length_stats['min']:.2f}")
        print(f"  Max: {avg_word_length_stats['max']:.2f}")

        print("\nFlesch-Reading Ease:")
        print(f"  Mean: {flesch_reading_ease_stats['mean']:.2f}")
        print(f"  Std Dev: {flesch_reading_ease_stats['std_dev']:.2f}")
        print(f"  Min: {flesch_reading_ease_stats['min']:.2f}")
        print(f"  Max: {flesch_reading_ease_stats['max']:.2f}")
