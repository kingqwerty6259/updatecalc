# Math Expression Calculator

## Overview

This is a simple Python script that performs basic mathematical operations on two numbers. It prompts the user to enter a mathematical expression in the form of `number1 operator number2` (e.g., `5 + 3`) and outputs the result. The script supports addition, subtraction, multiplication, and division.

## Requirements

- Python 3.x

## Usage

1. Run the script.
2. Enter a mathematical expression in the format:  
   ```  
   number1 operator number2  
   ```
   Example:
   ```  
   5 + 3  
   ```
3. The program will calculate the result and display it.

4. To exit, type any non-numeric expression or press `Ctrl + C`.

## Supported Operators

- `+` for addition
- `-` for subtraction
- `*` for multiplication
- `/` for division (Note: division by zero is not allowed and will return an error message)

## Code Walkthrough

1. The `math()` function prompts the user to enter an expression.
2. The function checks if the input contains letters (to allow for exiting) or is formatted correctly with an operator and two numbers.
3. It parses the expression, converting numbers to integers or floats as needed.
4. Based on the operator, it performs the corresponding mathematical operation and outputs the result.
5. The script runs continuously in a loop (`while run == True`) until a non-numeric input is entered.

## Example

```bash
Enter expression to calculate: 8 * 2
8 x 2 = 16

Enter expression to calculate: 10 / 0
Can't divide by zero
```

This calculator is ideal for quick, basic calculations in a command-line environment.
