# calends ver 0.35
This app generates a .docx format table showing the class meeting dates for a specified time frame and automatically fills in when those dates fall on hoidays. The program is run in the terminal and outputs a document to the user-configured location.

![Output screenshot](/img/calends_screenshot.png)

## Installing calends

1. Download [Python](https://www.python.org/downloads/)
2. Download the [files](https://github.com/jonalfarlinga/calends) from Github. On the repository page (linked) click the <> Code button, and then Download ZIP.
![github screenshot](/img/github_screenshot.png)
3. Extract the ZIP wherever you want to save calends.
4. Double-click to run <code>install.bat</code>. Close the terminal when finished
5. Double-click to run <code>configure.bat</code>. Press enter twice to use default values, or enter custom values. Close the terminal when finished.
><details>
>    <summary>Default Academic Calendar</summary>
>    <p>https://www.registrar.txst.edu/registration/ac/academic-calendar.html</p>
></details>
><details>
>   <summary>Default home path</summary>
>   <p>User home (e.g.) C:\\Users\username\</p>
></details>
6. You are ready to go!

## Running calends

1. Double-click to run <code>calends.bat</code>.
2. Answer the questions to create a calendar, paying attention to the required formatting.
3. After the program is complete, it will tell you the path the new doc was written to. Feel free to edit in your document processor from here!

![runtime screenshot](/img/runtime_screenshot.png)

## Next Steps
 - DONE - Use python-docx to create a table " Date - Topic - Assignment ".
 - SCRATCH - Gather holiday dates from HolidayAPI.
    - Free APIs don't look forward, and don't get spring break
 - DONE - Gather holidays from user source.
    - DONE - What source(s) TX State Registration - Academic Calendar
 - DONE - Take weekdays and start date from user.
    - DONE - What one-key codes? SMTWRFA
 - DONE - Add holiday logic to build_dates()
 - DONE Add configure .bat to set output path and holiday source
    - DONE add config.json to load saved info.
 - DONE Add run.bat to launch program.
 - Create a GUI
 - Format table
 - make an .exe
 - add option for continuous monthly
