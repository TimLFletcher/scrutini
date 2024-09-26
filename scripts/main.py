import os
import sys

def find_markdown_files(directory):
    """
    Recursively find all .md (Markdown) files in the given directory.
    """
    markdown_files = []
    
    # Walk through all directories and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                # Join the root and file name to get the full path
                full_path = os.path.join(root, file)
                markdown_files.append(full_path)

    return markdown_files

def main():
    # Check if a directory argument is provided, otherwise use current directory
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        root_directory = os.getcwd()  # current working directory
    
    # Find all markdown files
    markdown_files = find_markdown_files(root_directory)
    
    # Output the list of Markdown files
    print("\nFound the following Markdown files:")
    for md_file in markdown_files:
        print(md_file)

    # Optionally, save this list to a file for later use
    output_file = os.path.join(root_directory, 'markdown_files_list.txt')
    with open(output_file, 'w') as f:
        for md_file in markdown_files:
            f.write(md_file + "\n")
    
    print(f"\nMarkdown files list saved to {output_file}")

if __name__ == "__main__":
    main()
