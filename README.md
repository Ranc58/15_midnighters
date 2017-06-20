# Night Owls Detector

This program print out [DevMan](https://devman.org) students, who sent work after 12pm.

# How to install
1. Recomended use venv or virtualenv for better isolation.\
   Venv setup example: \
   `python3 -m venv myenv`\
   `source myenv/bin/activate`
2. Install requirements: \
   `pip3 install -r requirements.txt` (alternatively try add `sudo` before command)

# How to use

You can use argument `-t` to specify end time. It must be in this 24h format: `Hours:Minutes`.\
If you don't specify argument, program used default value for end time: 06:00.\
Run example on linux:
```
$ python seek_dev_nighters.py -t 5:00
User "desolator27" sent work at 02:06
User "rvota007" sent work at 01:42
User "AnatolioBambino" sent work at 01:13
User "galbator1x" sent work at 02:01
User "galbator1x" sent work at 01:56
User "СергейАнатольевич" sent work at 00:15
User "id20889227" sent work at 01:06
User "KhorinVitaly" sent work at 00:03
User "galbator1x" sent work at 00:02
User "DmitriiSokolov" sent work at 01:12
User "vgrishkin" sent work at 00:19
User "СергейИванов" sent work at 00:35
User "profactum" sent work at 03:47
User "profactum" sent work at 03:39
User "alexander.i.kamenev" sent work at 00:28
User "АннаБурденко" sent work at 00:12
User "id15856034" sent work at 01:58
User "KonstantinNaumov" sent work at 00:09
User "id54808965" sent work at 02:58
User "IgnatPetrenko" sent work at 02:36
User "alexander.i.kamenev" sent work at 02:12
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
