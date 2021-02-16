# project1-na354

You do need to install flask to run this program.
There are 3 files needed to run this. One python file servers as the flask host and one gets the backend info from the spotify api. Then a basic html file that prints the format.
For the code to run you need to set the client (CLIENT_ID) and client secret id (CLIENT_SECRET). (ALSO NEEDS THE GENIUS AUTH ID NOW) I used a seperate file and hid the file.
Then you insert the artists ids to use and then theres two functions that use that id. One function gets the artist from the id and one gets a list of top tracks.
From the toptracks function it returns a random song.
The app.py file will then call the function from the project1.py file and return the sorted json data to print in html.
The html now also prints out a genius link generated from the json data from the original function.

#############################################################################################################################################
Milestone 1
If I had more time to implement I wouldve added some additional css and html styling as of right now it just prints it all without any formating.
I would also like to add a button that recalls the function and gets a new random song without having to refresh the page.

The biggest technical issue actually stemmed when I was orignally trying to set up git hub repositories. I was unable to connect to the server properly as I was getting a key error I solved this via realiziing I was trying to use an SSH key and not an html key after rewatching the video posted on it.

The next biggest techincal issue is that I was orignally using the wrong id types from spotify. I copy and pasted the id but the extra things that were tacked on not realizing they wernt actually part of the id. This created a problem because when I tried to get the top tracks it wasnt calling html properly despite me using the correct request. I had to reget all the ids for my artists and that eventually solved the problem.

Lastly, my flask wasn't working in regards to the render_template I couldn't figure out exactly why but, I changed the import to just import the whole of flask instead 
of just the parts I needed and that worked as I needed it too.

#############################################################################################################################################
Milestone 2

With more time I would've liked to make a proper border and image wrapping to make the page less plain. I would've done this by adding a border around the webpage then putting another image on top where I would put all the other elements adding a border like image to the website.

Currently the program seems to work perfectly fine but, the audio and the lyrics arn't always accurate because some times it doesn't have lyrics or a preview audio. There also seemed to be a bug with the genius api being out of range but, I haven't been able to replicate it in a bit and im not sure if its still happening. I would have to see the bug more to see whats causing it. My guess would be that the search request isn't 

One tech issue I struggled with was getting genius api set up. I wasn't sure on how to it so I orginally tried to get an authorization request to genius servers but, I eventually found out it only needs to be 1 request and there you can get a link that has the lyrics on it.

Another technical issue I had was getting heroku to set a defualt language. Eventually I realized that my commit didn't include my Procfile which had the python decleration line which it needed.
