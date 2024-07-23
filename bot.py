"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""


# Import for the Desktop Bot
from botcity.core import DesktopBot,Backend

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    
    # Implement here your logic...
    exePath = "E:\RPA\BotCity\Projects\desktop_automation\MyCRM\MyCRM.exe"
    #bot.execute(exePath)
    app = bot.connect_to_app(backend=Backend.UIA, path=exePath, title="My CRM (Sample App)")

    first_field = bot.find_app_element(from_parent_window=app.top_window(), auto_id = "textBoxPeopleFirstName")
    first_field.set_text("Thestalos")
    
    last_field = bot.find_app_element(from_parent_window=app.top_window(), auto_id = "textBoxPeopleLastName")
    last_field.set_text("Monarch")

    company_tab = bot.find_app_element(from_parent_window=app.top_window(), control_type ="TabItem", title="Company ")
    company_tab.select()

    other_tab = bot.find_app_element(from_parent_window=app.top_window(), control_type ="TabItem", title="Other")
    other_tab.select() 

    state_dropdown = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "comboBoxPeopleAddressState", title = "State:")
    state_dropdown.click_input()

    list_item = bot.find_app_element(from_parent_window = app.top_window(), title = "AK", control_type = "ListItem")
    list_item.click_input()

    is_active_checkbox = bot.find_app_element(from_parent_window=app.top_window(), auto_id = "checkBox1")
    is_active_checkbox.toggle()
    is_active_checkbox.click()
    print(is_active_checkbox.get_toggle_state())

    if is_active_checkbox.get_toggle_state() == 0:
        print("The checkbox is unchecked, let's check it!")
        is_active_checkbox.toggle()
    else:
        print("Checkbox already checked!")

    save_btn =  bot.find_app_element(from_parent_window=app.top_window(), auto_id = "button1")
    save_btn.click()

    #other_tab = bot.find_app_element(from_parent_window=app.top_window(), control_type ="TabItem", title="Other")
    other_tab.select() 
    browse_btn =  bot.find_app_element(from_parent_window=app.top_window(), auto_id = "button2")
    browse_btn.click()
    #state_dropdown.select("AZ")
    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()