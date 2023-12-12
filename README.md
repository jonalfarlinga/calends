# calends ver 0.11
An app for generating semester calendars. When complete, the user will specify
a location for a holiday list, or use an API to get holidays, and specify weekdays
for the class to meet. The app will create a .docx containing a table of
"Mon dd" and "holiday status".

![Output screenshot](/img/calends_screenshot.png)

## Next Steps
 - DONE - Use python-docx to create a table " Date - Topic - Assignment ".
 - SCRATCH - Gather holiday dates from HolidayAPI.
    - Free APIs don't look forward, and don't get spring break
 - DONE - Gather holidays from user source.
    - DONE - What source(s) TX State Registration - Academic Calendar
 - DONE - Take weekdays and start date from user.
    - DONE - What one-key codes? SMTWRFA
 - DONE - Add holiday logic to build_dates()
 - Add configure .bat to set output path and holiday source
    - add config.json to load saved info.
 - Add run.bat to launch program.
 - Create a GUI
 - Format table
 - make an .exe
