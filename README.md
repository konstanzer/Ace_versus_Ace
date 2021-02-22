
<div style="text-align:center"><img src="/img/Statcast_logo.jpg" /></div>
### About Statcast

Statcast is a tracking technology that allows for the collection and analysis of a massive amount of baseball data in ways that were never possible in the past. Statcast built upon that innovation by adding the tracking of players and the batted ball to the initial pitch-tracking technology. The initial radar/camera system was installed in all 30 parks in 2015 after a partial trial run in 2014.

<img alt="" src="/img/motioncapture.jpg" width='400'>  
<sub><b>Fig. 1: </b> Tracking baserunner paths. </sub> 


<img alt="" src="/img/pitchtracker.jpg" width='400'>  
<sub><b>Fig. 2: </b> Tracking pitch flight. </sub> 

Since then, Statcast technology and terminology has changed the way that games are viewed and decisions are made, allowing allows front offices, broadcasters and fans alike to quantify the raw skills of players in ways that were previously available only to scouts or not available at all. Terms like "spin rate," "exit velocity," "launch angle" and more have become ubiquitous not just on broadcasts but from the players on the field as well, as players across the league used the data and the thinking behind it to elevate their game.


<img alt="" src="/img/hawkeyemap.png" width='400'>  
<sub><b>Figure 1: </b> Map of Hawk-Eye. Cameras dedicated to pitch tracking are in red; those dedicated to motion tracking and batted balls are in yellow. </sub> 

In 2020, MLB introduced upgraded technology to power Statcast, featuring optical tracking sensors from Hawk-Eye Innovations and cloud infrastructure from Google Cloud. Hawk-Eye first partnered with MLB through the 2014 launch of the video replay system. The Hawk-Eye Statcast system uses a total of 12 cameras for optical pitch, hit and player tracking. Five cameras operating at 100 frames per second are primarily dedicated to pitch tracking, while an additional seven cameras are focused on tracking players and batted balls at 50 frames per second.

<img alt="" src="/img/hawkeyecam.png" width='400'>  
<sub><b>Figure 1: </b> A Hawk-Eye camera installation. </sub> 

<img alt="" src="/img/hawkeyemap.png" width='400'>  
<sub><b>Figure 1: </b> Map of Hawk-Eye. Cameras dedicated to pitch tracking are in red; those dedicated to motion tracking and batted balls are in yellow. </sub>   

Statcast currently reports measurements (raw numbers from the on-field action) and metrics (combinations of raw measurements into useful numbers).

#### Baseball Savant

BaseballSavant.MLB.com is MLB.com's clearinghouse for Statcast data. That includes pre-made leaderboards for metrics like Sprint Speed, Outs Above Average and Pop Time, as well as a search tool that allows users to create custom queries.

Baseball Savant provides a real-time game feed for any game played in a Statcast-enabled ballpark, and offers an interactive 3D pitch-tracking system.

#### Savant Scraper

Baseball Savant includes data about each pitch such as speed, spin, and location. However,for modeling purposes, it is useful to have an observation for each pitch. The website currently does not offer this functionality. Savant Scraper allows for simple loading of a portable database or the creation of individual files that could be loaded to a storage object like S3 on AWS.
