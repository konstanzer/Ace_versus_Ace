<a href="https://baseballsavant.mlb.com/statcast_search">
    <img src="img/Statcast_logo.jpg" alt="Statcast logo" title="Statcast" align="right" height="160" width="200"/>
</a>

Statcast Pitch Tracking
======================
Statcast is a tracking technology that allows for the collection and analysis of a massive amount of baseball data based on ball flight paths and player movements. The initial radar+camera system was installed in all 30 parks in 2015 after a partial trial run in 2014.


<img alt="" src="/img/pitchtracker.jpg" width='600'>  
<sub><b>Fig. 1: </b> Tracking pitch flight at Wrigley Field. </sub>

___

### Hawk-Eye

In 2020, MLB switched from Trackman to Hawk-Eye Innovations tracking technology. Hawk-Eye systems are based on the principles of triangulation using visual images and timing data provided by a number of high-speed video cameras located at different locations and angles around the area of play. In each frame sent from each camera, the system identifies the group of pixels which corresponds to the image of the ball and calculates the position of the ball by comparing its position on at least two cameras at the same instant in time. A succession of frames builds a record of the ball travel path and predicts the future flight path of the ball, as well as where it will interact with the playing area features programmed into the database. The system can even interpret these interactions to decide infringements of the rules of the game.

Hawk-Eye first partnered with MLB through the 2014 launch of the video replay system. The Hawk-Eye Statcast system uses a total of 12 cameras for optical pitch, hit and player tracking. Five cameras operating at 100 frames per second are primarily dedicated to pitch tracking, while an additional seven cameras are focused on tracking players and batted balls at 50 frames per second.


<img alt="" src="/img/hawkeyecam.png" width='600'>  
<sub><b>Fig. 2: </b> A typical Hawk-Eye camera installation. </sub>

<img alt="" src="/img/hawkeyemap.png" width='600'>  
<sub><b>Fig. 3: </b> Cameras dedicated to pitch tracking are in red; those dedicated to motion tracking and batted balls are in yellow. </sub>   

___

### Google Cloud

MLB migrated its Wheelhouse Data and Analytics Platform to BigQuery, Google Cloud’s enterprise data warehouse. In one particulary outstanding interactive 3D visualization, BigQuery is used to store five seasons of pitch level event data. Views are created on top of the raw data to complete the feature engineering process. Finally, a K-Means clustering algorithm and dimensionality reduction via PCA map them onto a 3D space. The clusters represent pitchers' strategies.

### Baseball Savant

BaseballSavant.MLB.com is MLB.com's clearinghouse for Statcast data. It reports measurements (raw numbers from the on-field action) and metrics (combinations of raw measurements into useful numbers) and provides a real-time game feed. Baseball Savant includes a search tool to create custom queries and dowload th output as .csv files. However, for modeling purposes, it is useful to have an observation for each pitch. The website currently does not offer this functionality. Savant Scraper allows for simple loading of a portable database or the creation of individual files that could be loaded to a storage object like S3 on AWS.
