<a href="https://baseballsavant.mlb.com/statcast_search">
    <img src="img/Statcast_logo.jpg" alt="Statcast logo" title="Statcast" align="right" height="160" width="200"/>
</a>

Comparing Sliders with Statcast Pitch Tracking
======================
Statcast is a tracking technology that allows for the collection and analysis of a massive amount of baseball data based on ball flight paths and player movements. The initial radar+camera system was installed in all 30 parks in 2015 after a partial trial run in 2014.

## Contents
1. [Dataset](#dataset)
2. [Exploratory data analysis](#eda)
2. [Future Directions](#future-directions)

<img alt="" src="/img/pitchtracker.jpg" width='600'>  

___

### Hawk-Eye

<img alt="" src="img/hawkeyecam.png" width='600'>  

In 2020, MLB switched from Trackman to Hawk-Eye Innovations tracking technology. Hawk-Eye systems are based on the principles of triangulation using visual images and timing data provided by a number of high-speed video cameras located at different locations and angles around the area of play. In each frame sent from each camera, the system identifies the group of pixels which corresponds to the image of the ball and calculates the position of the ball by comparing its position on at least two cameras at the same instant in time. A succession of frames builds a record of the ball travel path and predicts the future flight path of the ball, as well as where it will interact with the playing area features programmed into the database. The system can even interpret these interactions to decide infringements of the rules of the game.

<img alt="" src="/img/hawkeyemap.png" width='600'>  
<sub> Cameras dedicated to pitch tracking are in red; those dedicated to motion tracking and batted balls are in yellow. </sub>  


Hawk-Eye first partnered with MLB through the 2014 launch of the video replay system. The Hawk-Eye Statcast system uses a total of 12 cameras for optical pitch, hit and player tracking. Five cameras operating at 100 frames per second are primarily dedicated to pitch tracking, while an additional seven cameras are focused on tracking players and batted balls at 50 frames per second.

 <img alt="" src="img/objectdetection.png" width='600'>  
<sub>Objects are tracked to within 0.5cm accuracy of their true positions. </sub>

___

### Google Cloud

Also in 2020, MLB migrated its Wheelhouse Data and Analytics Platform to BigQuery, Google Cloud’s enterprise data warehouse. In a Google Cloud demo, five years of Statcast pitch data are mapped via a K-Means clustering algorithm and PCA dimensionality reduction onto a 3D space. The clusters represent pitchers' strategies, demonstrating one possible use of machine learning with this dataset.

___

### Baseball Savant

BaseballSavant.MLB.com is MLB.com's clearinghouse for Statcast data. It reports measurements (raw numbers from the on-field action) and metrics (combinations of raw measurements into useful numbers) and provides a real-time game feed with tracking data. Baseball Savant includes a powerful search tool to create custom queries and download the output as .csv files. However, for hypothesis testing and modeling purposes, it is useful to have an observation for each pitch; the website does not offer this functionality.

<img alt="" src="img/savantsearch.png" width='1000'>  
<sub><b>Fig. 4: </b> The search tool I used to determine a URL for scraping. </sub> 

___


