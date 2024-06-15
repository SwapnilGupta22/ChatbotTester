Problem Statement:
Test Basic Functionality of ChatGPT using Python and Playwright-
1. Create a test plan for basic functionality of login and text based exchanges.
2. Implement the code to test the functionality to login, sned two text mesasges and get the response back followed by a logout.
3. Implement the code to test the functionality to login, upload an image, ask ChatGPT to Describe theimage and get the response back followed by a logout.

Come up with an implementation plan for testing Github Copilot on Visual Studio Code.

Outlining some challenges mentioned in my attempt to execute the implementation.

Starting with Problem 1:

Inside this repo, under the folder "Codegen Attempt" you will find 2 types of python files.
image_check.py and two_question.py
These codes were generated using the code gen tool.
To execute these files,
Ensure that Playwright and Python are installed.

>> pip install playwright pytest python-dotenv
>> playwright install

>> pytest image_check.py --browser firefox
>> pytest two_question.py --browser firefox

On the other hand, you will find config.py; test_img.py; test_two_message.py and .env files are creating a modular code structure.

Before I explain my code, I would like to inform you that Problem 1, part 1 is added in the repo under "test-plan.txt".

config.py is the file under which most of the important functions of a code have been written and added. This file consists of Login, Send Message, Upload File, and Logout methods inside them, which can be called in any file as per the requirements.
.env file includes the credentials in a separate file which we can set to be hidden if needed and configured to be customizable without modifying the main code files.

Part 2 is named test_two_message.py
Part 3 is named test_img.py

Coming to the Challenges and Observations throughout this assessment, I noticed that the code is very untidy and not easy to read for the script generated using the Codegen tool.
The modular code created is a much better representation of the standards of good coding practice increasing the reusability and ease of understanding.

The codegen tool had some clear limitations which had to be manually cleared out to avoid issues. The tool is only capable of Behaviour-based testing which includes clicking of buttons, filling forms/fields of data, etc.
The code cannot verify the presence or the UI parts of the site.

In the case of modular coding, I was able to create multiple scenarios where detecting the presence of an element like the response of GPT or waiting for the Login to successfully happen and load the texting window. In terms of the behavior of locators and how they differ from Selenium, it was a time-consuming task to get accustomed to Playwright and its syntax which required lots of trial and error.

Moving on to Problem 2:
I was unable to come up with a test plan for GIthub CoPilot testing on VScode using automation. Playwright and Selenium are not capable of testing Desktop-based applications. The web-based application of VScode does not allow us to add Github Copilot as an extension.
Due to this, I am sharing only the functional test plan using Manual intervention.

Scenarios, where the Github Copilot extension should be tested and their benefits, are:
1. Code Suggestions - Based on the existing files, copilot suggests a code sample that the user might be able to utilize.
2. Code Completion - Based on the currently created files, copilot generates code snippets which can increase efficiency and reduce human effort.
3. Code Refactoring Suggestion - Based on real-world scenarios, the copilot suggests improvements in certain areas of the code.
4. Error Detection and Fixes - Copilot can help with common errors and minor debugging.


#broswer specific commands:

    pytest test_two_message.py --browser firefox
    pytest test_img.py --browser firefox

#Prerequisites
Run these commands to avoid errors:

pip install playwright pytest python-dotenv
playwright install
