class AlertPageLocators:

    CLICK_ALERT = ("css selector", "button[onclick='jsAlert()']")
    CONFIRM_ALERT = ("css selector", "button[onclick='jsConfirm()']")
    PROMPT_ALERT = ("css selector", "button[onclick='jsPrompt()']")
    ALERT_RESULT_TEST = ("css selector", "p#result")
