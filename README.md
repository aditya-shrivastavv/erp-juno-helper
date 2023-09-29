# Automation Stale Task - ERP JUNO Quiz

## Python - Selenium

This script collects all the questions and it's options from the quiz and compiles them into a file `output.txt`. Then you can find the answers by any mean you want to then fill the answers on the website then submit.

### Run

To this script follow the steps listed:

1. Clone this repo. (First fork if you want to. (Optional))
1. Open it in VS Code or Just open terminal here.
1. Run the command:

   ```bash
   pip install -r requirements.txt 
   ```

1. Make a `.env` file, In that file add the following environment variables:

   ```env
   ERP_BASE_URL=<your erp website login page link>
   ERP_USERNAME=<your username or email registered with the website>
   ERP_PASSWORD=<your password>
   ERP_TEST_NUMBER=<test number>
   ```

1. The test number is just the number you will find by counting the numbers from the top. For example the test listed on top is the test number one, next one will be test number two. IT IS THE TEST FOR WHICH YOU WANNA RUN THE SCRIPT.
1. To run the script:

    ```bash
    python run.py
    ```

After running the `Edge Browser` should open and you can see the script running. After completion of the script you will be on the last question of the quiz on the website. DO NOT CLOSE THE BROSWER WINDOW OR THE WEBSITE.

You will see a `output.txt` file generated in your project root.

You can find the answers from wherever you want (You know what i mean). A prompt is already added at the top of the `output.txt` file.

## Plain Javascript

In case the tiles on the side through which you can navigate the questions of the quiz are disabled you this. This is not fully automatic but it does the work.
