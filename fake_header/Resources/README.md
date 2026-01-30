 grace aux commentaires de la page avec l'albatros, on apprend qu'on doit arriver sur la page depuis https://www.nsa.gov/ avec le navigateur "ft_borntoSec"

" You must come from : "https://www.nsa.gov/". "

" Let's use this browser : "ft_bornToSec". It will help you a lot. "

on devine qu'on doit envoyer une requete spéciale en modifiant les champs Referer et User-agent qui correspondent respectivement à la page référente à partir duquelle les personnes accèdent à la page pour 'Referer'; et le navigateur (browser) depuis lequel une personne se connecte à la page (user-agent)

commande complète

curl 'http://192.168.1.33/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' -H 'User-Agent: ft_bornToSec' -H 'Referer: https://www.nsa.gov/'