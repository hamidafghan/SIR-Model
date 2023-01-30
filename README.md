# SIR MODEL

`python3 main.py`

Here is a tiny example how to model the social contagion and plot the SIR.

In `utils/Graph.py` file, you may customize to your own graph.

To simulate the SIR model on the graph performed the following actions:

1. Initialized the initial values (infection rate, recovery rate, number of ini-
   tially infected nodes, the minimum number of times for a node to be in
   infection)
2. Change all node’s colors to blue and label them ”S” and initialized the
   time tracker
3. Infect the randomly the initially infected nodes (Change the label to ”I”
   and color to red)
4. Loop of the neighbors of infected nodes and infect them if the random
   probability is less than the infection rate (as per instruction). Recover the
   node if the random probability is less than the recovery rate and the node
   was infected a minimum number of times.
5. Continue loop until all nodes get recovered
6. Print the steps, number of infected notes, and number not infected at all
   nodes.

### Output

- It generates images of each step in `/images` directory.
- It merges the generated images to a single file as video `./movie.mp4` file. \*

### Notes

In order to generate the movie you need to install `ffmpeg` on operating system level.

<br />
ubuntu:

`sudo apt install ffmpeg`

`ffmpeg -version` to verify installation

<br/>
macOS:

`brew install ffmpeg`
More details [here](https://formulae.brew.sh/formula/ffmpeg)

<br/>
Windows:

`I don't know :)`

<br/>
Thanks :)
