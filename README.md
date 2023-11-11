# Space Telegram

This project helps to download photos from NASA resources and post them in your Telegram channel.

## How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## Environment variables

Before launching the script, create an .env file in your project directory (or in the root of your project).

At first, Get your APOD key [here](https://api.nasa.gov/#apod). Put your APOD key into the .env file and assign its value to the new environment variable. For example:

```python 
APOD_KEY="your_APOD_key_here"
```
Then create new Telegram bot with the help of @BotFather (you can find it in Telegram) and get your API token from it.
Create new variable in the same .env file and put your token here. For example:

```python 
TOKEN ="your_telegram_token_here"
```
At last create new Telegram channel and make your bot the admin in it. Invent a name for your channel and put it 
in a new variable in the same .env file. For example:

```python 
CHAT_ID = "@my_photo_channel"
```

---
## save_images_helper

This script contains all necessary logic for downloading images.

## fetch_spacex_images

This script helps to download photos from SpaceX flights. You can

### How to launch:

Run the script and add ID of flight as an argument to download images from it.
You can find ID [here](https://api.spacexdata.com/v5/launches/). Example:

```
python path_to_file\post_images_to_channel.py --spacex_id "5eb87ce4ffd86e000604b338"
```
If you don't add ID as an argument, script will download images from the latest flight (note that not every flight has images from the launch).

## fetch_apod_images

This script helps to download NASA picture of the day. You can add the quantity of images you need.

### How to launch:

Change the number of images you need in this fragment of code:

```python 
apod_payload = {'apod_key': apod_key, 'count': number_of_images}
```
Run the script:

```
python path_to_file\fetch_apod_images.py
```

## fetch_epic_images

This script helps to download Earth photos depending on the date.

## How to launch:

Run the script:

```
python path_to_file\fetch_epic_images.py
```
## telegram_bot

This script stores the data for creating your Telegram bot.
You can use it to send pictures directly to your Telegram channel.

## post_images_to_channel

This script sends pictures to the Telegram channel.

## How to launch:

If you run the script without any arguments, it will send a random picture to your channel.

If you want to use a custom delay between sending images to your channel, use the following code.
You can use any time in seconds.
Without this argument the delay between sending images is equal to 4 hours.

```
python path_to_file\post_images_to_channel.py -delay_time 5
```

If you want to send chosen picture, use the following code:

```
python path_to_file\post_images_to_channel.py --image_name "image.jpg"
```

If you want to send images to you channel in infinite loop, use the following code:

```
python path_to_file\post_images_to_channel.py --infinite_loop
```

---
## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/)