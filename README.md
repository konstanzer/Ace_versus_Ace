<a href="https://baseballsavant.mlb.com/statcast_search">
	<img src="/img/logo.jpg" alt="Statcast logo" title="Statcast" align="right" width="200"/>
</a>

Ace versus Ace: An analysis of 2020 Statcast data for Gerrit Cole and Jacob deGrom
======================

Statcast is a tracking technology that allows for the collection and analysis of a massive amount of baseball data based on ball flight paths and player movements. The initial camera and radar system was installed in all 30 MLB parks in 2015 after a trial run in 2014. This project focuses specifically on Statcast data for two pitchers, Gerrit Cole of the New York Yankees and Jacob deGrom of the New York Mets, gathered during the abbreviated 2020 season. The dataset includes a total of 2,338 pitches, each with five features: pitch type, release speed, release spin rate, vertical movement, and horizontal movement.

<img alt="" src="img/statcast.jpg" width='300'>  

___

## Overview

Baseball players, managers, scouts, and fans alike have used stats to analyze and compare player performance for as long as baseball has been played. As the game increased in competitiveness and complexity, more statistics were tracked, and in some cases, as with RBIs and saves, retroactively added to playing careers long since ended. Until relatively recently in the sport's history, metrics were limited to counting stats such as strikeouts and wins or averages such as ERA and WHIP. With the introduction of the radar gun as a measure of pitch speed in the late 1970s, baseball turned a corner. Scouts had a new way to judge a player's ability based on raw, on-field athletic performance. in 2015, the amount of on-field measurements exploded with the introduction of Statcast.

Much of the value of Statcast data has been realized already. Pitchers such as Adam Ottavino have revived their careers through a process known as pitch design. Using real-time feedback from high-speed cameras connected to a laptop computing movement, the pitcher tweaks mechanics and grips until he achieves a maximally breaking pitch. On the visualization front, Daren Willman, founder of the Baseball Savant website, has produced some truly excellent and original diagrams providing new insights into an old game. For the purposes of this project, I wanted to see what measurable on-field factors were associated with a successful pitch and outing and their opposites. It stands to reason that a pitcher may achieve an edge id he knows what factors are correlated with his successes and failures. On the opposite side of the ball, a hitter who knows the pitcher's usual plan of attack is more prepared for the location, movement, and sequence of pitches.
___

## Hawk-Eye

<img alt="" src="img/hawkeye1.png" width='500'>  


In 2020, MLB switched from Trackman to Hawk-Eye Innovations tracking technology. Hawk-Eye systems are based on the principles of triangulation using visual images and timing data provided by a series of high-speed video cameras located at different locations and angles around the field. In each frame, the system identifies the group of pixels which corresponds to the image of the ball and calculates its true 3d position by comparing its 2d position on at least two cameras at the same instant in time. A succession of frames builds a record of the ball travel path and predicts the future flight path of the ball, as well as where it will interact with the playing area features programmed into the database. The system can even interpret these interactions to decide infringements of the rules of the game.

<img alt="" src="/img/hawkeye4.png" width='500'>  


Hawk-Eye first partnered with MLB through the 2014 launch of the video replay system. The Hawk-Eye Statcast system uses a total of 12 cameras for optical pitch, hit and player tracking. Five cameras operating at 100 frames per second are primarily dedicated to pitch tracking, while an additional seven cameras are focused on tracking players and batted balls at 50 frames per second. Objects are tracked to within 0.5cm accuracy of their true positions.

 <img alt="" src="img/hawkeye5.png" width='500'>  

___

## Baseball Savant

BaseballSavant.MLB.com is MLB.com's clearinghouse for Statcast data. It reports measurements (raw numbers from the on-field action) and metrics (combinations of raw measurements into useful numbers) and provides a real-time game feed with tracking data. Baseball Savant includes a search tool to create custom queries and download the output as .csv files. However, for hypothesis testing and modeling purposes, it is useful to have an observation for each pitch and the website does not offer this functionality. A query for all pitches thrown by Gerrit Cole in the Statcast era, for example, returns only a total count and summary statistics. Fortunately, the site allows web scraping with a simple change to the URL on the search tool page. Adding `csv?all=true` to the beginning and `type=detail` to the end will automatically download a .csv file with individual observations. These files must be broken up by for general datasets by changing the `team` and `Sea` parameters. Looping through the database in this way, I was able to download all pitching Statcast data (2015-2020, 1.7GB) in about 40 minutes on my Macbook Air. I did not download offensive data.

