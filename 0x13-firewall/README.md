<p align="center"><img src="https://github.com/facu2279/holberton-system_engineering-devops/blob/master/0x08-networking_basics_2/holberton-logo.png"/></p>
<br>
<h1 align="center">0x13. Firewall</h1>
<br><br>
<p align="center"><img src="https://github.com/facu2279/holberton-system_engineering-devops/blob/master/0x13-firewall/firewall.png"/></p>

## More Info
As explained in the web stack debugging guide concept page, telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on web-02:

```
facundo@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
facundo@ubuntu$
```

We can see for this example that the connection is successful: Connected to web-02.holberton.online.

Now lets try connecting to port 2222:

```
facundo@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
facundo@ubuntu$
```

We can see that the connection never succeeds, so after some time I just use ctrl+c to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will be originating from web-02 and not from the schools network, bypassing the firewall.

<b>Warning!
Containers on demand cannot be used for this project (Docker container limitation)

Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.
</b>
<br><br>
<p align="center"><img src="https://github.com/facu2279/holberton-system_engineering-devops/blob/master/0x13-firewall/tutorial.png"/></p>
<br>

# Authors
Made by [Facundo Diaz](https://github.com/facu2279) to Holberton School 2021

Social Networks
-------------------
- [Linkedin](https://www.linkedin.com/in/facundo-d%C3%ADaz-720110149/)
- [Twitter](https://twitter.com/facudiazuy)