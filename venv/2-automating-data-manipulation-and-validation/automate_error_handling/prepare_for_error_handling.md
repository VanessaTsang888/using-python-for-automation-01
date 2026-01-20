# prepare_for_error_handling

Prepare for error handling because:

1. Enhances the robustness of the programs we develop.
2. Improves user interaction with our programs.
3. Makes debugging more efficient.

Three most common categories of errors we might encounter in Python programs:

1. Syntax Errors: These occur when the code violates Python language rules.
2. Runtime Errors: Unexpected conditions during execution that halt the program. Example:
   - NameError: Using an undefined variable.
   - TypeError: Mismatched data type operation.
   - IndexError: Out-of-range sequence index.
   - AttributeError: Invalid object/method.
   - ValueError: Incorrect argument value.
   - ZeroDivisonError: Division by zero.
3. Logical Errors: Code runs smoothly but yields incorrect outcomes due to flowed reasoning. Example, a 'for-loop' that iterate through the wrong range.
4. Assert Statements: A debuging tool used to validate specific conditions during code execution, aiding in the detection and management of logical errors.

Error handling is a crucial aspect of programming and acquiring techniques for detecting and handling errors will help you take your Python skills to the next level.

There are three major reasons why this is an important process. First, it enhances the robustness of the programs you develop. It ensures that unexpected situations like invalid inputs or unexpected data are handled gracefully rather than causing a program to crash. Second, it improves the experience of users who will use the programs you build. Instead of encountering cryptic error messages, users can receive informative feedback making your application more user-friendly. Third, it makes debugging more efficient. When errors occur, the program can provide detailed information about the issue, helping you identify and fix the issues quickly. Also, it's helpful to keep in mind the three most common categories of errors you might encounter in Python programs.

<mark>First</mark> are syntax errors. These occur when the code violates Python language rules, for example, a missing colon at the end of an if condition.
<br />
<mark>Second</mark>, are runtime errors, also known as exceptions. These occur when the program is executing and encounters an unexpected condition that prevents it from continuing. Examples include referring to a variable before defining it, name error, applying an operation or function to the wrong type of data type error. Accessing an index out of a sequence that's out of range. Index error, accessing an attribute or method of an object that does not exist or is not defined for that object. Attribute error, calling a function with a proper argument type, but with the wrong value. Value error, and trying to divide a number by zero, zeroDivisioError.
<br />
<mark>Third</mark>, are logical errors. These occur when the code runs without any syntax or runtime errors, but produces incorrect results due to flawed logic in the code. For example, a for loop that iterates over the wrong range. **_Error handling and python is often done using Try accept blocks_**, which allow you to catch and handle exceptions that might otherwise cause your program to crash or behave unpredictably.

Another technique for error handling involves creating cert statements. An cert statement can often be used as a debugging tool. It's especially helpful in detecting logical errors based on specific conditions that you check for.

Now that you've gotten a conceptual overview of the importance of error handling, the common types of errors to look out for and techniques for error handling, you're ready to dive into implementation in Python.
