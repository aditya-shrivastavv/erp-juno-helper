# Automation Stale Task - ERP JUNO Quiz

## Important

Before choosing any of the given two methods:

1. Python - Selenium (Fully Automatic)
2. Plain JS (Semi - Automatic)

You must check if the "blue colored chips for navigating through the question while giving the tests are enabled or not? are they clickable or not"

```js
if (enabled) {
   Go With Python Selenium (`run.py` and `main.py`)
}
else {
   Go With Plain JS (`script.js`)
}
```

## Python - Selenium

This script collects all the questions and it's options from the quiz and compiles them into a file `output.txt`. Then you can find the answers by any mean you want to then fill the answers on the quiz portan then submit.

> NOTE: This script does not guaruntee the correctness of answers.

### Run

To this script follow the steps listed:

> NOTE: Only made to run in edge browser but can be modified for other browsers too.
> PREREQUISITES: Python must be installed in your system

1. Firstly you need to download the driver for your browser
   1. Search this in the edge browser: `edge://version/`
   2. Check the first line displaying the version of the browser
   3. Download the compatible zip file of the driver from <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>, and make sure to download it through the `Stable Channel` and the `x64` version
   4. After extracting the zip file, keep running `msedgedriver.exe` in the background while the script is running
2. Clone this repo. (First fork if you want to. (Optional))
3. Open it in VS Code
4. Run the command:

   ```bash
   pip install -r requirements.txt
   ```

5. Make a `.env` file, In that file add the following environment variables:

   ```env
   ERP_BASE_URL=<your erp website login page link>
   ERP_USERNAME=<your username or email registered with the website>
   ERP_PASSWORD=<your password>
   ERP_TEST_NUMBER=<quiz number>
   ```

   You will find the quiz number by counting the quiz from the top. For example the quiz listed on top is the quiz number 1, next one will be quiz number 2.

   **IT IS THE QUIZ FOR WHICH YOU WANNA RUN THE SCRIPT.**

6. In the `run.py` file there is a statement:

   ```py
   bot.startTest([bool, int])
   ```

   It takes array as an input, that array is the configuration for starting the test

   - If there is no password required to start the quiz the array should be `[False, "x"]`
   - If you know that there is password make that array to be `[True, 1234]`. **1234** is the default password

   The `True` tells the script that there is password requried after that you give it the password to be filled there. If the password is a string, make sure it is within quotes (Basic programming)

7. To run the script:

    ```bash
    python run.py
    ```

After running the `Edge Browser` should open and you can see the script running. After completion of the script you will be on the last question of the quiz on the website. The terminal will ask you if you want to close that window, do whatever you want.

You will see a `output.txt` file generated in your project root.

I recommend finding the answers of the question and then fill the answers, then submit and close that browser window

You can find the answers from wherever you want (You know what i mean. Huh??). A prompt is already available in the end of `run.py` file.

## Plain JS

In case the tiles on the side through which you can navigate the questions of the quiz are disabled the Selenium script will not work. So use this script. **This is not fully automatic but it does the work**.

### Use

1. Start the quiz
1. Open the console on broswer
1. Paste the function `run` as it is from the `script.js` file to the console and PRESS enter

Now you are done to make use of it.

1. Type `run()` on the console and use will get the output per question on the console itself.
1. Copy the output and find the answer, fill the answer on the quiz and proceed to next question
1. Repeat for all questions

> TIP: Just press the UP ARROW to get the previous command on the console to run.
