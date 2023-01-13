 # Recruiting Automation Using Selenium-Python
 
- The following code structure is used to create automation for Learn JavaScript with HTML testing and HTML testing:
  - Usage of Selenium-Python is used for testing the following website: "https://yorkdevtraining.com/"
  - Purpose of using Selenium-Python is so that we do not have to manually test certain things on a website. All we need to do is run a script and it will test the website to see if the website works or does not work 
  - This helps to make sure your code is functioning correctly without having to manually test each function

## Structure of Test Cases
- Unit test is built into python to create Testcases
- Create a class for the main test cases to perform on the website
- Run this specific class to run all the test cases within this class to determine if the testcases pass or fail
- Create a setUp, before any of the test cases run, the first thing that will run is the setUp
  - setUp includes:
    - Chromedriver 
    - Website Page 
    - Login requirements for the website, Email & Password 
    - Navigating to User Lookup 
    - Searching for User associated with "Bob1@"
    - Navigating to User Profile
    - Opening headers for 'HTML' and 'Learn JavaScript with HTML' so that the iframe is accessible when testing

## Test Case Scenarios

'Learn JavaScript with HTML'
- Access the iframe within the header to make sure test case scenarios run correctly
1. First test case is testing to make sure the user has included all the requirements
2. Second test case is testing a failure when the user does not include a number within the username requirements
3. Third test case is testing a failure when the user includes more than 12 characters which exceeds the username requirements
4. Fourth test case is testing a failure when the user does not include an upper case letter per the username requirements
5. Fifth test case is testing a failure when the user does not meet the minimum requirement of number of characters for username requirements
6. Sixth test case is testing a failure when the user does not enter in anything for any of the requirements

'HTML'
- Access the iframe in with this header to make sure test case scenarios run correctly
1. First test case verifies that the heading includes "My First HTML Page"
2. Second test case verifies that the paragraph to be included in this page is at least 30 words or more
3. Third test case verifies that the images included in this page have a height = 300, width = 200, and alt text description
4. Fourth test case verifies the links to be included can be opened in another window and return a status code of 200, which helps verify that the links work
5. Fifth test case verifies that there is a HTML table included with texts including a Firstname, Lastname, City, State, and Birth Month


