# core/analysis_manager.py

class AnalysisManager:
    def __init__(self):
        self.analyzers = []

    def register_analyzer(self, analyzer):
        """Register an analyzer function or class."""
        self.analyzers.append(analyzer)

    def analyse(self, file_path, content):
        """Run all registered analyzers and collect their results."""

        for analyzer in self.analyzers:
            # Now passing both file_path and content to the analyzer
            metrics = analyzer(file_path, content)

