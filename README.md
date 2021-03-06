Code Documentation:
                                                
The code for our Visualizing Fictional Narratives project can be broken up into two parts. The first part is a collection of python scripts that are run on a source text in order to generate a tsv and json file with sentiment and co-occurrence data about the story. The second part is a flask web app that uses d3,js and the canvas to showcase the data stored in the tsv and json files on a website.
                                                
The pr1.py script runs on the source text, and extracts the n most frequently occurring people in the story. The get_cooccurence.py script calculates the sentiment between characters, which can be pulled from the file generated by the pr1.py script, and uses them to create the tsv and json data files, which are stored in the static folder.
                                                
The flask web app is run out of app.py, which return the base index.html page stored in the templates folder. index.html calls d3.js libraries that are stored in the static folder. The script compare_sen.py serves as the backend code for the buttons on the web app that allow users to compare the sentiment data for two chapters in the story.
                                                
How to Run Code:
                                                
The user can use the python scripts mentioned above to generate the tsv and json files. The user can spin up the web app by opening the command line, and running ‘python app.py’. This will spin up a local web app. Then, the user can point their web browser to ‘localhost:5000’ in order to use the web app.
                                        
How to Use Website: (https://sahaj96.github.io/The-Hobbit-Visualization/  &  http://sahaj96.pythonanywhere.com)
                                                
There are a number of tools that users can use on the website to better understand a story’s narrative. There is an interactive circular flow chart that displays the ratio of co-occurrences between characters in the book, which reflects the strength of their interactions with each other. Hovering over the character name allow just the relationships of that person to be highlighted. There is a draggable bar above the chart to maneuver between different chapters.
                                                
Clicking on a character’s name results in the bar chart below, which shows normalized sentiment through the course of the story, to focus on the values generated by that character. There is a button below this chart to revert the selection, and once again show the sentiment across the entire story. Hovering over the sentiment bars allows users to see the passage which was responsible for generating the particular sentiment bar.
                                                
Finally, there is an area to select two chapter numbers, and a button which takes the user to a new view that depicts a close up of the two chapter’s sentiment compared against each other. The green line represents the first chapter selected, while the yellow represents the second. Only chapter numbers within the story are selectable on the main page.
