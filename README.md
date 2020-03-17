# Hitchhikers guide to galaxy door

The first time I watched the movie Hitchhiker's Guide to the galaxy I had a great laugh. Especially the part where they enter the Space ship with the sighting doors. Check it out [here](https://www.youtube.com/watch?v=jn3Vv6VYdxw). Anyway, I immediately thought how hard can it be to make this happen in the world of minicomputers and cheap sensors. So I gave it a go.

## Requirements

Let me first share my shopping list required for this project. First, you need a [Raspberry Pi 3 b+](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07P4LSDYV) (overkill, but I had one laying around) and a [door sensor switch](https://pixelelectric.com/mc-38-wired-door-sensor-switch/) to be able to determine if the door is open or not. Additionally, you need some kind of speaker. I wanted to try out this [one](https://www.monkmakes.com/pi_speaker_kit/), but I guess any speaker that has an AUX cord will do.

## Wiring

The wiring is super easy and does not require any soldering. In my case, I needed to connect my speaker to the 5V and to the ground. To be able to use my code directly connect the door sensor to the Raspberry pin 18 and that's it.

## Connect and deploy

Connect to the PI via ssh and clone the repository. In my case the name of the Pi is galaxy.

```bash
    ssh pi@galaxy.local
	git clone git@github.com:alexus37/hg2gDoor.git
```

## Code overview

The whole code required is basically in the file `main.py` and it loads all the audio samples (different sighs for more variety) and uses pygame to play them if the door state changes.

## Autostart

If you want to add the script to the autostart folder run:

```bash
    crontab -e
```

and add the following lines

`@reboot python3 /home/pi/hg2gDoor/main.py >>/home/pi/log.txt 2>&1 &`
