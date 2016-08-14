# QuickCanvas
###Built for MadHacks Spring 2016 Hackathon###
We received honorable mention, or 5th out of 15-20 teams. The hackathon lasted for about 12 hours. The team consisted of Kevin Houck and Gabriel Elkind

###Description of Problem###
The idea for this app came from Gabriel. He had recently just helped canvas an large area, or gauge interest on how voters feel about certain issues on the upcoming election.
He noticed that coordinating canvassing efforts with a team of people was actually faitly complicated. The idea was they would split up, and each team member would go to a subset of houses. 
However, sitting down and trying to plan routes for each team member that would take around the same time to finish was not simple

###Description of Solution###
QuickCanvas tries to solve this problem. Given a list of houses and a number of users, the app will plan coherent routes that are close to the same distance. Each canvasser can see their route on their phone, and doesn't have to worry about the logistics of planning routes.
QuickCanvas allows them to focus on what they are trying to accomplish.

###How to use QuickCanvas###
To use QuickCanvas, a single user sends a list of houses to the server along with the number of canvassers, and the server returns a number. The server then returns a canvas id. Users can then go onto the app and enter this canvas id along with what number user they are to see their route. 
Their route is then displayed on a Google Maps view.

###Technologies###
This back end for this app is built in Python. Its core functionality is exposed via a RESTful API. We are using google maps to get the geolocation of each of the addresses. 
We then compute a distance matrix to find the distances between each house. The algorithm to plan routes works by taking n number of canvassers, and then finding the n houses farthest away from each other. We chose to start with this because a team of canvassers will usually share a car, and each can be dropped off.
Next, a greedy algorithm iterates through each canvasser, selecting their nearest house by distance, using the distance matrix we computed earlier.

The front end is built in TypeScript using Ionic 2 and Angular.js 2. We chose to use TypeScript because we did not want to have to waste time debugging during a hackathon, as the compiler could let us know of our mistakes at compile time rather than run time. We are also using Google Maps view to display the routes.

###Todo List/Caveats###
For the Hackathon we were not able to implement a lot of the vision for this app. Thing we would like to improve upon if we ever pick up this project again are:
* A UI for uploading a list of houses. This is currently done with a POST request and a JSON array.
* Authentication rather than using a canvas id to let users view their routes. This would be done by registering groups, and having users belong to those groups. This would also remove the need for users to enter a canvasser number.
* A better algorithm. We were only able to accomplish a Proof of Concept for the Hackathon. Improvements to the algorithm would be:
  * Account for other time costs in addition to distance. Visiting each house takes time, and thing like waiting to cross the street do as well.
  * Start and end all canvassers at the same single location, so they can just park their car and come back to it.
