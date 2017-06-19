Title: Projects
Date: 2017-05-17 22:48
Author: Herman Tong

##<center>**Projects**</center>
---

###<center>**Texas Hold'em Simulation with AI**</center>

<center>![Alt Text]({filename}/images/TexasHoldem.png)</center>

This is a fully implemented command-line based Texas Hold'em Poker Game with odd
calculation. ASCII graphics and AI players using C++. It follows the fixed limited 
betting and ante rules. It utilizes the STL::&lt;unordered_map&gt; to store rankings
of different hands and uses the Monte Carlo approach to simulate the probability
of winning based on player's hand and the community cards.

<center>![Icon]({filename}/images/github2.png)[ Click here for Texas Hold'em repository ](https://github.com/tkherman/Texas-Hold-em-Game)</center>

---

###<center>**Web Server**</center>

<center>![Alt Text]({filename}/images/spidey.gif)</center>

In my system programming course, one of the final projects was to create a web
server which can handle file requests, CGI script requests and directory
browsing requests. It was implemented using C system calls and can handle
request one by one or by forking. A python script and several shell scripts were
also created to benchmark the latencies and throughputs for forking and
single. To see results of the benchmark and analysis, please click the link
below to the blog post or read the README.md in the Github repository.

p.s. The thumbnail picture is a meme of one of my group members

<center>![Icon]({filename}/images/blog.png)[ How forking affects latency and throughput of server ](http://tkherman.github.io/how-forking-affects-latency-and-throughput-of-web-server)</center>
<center>![Icon]({filename}/images/github2.png)[ Click here for Web Server repository ](https://github.com/tkherman/Spidey-Webserver)</center>

---

###<center>**Partial re-implementation of find**</center>

This is an partial re-implementation of the linux __find__ command using C system
calls that deal with files, directories, and processes. Similar to __find__,
__search__ recursively searches a directory and prints items it finds based on
the specific options:


$ ./search -help

Usage: ./search PATH [OPTIONS] [EXPRESSION]

Options:

    -executable     File is executable or directory is searchable to user
    -readable       File readable to user
    -writable       File is writable to user

    -type [f|d]     File is of type f for regular file or d for
                    directory

    -empty          File or directory is empty

    -name  pattern  Base of file name matches shell pattern
    -path  pattern  Path of file matches shell pattern

    -perm  mode     File's permission bits areexactly mode (octal)
    -newer file     File was modified morerecently than file

    -uid   n        File's numeric user ID is n
    -gid   n        File's numeric group ID is n

Expressions:

    -print          Display file path (default)
    -exec cmd {} ;  Execute command on path

<center>![Icon]({filename}/images/github2.png)[ Click here for Search repository ](https://github.com/tkherman/search)</center>
