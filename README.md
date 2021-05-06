### Connecticut Crash Data Repository


The Connecticut Crash Data Repository (CTCDR) is a web tool designed to provide access to select crash information collected by state and local police. This data repository enables users to query, analyze and print/export the data for research and informational purposes. The CTCDR is comprised of crash data from two separate sources; The Department of Public Safety (DPS) and The Connecticut Department of Transportation (CTDOT). The purpose of the CTCDR is to provide members of the traffic-safety community with timely, accurate, complete and uniform crash data. The CTCDR allows for complex queries of both datasets such as, by date, route, route class, collision type, injury severity, etc. For further analysis, this data can be summarized by user-defined categories to help identify trends or patterns in the crash data.

#### Please visit our website [crashdash.org](https://crashdash.org/) to see our final product

Running our code from this repository requires VS Code with the live serverand live Sass compiler extensions by Ritwick Dey, as well as Python and Pip, which will be necessary to install Flask and Plotly Dash to run the individual web dashboards on each page, and re-deploy them. The plotly dashboards are deployed using Heroku, which is an online hosting platform. Each dashboard features a "requirements.txt" file which contains the different packages that are needed to run them, heroku automatically downloads the packages from this file upon  deployment. To add a new dashboard and pubish to heroku follow these instructions https://dash.plotly.com/deployment. 

To run the page in VS Code, make sure you have the live server extension, then right-click on "index.html" and click "Open with Live Server" and the website will open on a localhost server in your browser. 

If edits are made to the "tabstyle.scss" file make sure to hit the "Watch Sass" button in the bottom right to make sure the changes are applied to the CSS file as well.
