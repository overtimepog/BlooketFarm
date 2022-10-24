
# Blooket Farm

A tool to farm Coins and XP from Blooket


## Support

For support, join the server https://discord.gg/3YktCmHw4e.


## FAQ

#### Do you see what I put in the .env file?

No, The Values in the .env file are only visable to you :)


## Installation

git clone the Farm and install the requirements

```python
  git clone theproject.git
  cd my-project
  pip3 install -r requirements.txt
```
please also change the name of the ```.env.example``` file
to ```.env```

it should look like this:
```
  username=
  password=
  blooket=
```

#### .env values
Blooket Account **can not** be google login only, must be regular acccount.

| Value | Description                |
| :-------- | :------------------------- |
| `username` | **Required**. Your Blooket Account Username |
| `password` | **Required**. Your Blooket Account Password |
| `blooket` | Blooket to Farm (Can be left alone) |


#### Complete .env:
it should look like this:
```
  username=BlooketUsername
  password=BlooketPassword
  blooket=https://play.blooket.com/host?id=600b1491d42a140004d5215a
```


    
## Running

To run the Farm run the command:

```python
  python3 Farm.py
```

