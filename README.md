# Currency Converter
Basic Python currency converter.

Currency exchange rate data is obtained from the JSON Currency Data API available from APILayer. (https://apilayer.com/marketplace/currency_data-api)

The GUI is built using the PyQt5 framework. The CC_QT.ui file (in XML) is the design of the GUI created in QT designer, and app.py interfaces that design with Python.

As of now, the program can be run by running the app.py file. However, the program will not work unless an API key obtained from <a href="https://apilayer.com/marketplace/currency_data-api">APILayer</a> is entered into the marked section near the top of the basic_converter file.

This program requires the following packages to run:
<ul>
<li>PyQt5</li>
<li>sys</li>
<li>requests</li>
<li>pandas</li>
</ul>

Since the program is built using Python and PyQt5, it can be run cross-platform, with UI elements displayed in the local OS' design.
<table>
    <tr>
        <th><img width="350" alt="UI_rev3_Mac" src="https://user-images.githubusercontent.com/24969290/183815287-550c685c-a9b2-442b-b1b1-6ff326664492.png"></th>
        <th><img width="350" alt="UI_rev3_Win11" src="https://user-images.githubusercontent.com/24969290/183822572-9650fa08-900a-422a-bb19-4c55d0618b5c.png"></th>
        <th><img width="350" alt="UI_rev3_Ubuntu" src="https://user-images.githubusercontent.com/24969290/183815310-3b3edc5d-2f59-41d8-99b0-9ad0f2cb40fd.png"></th>
    </tr>
    <tr>
        <th>MacOS Monterey</th>
        <th>Windows 11</th>
        <th>Ubuntu 20.04</th>
    </tr>
</table>
