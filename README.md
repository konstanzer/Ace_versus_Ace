<a href="https://baseballsavant.mlb.com/statcast_search">
    <img src="img/Statcast_logo.jpg" alt="Statcast logo" title="Statcast" align="right" height="160" width="200"/>
</a>

Statcast Pitch Tracking
======================
Statcast is a tracking technology that allows for the collection and analysis of a massive amount of baseball data in ways that were never possible in the past. Statcast built upon that innovation by adding the tracking of players and the batted ball to the initial pitch-tracking technology. The initial radar/camera system was installed in all 30 parks in 2015 after a partial trial run in 2014.

___

<img alt="" src="/img/pitchtracker.jpg" width='600'>  
<sub><b>Fig. 1: </b> Tracking pitch flight at Wrigley Field. </sub>

___

In 2020, MLB introduced upgraded technology to power Statcast, featuring optical tracking sensors from Hawk-Eye Innovations and cloud infrastructure from Google Cloud. Hawk-Eye first partnered with MLB through the 2014 launch of the video replay system. The Hawk-Eye Statcast system uses a total of 12 cameras for optical pitch, hit and player tracking. Five cameras operating at 100 frames per second are primarily dedicated to pitch tracking, while an additional seven cameras are focused on tracking players and batted balls at 50 frames per second.

___

<img alt="" src="/img/hawkeyecam.png" width='600'>  
<sub><b>Fig. 2: </b> A typical Hawk-Eye camera installation. </sub>

<img alt="" src="/img/hawkeyemap.png" width='600'>  
<sub><b>Fig. 3: </b> Cameras dedicated to pitch tracking are in red; those dedicated to motion tracking and batted balls are in yellow. </sub>   

___

#### Baseball Savant

BaseballSavant.MLB.com is MLB.com's clearinghouse for Statcast data. It reports measurements (raw numbers from the on-field action) and metrics (combinations of raw measurements into useful numbers) and provides a real-time game feed. Baseball Savant includes a search tool to create custom queries and dowload th output as .csv files. However, for modeling purposes, it is useful to have an observation for each pitch. The website currently does not offer this functionality. Savant Scraper allows for simple loading of a portable database or the creation of individual files that could be loaded to a storage object like S3 on AWS.
