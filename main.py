import os
import argparse
from read.markdown_reader import read_file
from analysis.units import TextStatisticsAnalyzer
from core.analysis_manager import AnalysisManager


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Analyze Markdown files.")
    parser.add_argument("--dir", default="./", help="The directory to search for Markdown files.")
    args = parser.parse_args()
    
    # Use environment variables to configure analyzers and output format
    # Set these in your action.yml or accept the defaults below
    analyzers = os.getenv("ANALYZERS", "links,text").split(",")
    
    # Set up the analyzer
    analysis_manager = AnalysisManager()

    # Register analyzers based on environment variables
    if "links" in analyzers:
        #analysis_manager.register_analyzer(analyze_links)
        pass
    if "text" in analyzers:
        text_stats_analyzer = TextStatisticsAnalyzer()
        analysis_manager.register_analyzer(text_stats_analyzer.analyze)

    # Loop through the directory to find .md files
    for root, dirs, files in os.walk(args.dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # Read the markdown file
                content = read_file(file_path)
                
                # Analyze the content with all registered analyzers
                metrics = analysis_manager.analyse(file_path, content)
                #print(metrics)

    
    # Generate the final report
    text_stats_analyzer.print_report()
    text_stats_analyzer.print_summary()


if __name__ == "__main__":
    main()

