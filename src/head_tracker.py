from reachy_mini import ReachyMini
import cv2

# Connect to the running daemon
with ReachyMini(localhost_only=False, timeout=15.0) as mini:
    print("Connected to Reachy Mini! ")

    # Test de la caméra
    print("Test de la caméra...")
    try:
        # Capturer une image depuis la caméra
        frame = mini.camera.get_frame()
        print(f"Image capturée avec succès! Taille: {frame.shape}")

        # Afficher l'image
        cv2.imshow("Reachy Mini Camera", frame)
        print("Appuyez sur une touche pour fermer la fenêtre...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Caméra fonctionne correctement!")
    except Exception as e:
        print(f"Erreur lors de l'accès à la caméra: {e}")

    print("Done!")
