# calends ver 0.9.1
This app generates a .docx format table showing the class meeting dates for a specified time frame and automatically fills in when those dates fall on hoidays. The program is run in the terminal and outputs a document to the user-configured location.

![Output screenshot](/img/calends_screenshot.png)

## Installing calends

1. Download [Python](https://www.python.org/downloads/)
2. Download the [files](https://github.com/jonalfarlinga/calends) from Github. On the repository page (linked) click the <> Code button, and then Download ZIP.
![github screenshot](/img/github_screenshot.png)
3. Extract the ZIP wherever you want to save calends.
4. Double-click to run <code>install.bat</code>. Wait up to 30 seconds for it to begin. You may have to approve a security prompt. When finished, close the terminal if it didn't automatically.
5. Double-click to run <code>configure.bat</code>. Press enter twice to use default values, or enter custom values. When finished, close the terminal if it didn't automatically.
    - <details>
        <summary>Default Academic Calendar</summary>
        <p>https://www.registrar.txst.edu/registration/ac/academic-calendar.html</p>
      </details>
    - <details>
        <summary>Default output path</summary>
        <p>User home (e.g. C:\\Users\username\ )</p>
      </details>
6. You are ready to go!

## Running calends

1. Double-click to run <code>calends.bat</code>.
2. Answer the questions to create a calendar, paying attention to the required formatting.
<ul>
  <details>
    <summary>Show table style formats: Part 1</summary>
    <ul class="simple">
        <li>Table Normal</li>
        <li>Colorful Grid</li>
        <li>Colorful Grid Accent 1</li>
        <li>Colorful Grid Accent 2</li>
        <li>Colorful Grid Accent 3</li>
        <li>Colorful Grid Accent 4</li>
        <li>Colorful Grid Accent 5</li>
        <li>Colorful Grid Accent 6</li>
        <li>Colorful List</li>
        <li>Colorful List Accent 1</li>
        <li>Colorful List Accent 2</li>
        <li>Colorful List Accent 3</li>
        <li>Colorful List Accent 4</li>
        <li>Colorful List Accent 5</li>
        <li>Colorful List Accent 6</li>
        <li>Colorful Shading</li>
        <li>Colorful Shading Accent 1</li>
        <li>Colorful Shading Accent 2</li>
        <li>Colorful Shading Accent 3</li>
        <li>Colorful Shading Accent 4</li>
        <li>Colorful Shading Accent 5</li>
        <li>Colorful Shading Accent 6</li>
        <li>Dark List</li>
        <li>Dark List Accent 1</li>
        <li>Dark List Accent 2</li>
        <li>Dark List Accent 3</li>
        <li>Dark List Accent 4</li>
        <li>Dark List Accent 5</li>
        <li>Dark List Accent 6</li>
    </ul>
  </details>
  <details>
    <summary>Show table style formats: Part 2</summary>
    <ul class="simple">
        <li>Light Grid</li>
        <li>Light Grid Accent 1</li>
        <li>Light Grid Accent 2</li>
        <li>Light Grid Accent 3</li>
        <li>Light Grid Accent 4</li>
        <li>Light Grid Accent 5</li>
        <li>Light Grid Accent 6</li>
        <li>Light List</li>
        <li>Light List Accent 1</li>
        <li>Light List Accent 2</li>
        <li>Light List Accent 3</li>
        <li>Light List Accent 4</li>
        <li>Light List Accent 5</li>
        <li>Light List Accent 6</li>
        <li>Light Shading</li>
        <li>Light Shading Accent 1</li>
        <li>Light Shading Accent 2</li>
        <li>Light Shading Accent 3</li>
        <li>Light Shading Accent 4</li>
        <li>Light Shading Accent 5</li>
        <li>Light Shading Accent 6</li>
        <li>Medium Grid 1</li>
        <li>Medium Grid 1 Accent 1</li>
        <li>Medium Grid 1 Accent 2</li>
        <li>Medium Grid 1 Accent 3</li>
        <li>Medium Grid 1 Accent 4</li>
        <li>Medium Grid 1 Accent 5</li>
        <li>Medium Grid 1 Accent 6</li>
        <li>Medium Grid 2</li>
        <li>Medium Grid 2 Accent 1</li>
        <li>Medium Grid 2 Accent 2</li>
        <li>Medium Grid 2 Accent 3</li>
        <li>Medium Grid 2 Accent 4</li>
        <li>Medium Grid 2 Accent 5</li>
        <li>Medium Grid 2 Accent 6</li>
        <li>Medium Grid 3</li>
        <li>Medium Grid 3 Accent 1</li>
        <li>Medium Grid 3 Accent 2</li>
        <li>Medium Grid 3 Accent 3</li>
        <li>Medium Grid 3 Accent 4</li>
        <li>Medium Grid 3 Accent 5</li>
        <li>Medium Grid 3 Accent 6</li>
    </ul>
  </details>
  <details>
    <summary>Show table style formats: Part 3</summary>
    <ul class="simple">
        <li>Medium List 1</li>
        <li>Medium List 1 Accent 1</li>
        <li>Medium List 1 Accent 2</li>
        <li>Medium List 1 Accent 3</li>
        <li>Medium List 1 Accent 4</li>
        <li>Medium List 1 Accent 5</li>
        <li>Medium List 1 Accent 6</li>
        <li>Medium List 2</li>
        <li>Medium List 2 Accent 1</li>
        <li>Medium List 2 Accent 2</li>
        <li>Medium List 2 Accent 3</li>
        <li>Medium List 2 Accent 4</li>
        <li>Medium List 2 Accent 5</li>
        <li>Medium List 2 Accent 6</li>
        <li>Medium Shading 1</li>
        <li>Medium Shading 1 Accent 1</li>
        <li>Medium Shading 1 Accent 2</li>
        <li>Medium Shading 1 Accent 3</li>
        <li>Medium Shading 1 Accent 4</li>
        <li>Medium Shading 1 Accent 5</li>
        <li>Medium Shading 1 Accent 6</li>
        <li>Medium Shading 2</li>
        <li>Medium Shading 2 Accent 1</li>
        <li>Medium Shading 2 Accent 2</li>
        <li>Medium Shading 2 Accent 3</li>
        <li>Medium Shading 2 Accent 4</li>
        <li>Medium Shading 2 Accent 5</li>
        <li>Medium Shading 2 Accent 6</li>
        <li>Table Grid</li>
    </ul>
  </details>
</ul>

3. After the program is complete, it will tell you the path the new doc and open the containing folder. Feel free to edit in your document processor from here!
4. <b>IMPORTANT:</b> Each time the program is run, it will overwrite the previoues output. Please copy or rename the file if you want to keep it.
![runtime screenshot](/img/runtime_screenshot.png)

## Dev Roadmap

 - Create a GUI
 - make an .exe
 - add option for continuous monthly

 ### Features Complete

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
 - DONE Format table
