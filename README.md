# cowin-jab-alert

This is a simple web scraper which will use cowin web APIs and will play alert music if slot is available for 18-44 age group in the given pincode.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
1. git client
2. python3
```

### Installing

Go to any folder in your windows machine.

```
git clone https://github.com/arunbhaud/cowin-jab-alert.git
```

now go to folder cowin-jab-alert and open the command prompt and install following dependencies using pip command

```
pip install requests

pip install playsound
```

Now run sample program which will play alert music after 7th iteration for demo purpose using below command -

```
py cowin_jab_demo_alarm.py

This will ask you to enter the pincode. Please enter the pincode of your area and continue.

Its will use the cowin API to search the slot for next 7 days from today with age limit 18-44

```

If the above demo program plays the alert music then everything is set. 

You can increase the volume of your speaker if the music is played at very low volume ;)


Now run actual program which will play alert music as soon as the slot is available -

```
py cowin_jab.py

This will ask you to enter the pincode. Please enter the pincode of your area and continue.

Its will use the cowin API to search the slot for next 7 days from today with age limit 18-44

As soon as the slot is available, alert music will be played!
```

## Authors

* **Arun Bhaud** - *Initial work* - [abhaud](https://github.com/arunbhaud)

See also the list of [contributors](https://github.com/arunbhaud/cowin-jab-alert/graphs/contributors) who participated in this project.

## License

This project is licensed under the MOT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://apisetu.gov.in/public/api/cowin

