Thanks to the comments on the page with the albatross, we learn that we must access the page from https://www.nsa.gov/ using the browser "ft_bornToSec".

"You must come from: https://www.nsa.gov/"

"Let's use this browser: ft_bornToSec. It will help you a lot."

We can deduce that we need to send a special request by modifying the Referer and User-Agent headers.

Referer corresponds to the referring page from which users access the page.

User-Agent corresponds to the browser used to access the page.

Full command:
curl 'http://192.168.1.33/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' \
  -H 'User-Agent: ft_bornToSec' \
  -H 'Referer: https://www.nsa.gov/'