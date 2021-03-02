<a href="https://baseballsavant.mlb.com/statcast_search">
	<img src="/img/logo.jpg" alt="Statcast logo" title="Statcast" align="right" width="200"/>
</a>

Ace versus Ace: An analysis of 2020 Statcast data for Gerrit Cole and Jacob deGrom
======================

Statcast is a tracking technology that allows for the collection and analysis of a massive amount of baseball data based on ball flight paths and player movements. The initial camera and radar system was installed in all 30 MLB parks in 2015 after a trial run in 2014. This project focuses specifically on Statcast data for two pitchers, Gerit Cole of the New York Yankees and Jacob deGrom of the New York Mets, gathered during the abbreviated 2020 season. The dataset includes a total of 2,338 pitches each with five features: pitch type, release speed, release spin rate, vertical movement, and horizontal movement.

<img alt="" src="img/statcast.jpg" width='300'>  
___

### Overview

Baseball players, managers, scouts, and fans alike have used stats to analyze and compare player performance for as long as baseball has been played. As the game increased in competitiveness and complexity, more statistics were tracked, and in some cases, as with RBIs and saves, retroactively added to playing careers long since ended. Until relatively recently in the sport's history, metrics were limited to counting stats such as strikeouts and wins or averages such as ERA and WHIP. With the introduction of the radar gun as a measure of pitch speed in the late 1970s, baseball turned a corner. Scouts had a new way to judge a player's ability based on raw, on-field athletic performance. in 2015, the amount of on-field measurements exploded with the introduction of Statcast.

Much of the value of Statcast data has been realized already. Pitchers such as Adam Ottavino have revived thir careers through a process known as pitch design. Using realtime feedback from high-speed cameras connected to a laptop computing movement, the pitcher tweaks mechanics and grips until he achieves a maximally breaking pitch. For the purposes of this project, I wanted to see what measurable on-field factors were associated with a successful pitch and their opposites. It stands to reason that a pitcher may achieve an edge id he knows what factors are correlated with his successes and failures. On the opposite side of the ball, a hitter who knows the pitcher's usual plan of attack is more prepared for the location, movement, and sequence of pitches.
___

### Hawk-Eye

<img alt="" src="img/hawkeye1.png" width='500'>  


In 2020, MLB switched from Trackman to Hawk-Eye Innovations tracking technology. Hawk-Eye systems are based on the principles of triangulation using visual images and timing data provided by a series of high-speed video cameras located at different locations and angles around the field. In each frame, the system identifies the group of pixels which corresponds to the image of the ball and calculates its true 3d position by comparing its 2d position on at least two cameras at the same instant in time. A succession of frames builds a record of the ball travel path and predicts the future flight path of the ball, as well as where it will interact with the playing area features programmed into the database. The system can even interpret these interactions to decide infringements of the rules of the game.

<img alt="" src="/img/hawkeye4.png" width='500'>  


Hawk-Eye first partnered with MLB through the 2014 launch of the video replay system. The Hawk-Eye Statcast system uses a total of 12 cameras for optical pitch, hit and player tracking. Five cameras operating at 100 frames per second are primarily dedicated to pitch tracking, while an additional seven cameras are focused on tracking players and batted balls at 50 frames per second. Objects are tracked to within 0.5cm accuracy of their true positions.

 <img alt="" src="img/hawkeye5.png" width='500'>  

___

### Baseball Savant

BaseballSavant.MLB.com is MLB.com's clearinghouse for Statcast data. It reports measurements (raw numbers from the on-field action) and metrics (combinations of raw measurements into useful numbers) and provides a real-time game feed with tracking data. Baseball Savant includes a search tool to create custom queries and download the output as .csv files. However, for hypothesis testing and modeling purposes, it is useful to have an observation for each pitch and the website does not offer this functionality. A query for all pitches thrown by Gerrit Cole in the Statcast era, for example, returns only a total count and summary statistics. Fortunately, the site allows web scraping with a simple change to the URL on the sarch tool page. Adding `csv?all=true` to the beginning and `type=detail` to the end will automatically download a .csv file with individual observations. These files must be broken up by for general datasets by changing the `team` and `Sea` parameters. Looping through the database in this way, I was able to download all pitching Statcast data (2015-2020, 1.7GB) in about 40 minutes on my Macbook Air. I did not download offensive data.

(As a possible alternative, an API for this data is available at sportradar.com. However, I did not have success using my trial key and did not pursue the matter further given the ease of scraping the data.)

___


