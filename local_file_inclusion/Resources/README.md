LFI exploit:

If you watch the url when you go on a page you can see that there is a tag page=<something>
And that give us the chance to look for file on the actual server.
Because we are not looking for file that renders the page but some internal files.

Just try the http://ip/?page=hey
There is a pop-up --> Huge clue

keep adding ../ before etc/passwd and here you go
http://192.168.1.16/?page=../../../../../../../etc/passwd
