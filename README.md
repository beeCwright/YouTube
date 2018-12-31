# YouTube
Python script and Dockerfile for using pytube to download songs from YouTube. Reads a .csv called urls.csv which contains youtube urls. 

### Usage
(1) Build the Docker image, where X.X is the version of this repo. E.g) v0.2
`docker build -t youtube:vX.X .`
(2) Run a container and specify the host mount location 
`docker run --name yt_downloader -v /path/to/downloads/folder/:/downloads youtube:vX.X`

Music will be downloaded into the downloads folder. Successes and failures are printed to the terminal.


### TODO:
- Check that urls.csv exists
- Check that the downloads folder exists
- Find a better way to manage shared storage, {volumes, smarter bind mountings, docker-compose}
- A downloads manager GUI would be nice
