# Space Telegram

This project helps to download photos from NASA resources and post them in your Telegram channel.

## How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/)

---
## save_images_helper
The main script, which helps to download images

## fetch_spacex_images

This script helps to download photos from SpaceX flights. You can add id of flight to download images from it.
If you don't add ID, script will download images from the latest flight (it can often be empty)

## fetch_apod_images

This script helps to download NASA picture of the day. You can add the number of images you need.

## fetch_epic_images

This script helps to download Earth photos depending on the date.

## telegram_bot

Here is the data for your Telegram bot. You can use it to download pictures.

## post_images_to_channel

Here is the logic for sending photos to your Telegram channel