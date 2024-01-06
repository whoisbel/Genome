from .extract import extract_python_code_from_html, extract_html_tags, extract_python_loops_from_html
from .run import run
from .template import Template
from sys import argv

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error opening the file: {e}")
        return None

def main():
    if len(argv) != 2:
        print("Usage: genome <file_name>")
        return

    file_name = argv[1]
    content = read_file(file_name)

    if content is not None:
        # Extract the content inside curly braces
        curly_braces_content = extract_python_code_from_html(content)
        loops_conditionals_content = extract_python_loops_from_html(content)
        # Extract everything except the main block
        html_content = extract_html_tags(content)
        # Run the main block
        main_result = run(curly_braces_content[0])
        # Run the loops inside curly braces and store the results in a list
        loops_conditionals_result = [run(loop, main_result) for loop in loops_conditionals_content]
        # Run the remaining contents inside curly braces and store in a list
        expression_results = [run(expr, main_result) for expr in curly_braces_content[1:]]
        # Initialize the Template
        final_template = Template(curly_braces_content[1:], expression_results, html_content[0], loops_conditionals_content, loops_conditionals_result, file_name)
        final_template.replace_loop_conditionals()
        final_template.replace_curly()
if __name__ == "__main__":
    main()
