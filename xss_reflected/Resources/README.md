Sooo the url is a very big sign page=media&src=nsa.
If we change the value of src for 'test', we find 'test' inside the source code.

We then try to do a alert() inside but doesn't work because some chars are encoded.
This is were we try do "hide" our chars. We use the object tag to decode our code.

So we encode <script>alert()</script> in base64 and will be decoded after the sanitize.
http://<ip>/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgpPC9zY3JpcHQ+
