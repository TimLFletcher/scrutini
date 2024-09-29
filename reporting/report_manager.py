# reports/reporter_manager.py

class ReportGenerator:

    def __init__(self, output_format="text"):
        """Initialize the ReportGenerator with a given output format."""
        self.output_format = output_format  # Store the output format
        self.report_data = []

    def add_metrics(self, file_path, metrics):
        """Add the metrics for a single file to the report data."""
        self.report_data.append({
            "file": file_path,
            "metrics": metrics
        })

    def generate(self):
        """Generate the final report based on the specified output format."""
        if self.output_format == "text":
            self._generate_text_report()
        elif self.output_format == "latex":
            self._generate_latex_report()
        # Add more formats here if needed

    def _generate_text_report(self):
        """Generate a simple text report."""
        print("Metrics Report:")
        for entry in self.report_data:
            print(f"File: {entry['file']}")
            for metric, value in entry['metrics'].items():
                print(f"  {metric}: {value}")
            print("\n")

    def _generate_latex_report(self):
        """Generate a LaTeX report."""
        print("LaTeX Report (Placeholder):")
        # LaTeX report generation logic goes here
