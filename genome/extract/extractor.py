from regex import findall, compile, IGNORECASE

def extract_python_code_from_html(html):
    """
    Extracts all code inside curly braces excluding code starting with 'for' or 'while'.

    Parameters:
    - html (str): The input text containing HTML with Python code within curly braces.

    Returns:
    - list: A list of Python code snippets extracted from the input text.
    """
    try:
        pattern = r'\{(?:[^{}]|(?R))*\}'
        matches = findall(pattern, html)

        # Remove extra curly braces from the beginning and end of each match
        cleaned_matches = [match[1:-1] for match in matches]

        # Exclude matches that start with 'for' or 'while'
        filtered_matches = [code for code in cleaned_matches if not code.strip().startswith(('for', 'while','if'))]

        return filtered_matches
    except Exception as e:
        print(f"Error in extract_python_code_from_html: {e}")
        return []

def extract_html_tags(html):
    """
    Extracts HTML tags from the given HTML content.

    Parameters:
    - html (str): The input HTML content.

    Returns:
    - list: A list of HTML tags and their content extracted from the input content.
    """
    try:
        pattern = compile(r'<html\b[^>]*>[\s\S]*?</html>', IGNORECASE)
        html_tags = pattern.findall(html)
        return html_tags
    except Exception as e:
        print(f"Error in extract_html_tags: {e}")
        return []

def extract_python_loops_from_html(html):
    """
    Extracts all code inside curly braces excluding code starting with 'for' or 'while'.

    Parameters:
    - html (str): The input text containing HTML with Python code within curly braces.

    Returns:
    - list: A list of Python code snippets extracted from the input text.
    """
    try:
        pattern = r'\{(?:[^{}]|(?R))*\}'
        matches = findall(pattern, html)

        # Remove extra curly braces from the beginning and end of each match
        cleaned_matches = [match[1:-1] for match in matches]

        # Include matches that start with 'for' or 'while'
        filtered_matches = [code for code in cleaned_matches if code.strip().startswith(('for', 'while','if'))]
        return filtered_matches
    except Exception as e:
        print(f"Error in extract_python_loops_from_html: {e}")
        return []
