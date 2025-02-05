class WebTablesLocators:
    ADD_BUTTON = ("css selector", "#addNewRecordButton")
    TYPE_TO_SEARCH_FIELD = ("css selector", "#searchBox")
    FIRST_NAME_COLUMN = "//*[text()='First Name']"
    LAST_NAME_COLUMN = "//*[text()='Last Name']"
    AGE_COLUMN = "//*[text()='Age']"
    EMAIL_COLUMN = "//*[text()='Email']"
    SALARY_COLUMN = "//*[text()='Salary']"
    DEPARTMENT_COLUMN = "//*[text()='Department']"
    MODAL_WINDOW = ("css selector", "#registration-form-modal")
    MODAL_WINDOW_CLOSE_BUTTON = ("xpath", "//*[text()='×']")
    EMPTY_SPACE = ("css selector", ".fade modal show")
    WEB_TABLE = ("css selector", "div.rt-tr.-odd")
    FORM_EDIT_BUTTON = ("xpath", "//div[text()='cierra@example.com']/following-sibling::*//*[@id='edit-record-1']")

    # ++++++++++++++++++++++++++++++ web form locators ++++++++++++++++++++++++++++++

    FIRST_NAME_FIELD = ("css selector", "#firstName")
    LAST_NAME_FIELD = ("css selector", "#lastName")
    EMAIL_FIELD = ("css selector", "#userEmail")
    AGE_FIELD = ("css selector", "#age")
    SALARY_FIELD = ("css selector", "#salary")
    DEPARTMENT_FIELD = ("css selector", "#department")
    SUBMIT_BUTTON = ("css selector", "#submit")
