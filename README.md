# Interactive Password Generator

This Python script generates random passwords of varying lengths with a mix of uppercase letters, lowercase letters, numbers, and symbols. It allows users to customize the password length and generates passwords interactively until the user decides to exit.

## Features

- Generates a random password based on user-specified length.
- Includes a mix of:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Symbols (e.g., !@#$%^&*())
- Allows users to generate multiple passwords consecutively or exit upon completion.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/interactive-password-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd interactive-password-generator
   ```

## Usage

1. Run the script:

   ```bash
   python password_generator.py
   ```

2. Follow the prompts:
   - Enter the desired password length (minimum 8 characters).
   - The script will generate a password and display it.
   - Choose whether to generate another password or exit.

## Example

Example interaction:

```
Enter password length (default is 8): 12
Generated Password: Df#9XzB4$A1K
Generate another password? (yes/no): yes
Enter password length (default is 8): 10
Generated Password: j7T%L*5fKz
Generate another password? (yes/no): no
```


### Notes:

- Ensure Python 3.x is installed on your system to run the script.
- Customize the character sets or password complexity in the `generate_password` function based on your security requirements.
- Feel free to modify and extend the script to add more features, such as saving generated passwords to a file or integrating with other applications.
