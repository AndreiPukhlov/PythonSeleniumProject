class WebFormsLocators:

    PRACTICE_FORM_BUTTON = ("xpath", "//*[text()='Practice Form']")
    FIRST_NAME = ("css selector", "#firstName")
    LAST_NAME = ("css selector", "#lastName")
    EMAIL = ("css selector", "#userEmail")
    MOBILE = ("css selector", "#userNumber")
    DOB_INPUT = ("css selector", "#dateOfBirthInput")
    SELECT_DOB_DAY = ("xpath", "(//div[text()='6'])[1]")
    SELECT_DOB_MONTH = ("css selector", ".react-datepicker__month-select")
    SELECT_DOB_YEAR = ("css selector", ".react-datepicker__year-select")
    CHOOSE_FILE_BUTTON = ("css selector", "#uploadPicture")
    ADDRESS = ("css selector", "#currentAddress")
    SUBJECT = ("css selector", "#subjectsInput")
    SELECT_STATE = ("css selector", "#state")
    INPUT_STATE = ("css selector", "#react-select-3-input")
    SELECT_CITY = ("css selector", "#city")
    INPUT_CITY = ("css selector", "#react-select-4-input")
    SUBMIT_BUTTON = ("css selector", "button#submit")
    INFO_RESULT = ("xpath", "//tbody/tr/td")
    UPLOAD_FOLDER_PATH = "data/test_data/demoqa_testdata/upload_demoqa"
    a = "//label[text()='Male']Sports"


