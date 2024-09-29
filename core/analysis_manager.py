class AnalysisManager:
    
    def __init__(self):
        self.analyzers = []

    def register_analyzer(self, analyzer):
        self.analyzers.append(analyzer)

    def analyse(self, content):
        all_metrics = {}
        for analyzer in self.analyzers:
            metrics = analyzer(content)
            all_metrics.update(metrics)
        return all_metrics
