def format_strings(*args):
    # Your implementation here
    text_strings = ''.join(args) 
    upper_string = text_strings.upper()
    format_strings = upper_string.replace(' ', '-')
    return format_strings
    

if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"