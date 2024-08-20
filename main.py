import tempfile
from typing import Any, Dict

from repoinsight import analyze_code, clone_code, extract_code, generate_readme


def analyze_repository(repo_url: str, config: Dict[str, Any]) -> None:
    """
    Analyze a git repository, extract its code, and generate a README file.

    This function performs the following steps:
    1. Clones the repository to a temporary directory.
    2. Extracts the code from the cloned repository.
    3. Analyzes the extracted code.
    4. Generates a README file based on the analysis.
    5. Saves the generated README file in the current working directory.

    Args:
        repo_url (str): The URL of the git repository to analyze.
        config (Dict[str, Any]): A dictionary containing configuration parameters.

    Raises:
        ValueError: If there's an error during the repository analysis process.
        IOError: If there's an error writing the README file.

    Note:
        The generated README.md file will be saved in the current working directory.
    """
    print("Starting repository analysis...")

    try:
        # Use a temporary directory for cloning and analysis
        with tempfile.TemporaryDirectory():
            # Step 1: Clone the repository
            print("Cloning repository...")
            repo_dir = clone_code(repo_url)

            # Step 2: Extract code from the cloned repository
            print("Extracting code...")
            code_index, code_text = extract_code(repo_dir)

            # Step 3: Analyze the extracted code
            print("Analyzing code...")
            codebase_analysis = analyze_code(code_index, code_text)

            # Step 4: Generate README based on the analysis
            print("Generating README...")
            readme_content = generate_readme(codebase_analysis)

            # Step 5: Save the generated README
            print("Saving README...")
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(readme_content)

        print("README.md has been generated and saved in the current directory.")

    except Exception as e:
        # Handle any exceptions that occur during the process
        error_msg = f"An error occurred during repository analysis: {str(e)}"
        print(error_msg)
        raise ValueError(error_msg)
