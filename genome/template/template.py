from os import makedirs, path
from bs4 import BeautifulSoup
class Template:
    def __init__(self, expressions, expression_result, html_content, loops_conditionals, loops_conditionals_result, file_name):
        self.expressions = expressions
        self.expression_result = expression_result
        self.html_content = html_content
        self.loops_conditionals = loops_conditionals
        self.loops_conditionals_result = loops_conditionals_result
        self.file_name = file_name

    def replace_tokens(self, tokens, results):
        for token, result in zip(tokens, results):
            self.html_content = self.html_content.replace(f"{{{token}}}", str(result))

    def replace_curly(self):
        self.replace_tokens(self.expressions, self.expression_result)
        self.write_to_file()

    def replace_loop_conditionals(self):
        self.replace_tokens(self.loops_conditionals, self.loops_conditionals_result)
        self.write_to_file()

    def write_to_file(self):
        dist_directory = 'dist'
        makedirs(dist_directory, exist_ok=True)

        with open(path.join(dist_directory, self.file_name), "w+") as file:
            file.write("<!DOCTYPE html>\n")
            file.write(self.prettify(self.html_content))

    def prettify(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return soup.prettify()

# Example usage:
# transpiler = Transpiler(["expr1", "expr2"], ["result1", "result2"], "html_content_here", "output_file.html")
# transpiler.replace_curly()