(As a possible alternative, an API for this data is available at sportradar.com. However, I did not have success using my trial key and did not pursue the matter further given the ease of scraping the data.)

<img alt="" src="img/techslide.png" width='500'>  

___

## Visualizations

**Stacked bar chart of pitch frequencies in 2020**

<img alt="" src="src/visuals/stacked_bar_pitches.png" width='800'> 

___

**Boxplots of speed, spin rates, and movement lateral and vertical**

Release speeds             |  Release spin rates
:-------------------------:|:-------------------------:
<img alt="" src="src/visuals/release_speed_boxplot.png" width='400'>   |  <img alt="" src="src/visuals/release_spin_rate_boxplot.png" width='400'>

Lateral movements          |  Vertical movements
:-------------------------:|:-------------------------:
<img alt="" src="src/visuals/pfx_x_boxplot.png" width='400'>   |  <img alt="" src="src/visuals/pfx_z_boxplot.png" width='400'> 

___

**Density plots comparing speeds grouped by pitch type**

Unit is MPH measured out-of-hand.

<img alt="" src="src/visuals/Gerrit Cole_release_speed_density.png" width='1000'> 
<img alt="" src="src/visuals/Jacob deGrom_release_speed_density.png" width='1000'>

___

**Density plots comparing spin rates grouped by pitch type**

Unit is RPM. A baseball spins approximately 17 to 22 times during travel.

<img alt="" src="src/visuals/Gerrit Cole_release_spin_rate_density.png" width='1000'> 
<img alt="" src="src/visuals/Jacob deGrom_release_spin_rate_density.png" width='1000'>

___

**Density plots comparing lateral movement grouped by pitch type**

Lateral movement from catcher's perspective. Unit is inches moved in last 40 ft. Negative values move in on a right-handed hitter and vice versa.

<img alt="" src="src/visuals/Gerrit Cole_pfx_x_density.png" width='1000'> 
<img alt="" src="src/visuals/Jacob deGrom_pfx_x_density.png" width='1000'>

___

**Density plots comparing vertical movement grouped by pitch type**

Vertical movement from catcher's perspective. Unit is inches moved in last 40 ft. Negative values move down and vice versa. While no pitch technically rises due to gravity, rise in this case means the deviation from the path of a ball with no spin-induced movement.

<img alt="" src="src/visuals/Gerrit Cole_pfx_z_density.png" width='1000'> 
<img alt="" src="src/visuals/Jacob deGrom_pfx_z_density.png" width='1000'> 

___

## Hypotheses and method

### Hypothesis the first

**Scientific Question**
    
   Are the the mean fastball release speeds between Jacob deGrom and Gerrit Cole the same?

**Null Hypothesis**
    
   The mean fastball release speeds between deGrom and Cole are the same.

**Alternative Hypothesis**
    
   The mean fastball release speeds between deGrom and Cole are not the same.

**Type of Test and Test Statistic**
    
   I use a Welch's t-test. In order to perform a Welch's t-test I use `scipy.stats.ttest_ind`.

**What is the distribution under the null hypothesis?**
    
   The distribution of the null hypothesis represents the difference between the mean of the two distributions. Comparing the release speeds for fastballs, it is
   the distribution of the difference of samples means where the assumption is that the mean of this distribution is zero:
   𝜇 FF_speed deGrom - 𝜇 FF_speed Cole = 0

**Significance level**
    
   I will select a standard significance level of 0.05. I will also use a Bonferonni correction of 3 to account for the fact that I will be comparing multiple
   means. There for my signficance for each individual test will be 𝛼=0.05/3 = 0.1666.

**p-value**

    Gerrit Cole mean release speed: 96.7
    Jacob deGrom mean release speed: 98.6
    Gerrit Cole sample size: 635
    Jacob deGrom sample size: 510
    t-stat: -28.6
    p-value: 4e-136

<img alt="" src="src/visuals/ttests/ttest_543037_594798_FF_release_speed.png" width='500'> 

**Conclusion**

   We have a p-value and need to compare it to our significance level of 0.1666. The p-value (the probability of seeing this result or a result more extreme given
   the null hypothesis) is far less than the significance level. Therefore my conclusion is:
   
   I *reject the null* hypothesis that the release speed means are the same.

