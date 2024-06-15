# ChatGPT Functionality Testing with Python and Playwright

This repository contains code and instructions for testing basic functionalities of ChatGPT using Python and Playwright. The tests include logging in, exchanging text messages, uploading an image, and receiving responses.

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Folder Structure](#folder-structure)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
    - [Running Tests](#running-tests)
6. [Implementation Plan](#implementation-plan)
7. [Challenges and Observations](#challenges-and-observations)
8. [GitHub Copilot Testing](#github-copilot-testing)

## Problem Statement

### Test Basic Functionality of ChatGPT using Python and Playwright
1. Create a test plan for basic functionality of login and text-based exchanges.
2. Implement the code to test the functionality to login, send two text messages, and get the response back followed by a logout.
3. Implement the code to test the functionality to login, upload an image, ask ChatGPT to describe the image, and get the response back followed by a logout.

### Testing GitHub Copilot on Visual Studio Code
- Develop an implementation plan for testing GitHub Copilot on Visual Studio Code.

## Folder Structure
- **Codegen Attempt**: Contains code generated using the Codegen tool.
  - `image_check.py`
  - `two_question.py`
- **Modular Code**: Contains modular and well-structured code.
  - `config.py`
  - `test_img.py`
  - `test_two_message.py`
  - `.env` (Contains environment variables like credentials)
- **Test Plan**: Contains the test plan for the basic functionality.
  - `test-plan.txt`

## Prerequisites
Ensure that Python and Playwright are installed. Run the following commands to install the required packages:
```bash
pip install playwright pytest python-dotenv
playwright install
```
## Create .env file
```bash
cp .env.template .env
```

## Installation
Clone this repository and navigate to the project directory. Ensure you have the prerequisites installed.

## Usage

### Running Tests
To execute the tests, use the following commands:

For the code generated using the Codegen tool:
```bash
pytest Codegen Attempt/image_check.py --browser firefox
pytest Codegen Attempt/two_question.py --browser firefox
```

For the modular code:
```bash
pytest test_two_message.py --browser firefox
pytest test_img.py --browser firefox
```

## Implementation Plan
### Problem 1: Basic Functionality Testing of ChatGPT

1. **Test Plan**: Located in `test-plan.txt` under the root directory.
2. **Modular Code Explanation**:
   - `config.py`: Contains essential functions like login, send message, upload file, and logout.
   - `.env`: Stores credentials to keep them separate and secure.
   - `test_two_message.py`: Tests the functionality to login, send two text messages, and logout.
   - `test_img.py`: Tests the functionality to login, upload an image, ask ChatGPT to describe the image, and logout.

## Challenges and Observations
- The code generated using the Codegen tool is often untidy and difficult to read.
- Modular code is better structured, more reusable, and adheres to good coding practices.
- The Codegen tool has limitations, such as being unable to verify UI elements' presence.
- Playwright's syntax differs from Selenium, requiring time and effort to learn.

## GitHub Copilot Testing

### Manual Testing Plan
1. **Code Suggestions**: Verify if Copilot suggests useful code samples based on existing files.
2. **Code Completion**: Ensure Copilot generates accurate code snippets to improve efficiency.
3. **Code Refactoring Suggestions**: Check if Copilot provides meaningful code improvement suggestions.
4. **Error Detection and Fixes**: Test Copilot's ability to detect and suggest fixes for common errors.

### Challenges
- Playwright and Selenium cannot test desktop applications.
- The web version of VS Code does not support the GitHub Copilot extension, necessitating manual testing.

## Browser-Specific Commands
To run tests in a specific browser (e.g., Firefox), use the following commands:
```bash
pytest test_two_message.py --browser firefox
pytest test_img.py --browser firefox
```

Ensure all prerequisites are installed to avoid errors.

---

By following the above instructions, you can effectively test the basic functionalities of ChatGPT and evaluate GitHub Copilot on Visual Studio Code.
