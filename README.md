# Genome

Genome is a Python templating engine designed for creating dynamic and personalized interfaces with embedded Python code in HTML templates.

## Installation

You can install Genome using pip:

```bash
pip3 install git+https://github.com/whoisbel/Genome.git
```

## Usage

Genome offers a command-line interface for quick template rendering:

```bash
genome template.html
```

# Getting Started

NOTE: When rendering HTML in a multi-line code block, use print. Genome will automatically render this with the proper value. Genome uses eval for single-line code and exec for multi-line code blocks.
## Example 1 - single line
```
{f"<h1>Hello, {name}</h1>"}
<!-- Is this same as -->
<h1>Hello, {name}</h1>
```
Output:
```
<h1>Hello, John Doe</h1>
```
## Example 2 - multi-line
```
{
if password == 'admin123':
    print("<h1>Correct password!</h1>")
else:
    print("<h1>Incorrect password!</h1>")
}
```
Output:
```
<h1>Correct password!</h1>
<!-- or -->
<h1>Incorrect password!</h1>
```
NOTE: When defining new variables, functions, or adding new imports, always put them in the main block.
## Basic example
```
{
# This is the main block
# You put the variables, functions, and imports in this part.
# for example we set the title
title = "First Genome Project"

}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    
</body>
</html>
```
Output
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Genome Project</title>
</head>
<body>
    
</body>
</html>
```
## Conditional statements

### Ternary conditional expression
```
{
# This is the main block
# You put the variables, functions, and imports in this part.
# for example we set the title
title = ""
}
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title if title else "No title"}</title>
</head>
<body>

</body>
</html>
```
Output
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No title</title>
</head>
<body>

</body>
</html>
```
### If-Else conditions
```
{
# This is the main block
# You put the variables, functions, and imports in this part.
# for example we set the title

title = "First Genome Project"
name = "John Doe"

}
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title if title else "No title"}</title>
</head>
<body>
{
if name == "John Doe":
    print(f"<h1>Hello, {name}. Welcome back!</h1>")
else:
    print("<h1>You are not John Doe</h1>")
}
</body>
</html>
```
Output
```
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   First Genome Project
  </title>
 </head>
 <body>
  <h1>
   Hello, John Doe. Welcome back!
  </h1>
 </body>
</html>
```
## Loops
Looping in genome is just like how you do loops in your python projects.

### For loop
```
{
# This is the main block
# You put the variables, functions, and imports in this part.
# for example we set the title

title = "First Genome Project"
hobbies = ["Reading", "Writing", "Painting"]
}
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title if title else "No title"}</title>
</head>
<body>
    <h1>My hobbies are</h1>
    <ul>
{
for hobby in hobbies:
    print(f"<li>{hobby}</li>")
}
    </ul>
</body>
</html>
```
Output:
```
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   First Genome Project
  </title>
 </head>
 <body>
  <h1>
   My hobbies are
  </h1>
  <ul>
   <li>
    Reading
   </li>
   <li>
    Writing
   </li>
   <li>
    Painting
   </li>
  </ul>
 </body>
</html>
```
### While loop
```
{
# This is the main block
# You put the variables, functions, and imports in this part.
# for example we set the title

title = "First Genome Project"
hobbies = ["Reading", "Writing", "Painting"]
index = 0
}
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title if title else "No title"}</title>
</head>
<body>
    <h1>My hobbies are</h1>
    <ul>
{
while index < len(hobbies):
    print(f"<li>{hobbies[index]}</li>")
    index += 1
}
    </ul>
</body>
</html>
```

## Functions and Imports

### Imports

```
{
import requests
}
```
### Functions

```
{
def func():
    return "Hello World"
}
<h1>{func()}</h1>
```
Output:
```
<h1>Hello World</h1>
```
Another example doing both importing and making functions
```
{
# This is the main block
# You put the variables, functions, and imports in this part.
# for example we set the title
import requests


title = "First Genome Project"
url = 'https://jsonplaceholder.typicode.com/todos/1'

def get_data(url):
    req = requests.get(url)
    data = req.json()
    return data

data_from_api = get_data(url)
}
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title if title else "No title"}</title>
</head>
<body>
{
for key, value in data_from_api.items():
    print(f"<h1 id=\"{key}\">{value}</h1>")
}
</body>
</html>
```
Output:
```
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   First Genome Project
  </title>
 </head>
 <body>
  <h1 id="userId">
   1
  </h1>
  <h1 id="id">
   1
  </h1>
  <h1 id="title">
   delectus aut autem
  </h1>
  <h1 id="completed">
   False
  </h1>
 </body>
</html>
```