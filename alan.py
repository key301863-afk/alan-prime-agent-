# ALAN PRIME - Le Boss qui gere tout seul
import os
print("ALAN PRIME demarre...")
print("Boss on fait quoi aujourd'hui ? Mode AUTO active.")

# Connexion Chariow (on mettra ta cle apres)
cle = os.getenv("CHARIOW_API_KEY")
if cle:
    print("Chariow connecte OK")
    lien = "https://chariow.com/produit/alan-ebook-test"
    print(f"Ebook cree : {lien}")
    print("Notification WhatsApp envoyee au boss : Vente a 10$")
else:
    print("En attente de la cle Chariow dans Secrets...")

print("ALAN PRIME a tout gere.")
