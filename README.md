# Polibugs [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
###### Polibugs is a nonpartisan tool to provide balanced viewpoints on the news.

made at [CodeDay Bay Area Winter 2018](https://showcase.srnd.org/winter-2018/ba/wrapup)  

winner of [Best in Class Application (1st Place)](https://drive.google.com/file/d/1cLVSdm1ooVIOO0GIcu4oYj9b-bkr1um8/view) out of nearly 100 participants and over 25 teams

website live at [https://polibugs.com/](https://polibugs.com/)

favicon by [adiante apps](https://www.iconfinder.com/icons/287491/blog_feed_news_newspaper_rss_icon)

### About  
###### Front-end
+ Polibugs is deployed and distributed using Amazon Web Services Elastic Compute Cloud (AWS EC2)
  + AWS Elastic Beanstalk is used to deploy the Docker container onto load balanced instances
  + the site is distributed over HTTPS using a CloudFlare trusted SSL certificate
+ Polibugs uses the Bootstrap front-end framework
###### Back-end
+ Polibugs does link processing server-side
+ Balanced articles are lazy-loaded client side
+ Uses [News API](http://newsapi.org) to get the latest articles
