from langchain.tools import tool


@tool #decorator for creating tool 
def get_greeting(name : str) -> str: #type hints
    """Generate a greeting message for a user""" #docstring

    return f"Hello {name}, Welcome to the AI world"


result = get_greeting.invoke({"name":"Subhasish"})
print(result)

print(get_greeting.name)
print(get_greeting.description)
print(get_greeting.args)