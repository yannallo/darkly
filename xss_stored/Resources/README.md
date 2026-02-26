There is an XSS.

In the 'Leave a feedback' but not in the message part.
So basically we just write some code to be executed in a certain way.
Here we do a simple <script>alert()</script> --> a html tag that allow to execute some code.

BUT here we do not use it in the Message section because it is not working.
IF you try in the Name section it just magically work even if its not shown in totally.
