# zahnarztlampe
for addressing typ_o's udp rgb lamp

accepts UDP packages on port 2390

packages have to look like this:

###R:G:B

values for the colors can be between 0 and 255

example nc command for testing:
```
echo -n "255:0:0" | nc -4u -w1 192.168.3.102 2390
```

