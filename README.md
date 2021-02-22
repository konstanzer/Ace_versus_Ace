
### Statcast

About Statcast

Statcast is a state-of-the-art tracking technology that allows for the collection and analysis of a massive amount of baseball data in ways that were never possible in the past. Statcast can be considered the next step in the evolution of how we consume and think about the sport of baseball that began over a decade ago, when Major League Baseball Advanced Media installed pitch tracking hardware in each Major League stadium. That was a step that unlocked a new age of baseball fandom, and Statcast built upon that innovation by adding the tracking of players and the batted ball to the initial pitch-tracking technology. The initial radar/camera system was installed in all 30 parks in 2015 after a partial trial run in 2014.

Since then, Statcast technology and terminology has changed the way that games are viewed and decisions are made, allowing allows front offices, broadcasters and fans alike to quantify the raw skills of players in ways that were previously available only to scouts or not available at all. Terms like "spin rate," "exit velocity," "launch angle" and more have become ubiquitous not just on broadcasts but from the players on the field as well, as players across the league used the data and the thinking behind it to elevate their game.

In 2020, MLB introduced upgraded technology to power Statcast, featuring optical tracking sensors from Hawk-Eye Innovations and cloud infrastructure from Google Cloud. Hawk-Eye first partnered with MLB through the 2014 launch of the video replay system, a successful partnership that has allowed MLB umpires to confirm or correct over 1,000 calls per season. The Hawk-Eye Statcast system utilizes a total of 12 cameras around the park for full-field optical pitch, hit and player tracking. Five cameras operating at 100 frames per second are primarily dedicated to pitch tracking, while an additional seven cameras are focused on tracking players and batted balls at 50 frames per second. Read more about the technology that powers Statcast here.
Available Data

Statcast currently reports measurements (raw numbers from the on-field action) and metrics (combinations of raw measurements into useful numbers).
Baseball Savant is a website that contains MLB Statcast data. This data includes data about each pitch such as speed, spin, and location. Most importantly, this source has information about the batted ball such as exit velocity and launch angle.

The website offers robust querying options. However, for predictive modeling/machine learning purposes, it is useful to have an observation for each pitch. The website currently does not offer this functionality. The goal of this project is to provide as complete a database of pitch events as possible. There are other projects that focus on specific queries or the functions can be easily modified to select different subsets of the data. This script allows for simple loading of a portable database or the creation of individual files that could be loaded to a storage object like S3 on AWS.
