-----
### 1. MLB Statcast
-----
* Purpose: MLB Statcast data has been collected for the last five years using high-speed cameras tracking every pitch and play at the major league level. It may be interesting to investigate for hidden value in player performance using the new metrics similar to what Billy Beane did with OBP and the Pirates with defensive shifts.
	
* Question: [Wins against replacement](https://en.wikipedia.org/wiki/Wins_Above_Replacement) is a widely accepted measure of player value. Strangely, baseball commentators are incapable of explaining its complicated formula. I would like to make a comprehensible metric using statcast and traditional statistics that correlates well with WAR. I am tempted to ask the subjective questions which fuel sports radio chatter but perhaps a simpler question like, "Did Gerrit Cole throw more sliders than Jacob deGrom in 2020?" would be suitable for hypothesis testing.
	
* Data: [Baseball Savant maintains a complete database of Statcast data.](https://baseballsavant.mlb.com/leaderboard/custom?year=2019,2018,2017,2016,2015&type=pitcher&filter=&sort=4&sortDir=asc&min=q&selections=xba,xslg,xwoba,xobp,xiso,exit_velocity_avg,launch_angle_avg,barrel_batted_rate,&chart=false&x=xba&y=xba&r=no&chartType=beeswarm) Query outputs can be downloaded as a .csv file. The site owner, Daren Willman, MLB director of R&D, has made some [outstanding visualizations based on this data.](https://twitter.com/darenw) For traditional statistics to accompany the new ones, [baseball-reference.org](https://www.baseball-reference.com/) maintains a comprehensive database dating back to 1871. 
-----
### 2. SpaceX
-----
* Purpose: [SpaceX](https://en.wikipedia.org/wiki/Book:SpaceX) has commercialized space and maintains perhaps the boldest mission statment of any business ever: to colonize Mars. The company's unlikely success has spurred a revival in space enthusiasm unseen since the Apollo program.

* Question: While there is ample data about each flight, SpaceX has only a moderate 117 launches as of February 22. Given this high-dimensional data, formulating a testable question is difficult, moreso because most parameters stay the same from flight to flight.

* Data: An [excllent REST API for SpaceX](https://github.com/r-spacex/SpaceX-API) launch, rocket, core, capsule, starlink, launchpad, and landing pad data resides on Github. The [SpaceX subreddit](https://www.reddit.com/r/spacex/) provides additional links and tables related to everything from mission timelines to to recovery vessels. Perhaps outside the scope of this project, I would like to see visualizations of Mars relative to Earth as a habitable planet.
-----	
### 3. Whaling
-----
* Purpose: Many cetaceans (large marine mammals) are under threat of extinction from human activity. Bringing awareness to the shrinking numbers of these species may curb their depletion.

* Question: What cetaceans are in the gravest danger of extinction? How successful has the IWF ban on commercial whaling been?
	
* Data: Marine biologist Daniel Purdy calls the [catch data collected by the Food and Agriculture Organization of the United Nations](http://www.fao.org/fishery/statistics/global-production/en) the best dataset we have for the "visible" haul of marine life from the ocean. Unfortunately, there exists a large illegal component for which no reliable data exists. The International Union for Conservation of Nature and Natural Resources [maintains a redlist of endangered species](https://www.iucnredlist.org/) and a .shapefile with geographic ranges of endangered whales. The International Whaling Commission also [maintains data on whales](https://iwc.int/estimate) that can be scraped from the website. Many documents are .pdfs and these can be scraped as well.
