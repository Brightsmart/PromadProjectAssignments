### Python web automation programs

#### dep
`pip install pytest pytest-html selenium allure-pytest openpyxllist, pytest -s src/ThirdProject/test_form_page.py --alluredir=allure-results,  allure serve allure-results  `

#### project 1
open the url - https://katalon-demo-cura.herokuapp.com/
click on the make appoinment button
verify that url changes - assert
time.sleep(3)
enter the username, password
next page verify the current url
make appoinment text on the web page.

#### project 2
Open the URL - https://www.idrive360.com/enterprise/login
Enter the username, password
Verify that Trial is fnished and current URL also
Add a logic to add Allure Screen for the Trail end.

#### project 3
Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
Enter all the fields excepts the username
Verify that the error message comes when you click on the submit button.