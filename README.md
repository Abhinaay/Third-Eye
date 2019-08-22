# हमारा पर्यटन कतई जहर
Someone is watching you...

## About
* Hamara Paryatan Katai Jahar is a project for developing Indian Tourism sector. We have build a solution to count the number of tourist in a specific part of a tourist place.<br>
* We are counting people by using our Human Detection System and plotting density graph on the heritage place map, which helps tourist to plan thier trips and helps rescue forces to identify people in case of emergencies.

## Installation Requirements and Guidelines
* Since this project is for human detection as such we need set of cameras to run this project.
* To run this system you need some packages pre-installed
  * Python
  * Python-dev tools
  * OpenCV
  * Keras
  * Tensorflow
  * Numpy, Pandas, Matplotlib
  * MariaDB
* Run the ```detection.py``` file in order to start the human detection system.
* Run the ```project.py``` file to start listening for the count.
* The whole project is accessible to users via our website, it is located in ```UI/index.html``` file.

## Systems required to run this project
* Basically we need 2 systems for the project execution
  1. One system is hosted on AWS containing the ```project.py``` listener and also containing the website files.
  2. The second system will be installed at the heritage place security server room, which will be used to connect to cameras and run the human detection system.

## Process flow of the project
1.  The ```detection.py``` file will use an alogorithm to detect human beings using the video foutage provided by the video cameras attached to the system.
<br><b>Note This system requires huge computation power</b>
2. The file will generate a count and send this via a socket to the another system.
3. On the other hand the system hosted on AWS will recieve the count via a socket within the ```project.py``` file.
4. The file will apply colors on the map which will represent the density of the crowd in a particular place of the Installed site.
5. The website login page is hosted on the AWS ```/var/www/html``` and it uses the user login credentials to create a docker container with a random available port and redirects the docker container as a website to the user.
6. As such every user accessing the website is isolated in the docker container.
7. The website contains an ```iframe``` of map which refresh itself every ```10``` seconds to update the density plot on it.
8.  The map is an image which is dynamically updated by the ```project.py``` as per the change in density.

## Presentation Link
* We have prepared a presentation for the project and it is available below
http://bit.ly/Hamara-Paryatan-Katai-Jahar
