import os
import argparse
from read.markdown_reader import read_file
from metrics.links import analyze_links
from metrics.units import analyse_text
from core.analysis_manager import AnalysisManager
from reporting.report_manager import ReportGenerator

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Analyze Markdown files.")
    parser.add_argument("--dir", default="./", help="The directory to search for Markdown files.")
    args = parser.parse_args()
    
    # Use environment variables to configure analyzers and output format
    # Set these in your action.yml or accept the defaults below
    analyzers = os.getenv("ANALYZERS", "links,text").split(",")
    output_format = os.getenv("OUTPUT_FORMAT", "text")
    
    analysis_manager = AnalysisManager()
    report_generator = ReportGenerator(output_format=output_format)

    # Register analyzers based on environment variable
    if "links" in analyzers:
        analysis_manager.register_analyzer(analyze_links)
    if "text" in analyzers:
        analysis_manager.register_analyzer(analyse_text)

    # Loop through the directory to find .md files
    for root, dirs, files in os.walk(args.dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # Read the markdown file
                content = read_file(file_path)
                
                # Analyze the content with all registered analyzers
                metrics = analysis_manager.analyse(content)

                # Add metrics to the report
                report_generator.add_metrics(file_path, metrics)
    
    # Generate the final report
    report_generator.generate()

if __name__ == "__main__":
    main()

# 