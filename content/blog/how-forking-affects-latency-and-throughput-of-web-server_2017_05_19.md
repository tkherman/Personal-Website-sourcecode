Title: How forking affects latency and throughput of web server
Date: 2017-5-19 19:09
slug: how-forking-affects-latency-and-throughput-of-web-server

The web server called Spidey is split into multiple files which have different
functions that carry out different jobs. It is organized so that it can process
requests in parallel and not in parallel. 

socket.c:

+ create socket, bind socket to a specific port and listen for incoming
connection
+ returns a file descriptor

request.c:

+ parse the HTML request
+ save request info such as method, uri, query, header etc in a **struct request**
+ provide function to free the allocated **struct request**

handler.c:

+ determine the type of request
+ return appropriate files to client according to the file type
+ handles HTML, static files and CGI Scripts

single.c:

+ repeated accept request, handle request and free request in a single while loop

forking.c:

+ repeated accept request
+ fork a new process and have the child process handle request
+ free struct request in parent process

spidey.c:

+ parse the command argument for starting server
+ allow user to decide the method of handling request, port, root directory...

##<center>Forking and how it works in Spidey</center>

To process requests in parallel, the server utilizes **forking**. Forking is
when a process spawns another process to carry out some task. The spawned
process is called the child process while the spawning process is the parent
process. To process requests in parallel, the server waits for incoming
requests. When a request arrives, the server first accept the request and parse
it. Then, it forks a child process to handle the request.

In general, when a parent process creates a child process, the parent process
would wait for the child process to complete the task and exit using the wait()
system call to prevent zombies. However, in order for the server to process
requests in parallel, the server instead ignores the child so that multiple
child processes can be forked and work in parallel.



##<center>Benchmark</center>

Since the server can run in both parallel and non-parallel, it could be used to
benchmark the performance of the server when using forking and when not using
forking. To do so, a python script called thor.py was created that is used to
send multiple requests to a server. thor.py takes in number of processes and
number of requests as the argument and send multiple requests according to them.

The web server was benchmarked by measuring the average latency of different
types of requests using 1, 2, and 4 processes on 100 requests. The average
throughput was also measured. Dummy files of 1KB, 1MB, and 1GB were created and
throughput was calculated by dividing the size of the file by the time it took
for the request to complete.



#<center>Table for Latency Tests</center>

| Mode    | File Type   | Number of Processes | Time  |
|---------|-------------|---------------------:|-------:|
| Single  | Directory   | 1                   | .0059 |
| Forking | Directory   | 1                   | .0061 |
| Single  | Directory   | 2                   | .0081 |
| Forking | Directory   | 2                   | .0075 |
| Single  | Directory   | 4                   | .0161 |
| Forking | Directory   | 4                   | .0147 |
| Single  | Static File | 1                   | .0060 |
| Forking | Static File | 1                   | .0061 |
| Single  | Static File | 2                   | .0081 |
| Forking | Static File | 2                   | .0074 |
| Single  | Static File | 4                   | .0160 |
| Forking | Static File | 4                   | .0143 |
| Single  | CGI Script  | 1                   | .0145 |
| Forking | CGI Script  | 1                   | .0146 |
| Single  | CGI Script  | 2                   | .0254 |
| Forking | CGI Script  | 2                   | .0161 |
| Single  | CGI Script  | 4                   | .0515 |
| Forking | CGI Script  | 4                   | .0344 |



#<center>Table for Throughput Tests</center>

| Mode    | File Size | Average Throughput (GB/s) |
|---------|-----------:|---------------------------:|
| Single  | 1 KB      | .036                      |
| Forking | 1 KB      | .040                      |
| Single  | 1 MB      | 29.3                      |
| Forking | 1 MB      | 35.2                      |
| Single  | 1 GB      | 44.7                      |
| Forking | 1 GB      | 94.7                      |


The results clearly display that forking to handle requests has both advantages
and disadvantages.  When running in forking mode, the parent process forks to
create a new child process to handle get requests.  This way, the parent can
focus on accepting requests while delegating the handling of these requests to
children (which gently kill themselves when they finish). Although forking isn't
always beneficial because there's overhead cost in creating a new process, it
seems that forking is mostly beneficial in the above example.

As noted above in our markdown tables, all of our tests with forking show 
significant advantages over single processing.  For instance the test with 
forking for the 1GB file yielded a throughput over twice as high as the 
analogous single processing test.  The only tests in which single processing 
performed better were the latency tests with one process and (100 requests). 
This makes sense because much of the benefits of forking are lost when only 
using one process, so the overhead of forking worsened performance as explained 
above.
