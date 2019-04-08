# Affichage sur écran LCD

Sur ce repesitory vous trouverez le script `lcd.py` et le `Dockerfile` nécessaire pour build l'image permetant d'éxécuter le script lcd.py
qui permetra l'affichage (comme sur un écran LCD de 3X3) du nombre.

Pour tester le script, il vous suffit de clone le repository, et de build l'image avec la commande `docker build -t lcd .`, puis ensuite 
d'éxécuter la commande suivant `docker run lcd python /src/lcd.py 129864758` oú `129864758` est votre nombre.