# reachy_mini-kikito

## Environnement virtuel

Ce projet utilise `reachy_mini_env` comme environnement virtuel.

Un lien symbolique `.venv -> reachy_mini_env` a été créé pour que `uv` trouve automatiquement l'environnement virtuel.

Pour créer ou synchroniser l'environnement virtuel avec `uv`, utilisez :
```bash
uv venv reachy_mini_env
uv sync
```

Pour exécuter un script Python :

**⚠️ Important : Connexion réseau requise**
Le terminal intégré de Cursor bloque l'accès réseau (sandbox), ce qui empêche la connexion au robot Reachy Mini. **Vous devez exécuter le script depuis un terminal externe** (Terminal.app, iTerm2, etc.).

**Option 1 : Utiliser le script shell (recommandé)**
```bash
./run.sh
```

**Option 2 : Exécuter directement avec uv**
Depuis un terminal externe :
```bash
cd /Users/franckmarandet/Documents/WORK/ALFRED/Reachy/Kikito
source reachy_mini_env/bin/activate
uv run python src/hello.py
```

**Note** : Si le lien symbolique `.venv` est supprimé, vous pouvez le recréer avec :
```bash
ln -s reachy_mini_env .venv
```
