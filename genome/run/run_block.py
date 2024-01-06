import importlib
import sys
import io

def run(code, context=None):
    """
    Execute Python code and return the result or local variables.

    Parameters:
    - code (str): The Python code to execute.
    - context (dict, optional): A dictionary representing the context in which the code will run.

    Returns:
    - dict or any: If the code is an expression, returns the result. If the code contains statements,
      returns a dictionary of local variables after execution.
    """
    local_vars = context or {}
    global_vars = {
        "__builtins__": __import__("builtins"),
    }

    try:
        # Check if code is a single line
        is_single_line = '\n' not in code.strip()
        if local_vars and is_single_line:
            result = eval(code, global_vars, local_vars)
            return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

    try:
        # Dynamically import modules based on code content
        import_statements = [stmt.split()[1] for stmt in code.splitlines() if stmt.startswith("import ")]
        from_import_statements = [stmt.split()[1:] for stmt in code.splitlines() if stmt.startswith("from ")]

        for module_name in import_statements:
            global_vars[module_name] = importlib.import_module(module_name)

        for from_import_statement in from_import_statements:
            module_name = from_import_statement[0]
            if len(from_import_statement) > 2 and from_import_statement[1] == "import":
                identifiers = from_import_statement[2:]
                imported_module = importlib.import_module(module_name)
                for identifier in identifiers:
                    global_vars[identifier] = getattr(imported_module, identifier)

        if not is_single_line:
            if code.strip().startswith(('for', 'while', 'if')):
                original_stdout = sys.stdout
                sys.stdout = io.StringIO()
                try:
                    exec(code, global_vars, local_vars)
                finally:
                    # Restore the original stdout
                    captured_output = sys.stdout.getvalue().strip()
                    sys.stdout = original_stdout
                return captured_output
            exec(code, global_vars, local_vars)
    except Exception as e:
        print(f"Error executing code: {e}")
        return None

    values_dict = {
        var: local_vars[var] for var in local_vars
        if not var.startswith("__")  and not isinstance(local_vars[var], type)
    }
    return values_dict