___

### Hypothesis the second

**Scientific Question**
    
   Are the the mean curveball release spin rates between Jacob deGrom and Gerrit Cole the same?

**Null Hypothesis**
    
   The mean curveball release spin rates between deGrom and Cole are the same.

**Alternative Hypothesis**
    
   The mean curveball release spin rates between deGrom and Cole are not the same.
   
**Type of Test and Test Statistic**
    
   I use a Welch's t-test. In order to perform a Welch's t-test I use `scipy.stats.ttest_ind`.

**What is the distribution under the null hypothesis?**
    
   The distribution of the null hypothesis represents the difference between the mean of the two distributions. Comparing the spin rates of curveballs, it is the
   distribution of the difference of samples means where the assumption is that the mean of this distribution is zero:
   𝜇 CU_spin deGrom - 𝜇 CU_spin Cole = 0

**Significance level**
    
   I will select a standard significance level of 0.05. I will also use a Bonferonni correction of 3 to account for the fact that I will be comparing multiple
   means. There for my signficance for each individual test will be 𝛼=0.05/3 = 0.1666.

**p-value**

    Gerrit Cole mean release spin rate: 2803
    Jacob deGrom mean release spin rate: 2632
    Gerrit Cole sample size: 207
    Jacob deGrom sample size: 30
    t-stat: 2.61
    p-value: 0.0141

<img alt="" src="src/visuals/ttests/ttest_543037_594798_CU_release_spin_rate.png" width='500'> 

**Conclusion**

   We have a p-value and need to compare it to our significance level of 0.1666. The p-value (the probability of seeing this result or a result more extreme given
   the null hypothesis) is far less than the significance level. Therefore my conclusion is:
   
   I *reject the null* hypothesis that the release spin rate means are the same.
   
___

### Hypothesis the third

**Scientific Question**
    
   Are the the mean curveball vertical movements between Jacob deGrom and Gerrit Cole the same?

**Null Hypothesis**
    
   The mean curveball vertical movements between deGrom and Cole are the same.

**Alternative Hypothesis**
    
   The mean curveball vertical movements between deGrom and Cole are not the same.
   
**Type of Test and Test Statistic**
    
   I use a Welch's t-test. In order to perform a Welch's t-test I use `scipy.stats.ttest_ind`.

**What is the distribution under the null hypothesis?**
    
   The distribution of the null hypothesis represents the difference between the mean of the two distributions. Comparing the vertical movements of curveballs, it
   is the distribution of the difference of samples means where the assumption is that the mean of this distribution is zero:
   𝜇 CU_movement deGrom - 𝜇 CU_movement Cole = 0

**Significance level**
    
   I will select a standard significance level of 0.05. I will also use a Bonferonni correction of 3 to account for the fact that I will be comparing multiple
   means. There for my signficance for each individual test will be 𝛼=0.05/3 = 0.1666.

**p-value**

    Gerrit Cole mean vertical movement: -0.94
    Jacob deGrom mean vertical movement: -0.36
    Gerrit Cole sample size: 207
    Jacob deGrom sample size: 30
    t-stat: -14.0
    p-value: 6e-16

<img alt="" src="src/visuals/ttests/ttest_543037_594798_CU_pfx_z.png" width='500'> 

**Conclusion**

   We have a p-value and need to compare it to our significance level of 0.1666. The p-value (the probability of seeing this result or a result more extreme given
   the null hypothesis) is far less than the significance level. Therefore my conclusion is:
   
   I *reject the null* hypothesis that the curveball vertical movement means are the same.
   
___

   
## Conclusions

Given the 2020 Statcast data for Jacob deGrom and Gerrit Cole:

	1. Who throws a harder fastball?
		Jacob deGrom
	2. Who has a higher curveball spin rate?
		Gerrit Cole
	3. Who has more drop on their curve?
		Gerrit Cole

### Additional research

	1. Explain why Cole creates more spin on average but deGrom has more extreme values of spin.
	2. Include command of pitches in analysis.
	3. Incorporate pitch outcomes into analysis
	4. Conduct z-test to compare overall effect of lateral break.
	
### Acknowledgements
Thank you to Dr. Juliana Duncan, lead data science instructor and principal data scientist at Galvanize Inc., for her pointed questions and conceptual help in forming hypotheses tests.
