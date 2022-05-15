# anime-pfp-detection
This selfbot relies on [animeface-2009](https://github.com/nagadomi/animeface-2009)

# Building
Requirements:
* Ruby
* ImageMagick
* GCC
* Make
* Python 3

Installing Requirements:
On Debian/Ubuntu-derived distributions:
```
sudo apt-get install ruby gcc make python3 libmagickwand-dev
sudo gem install rmagick
```

On Arch-based distributions:
```
sudo pacman -S yay
yay -S imagemagick-full ruby-rmagick ruby python3
```

After installing requirements git clone this repo and cd into it then run `chmod +x ./build.sh && ./build.sh`

After building completes, move the `animeface-ruby` directory to your home folder. *eg. `mv animeface-ruby ~/`*

# Usage
Edit run.py and put your token in, then simply run `python3 run.py`. After that edit t.sh and put your IMGBB API key in

In order to check for an anime pfp simply do `,avatar @user`




Do note that this is just a fun little side-project, and is pretty much useless.
Oh and btw this isn't well documented, I'll do that later.
