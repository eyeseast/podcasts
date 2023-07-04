# Podcasts

This is a script to download podcast audio files -- MP3, M4A, etc -- from a collection of feeds, without a dedicated podcast app. It will put files in a `podcasts` folder. You can then copy those files onto the player of your choice.

This works because pocasting is still based on the open RSS standard, and files are hosted on public servers. This is what your podcast player is doing under the hood.

## Caveat Emptor

This script is going to download files from the internet and save them onto your computer. **Make sure you know what you're downloading.**

The author of this script is not responsible for anything that goes wrong. Use at your own risk.

## Usage

To subscribe to feeds, you'll need the RSS link for the podcast of your choice. I've included three my oldest likes -- [But Why](https://www.npr.org/podcasts/474377890/but-why-a-podcast-for-curious-kids), [Circle Round](https://www.wbur.org/podcasts/circleround) and [Million Bazillion](https://www.marketplace.org/shows/million-bazillion/). A URL for each feed goes on its own line in `feeds.txt`, like this:

```
https://podcasts.vpr.net/but-why
https://rss.wbur.org/circleround/podcast
https://www.marketplace.org/feed/podcast/million-bazillion
```

### Install the script

Double click the `Install.command` icon. This will open a Terminal window and run a script that installs Python dependencies inside this directory. It shouldn't need any new permissions to run and won't touch anything outside this directory. Close the Terminal window when it finishes running.

### Download podcast episodes

Double click the `Update.command` icon. This will open another Terminal window and run another script. This will read through the URLs in `feeds.txt`, find each audio file and download it to a `podcasts` folder in this directory. Each file is named with the episode title.

### Copy files to your player

Different players are going to need files in different places. On mine, there's a `podcasts` folder. I copy all my new files into it, and that's it. Yours might be different. When in doubt, read the instructions.

## Backstory

I bought a [SanDisk Clip Player](https://a.co/d/drfuW2D) to let my kids have their own podcasts in the car. However, it needs actual MP3 files and has connection to the internet, and most of the podcasting ecosystem has moved toward native apps like Apple Podcasts or Overcast.

Downloading podcasts, getting to the actual files and giving them sensible names turns out to be [more difficult than it should be](https://discussions.apple.com/thread/254493062). This is an effort to fix that problem, without building a new, full-fledged desktop application.
