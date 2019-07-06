# हमारा पर्यटन कतई जहर
aap camera ki nazar mai hain....

## Contributing

Read the [Contributing Guidelines](https://github.com/Abhinaay/Hamara-Paryatan-Katai-Jahar/blob/master/CONTRIBUTING.md) before making a contribution. Please follow the [Pull Request Template](https://github.com/Abhinaay/Hamara-Paryatan-Katai-Jahar/blob/master/PULL_REQUEST_TEMPLATE.md) while making a PR. Please follow the [Code of Conduct](https://github.com/Abhinaay/Hamara-Paryatan-Katai-Jahar/blob/master/CODE_OF_CONDUCT.md)

## About

This is the data and program for human detection, I have turnoff the visual output, right now the program only display no of humans in the range(rangerexit).

## Requirment and Usage

1) Required Library are:
  opencv
  tensorflow
  numpy
  time

2) To install required library run command [pip install -r Requirement.txt]
   or just run the program once it will install required library by itself

3) Run the program using python detection.py direct run is not working resolving that issue soon

4) Usage:
  Currently the program take video input from main camera (0) if you want to change it to another video or camera just change video variable according to the requirements

  This Program will record initial no of humans in the frame and display it and next time if the no of humans decrease or increase by 3 it will update the no of humans

  The value can be increased or decreased by changing Ranger variable in the program
