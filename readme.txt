per ambiente virtuale:
-cd C:\Users\Admin\Desktop\PythonBot
-python -m venv .venv  (creo l'ambiente virtuale)
-cd .venv
-cd Scripts
-cd activate.bat    (avvio l'ambiente virtuale) per disattivare uso deactivate.bat

-cd .. (per tornare indietro nella directory)

-pip install per installare nuove librerie

-pip freeze > requirements.txt per generare il file con le dipendenze per server heroku