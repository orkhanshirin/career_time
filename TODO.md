# TODO:

* Add Support for Multiple Profiles:
    - Parse multiple LinkedIn profile URLs from input_urls.txt.
    - Dynamically load corresponding *.json files from a data/profiles/ directory.
    - Aggregate experience calculations for all talents and output a single JSON array.

* Enhanced Error Handling:
    - Add more robust error messages if data/profile.json files are missing or malformed.
    - Handle unexpected duration formats gracefully (e.g., if duration is not in "X years Y months" format).

* Testing:
    - Introduce unit tests for experience.py, data_providers.py, and main.py.
    - Add integration tests for multi-profile parsing.

* Command-Line Arguments:
    - Add command-line arguments to specify input directories, input URLs file, and output files.

* Logging:
    - Implement a logging mechanism to track runtime operations and debug issues.

* Documentation:
    - Expand README.md with clearer instructions and examples.
    - Add docstrings to all functions and modules for better maintainability.