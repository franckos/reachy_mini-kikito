# reachy_mini-kikito

## Environnement virtuel

Ce projet utilise `reachy_mini_env` comme environnement virtuel.

Un lien symbolique `.venv -> reachy_mini_env` a été créé pour que `uv` trouve automatiquement l'environnement virtuel.

### Installation initiale

Pour créer ou synchroniser l'environnement virtuel avec `uv`, utilisez :

```bash
uv venv reachy_mini_env
uv sync
```

### Installation de reachy_mini_toolbox

Le package `reachy_mini_toolbox` doit être installé dans `reachy_mini_env` avec ses dépendances optionnelles :

```bash
# Activer l'environnement
source reachy_mini_env/bin/activate

# Installer reachy_mini_toolbox avec les dépendances vision
# Note : Utiliser des guillemets simples pour éviter les problèmes avec zsh
cd reachy_mini_toolbox
pip install -e '.[vision]'
cd ..
```

**Note importante pour zsh** : Les crochets `[]` doivent être échappés ou mis entre guillemets. Utilisez `'.[vision]'` ou `".[vision]"` au lieu de `.[vision]`.

## Exécution des scripts

**⚠️ Important : Connexion réseau requise**
Le terminal intégré de Cursor bloque l'accès réseau (sandbox), ce qui empêche la connexion au robot Reachy Mini. **Vous devez exécuter le script depuis un terminal externe** (Terminal.app, iTerm2, etc.).

### Scripts du projet principal

**Option 1 : Utiliser le script shell (recommandé)**

```bash
./run.sh
```

**Option 2 : Exécuter directement**
Depuis un terminal externe :

```bash
cd /Users/franckmarandet/Documents/WORK/ALFRED/Reachy/Kikito
source reachy_mini_env/bin/activate
python src/hello.py
```

### Exemples de reachy_mini_toolbox

Pour exécuter les exemples du toolbox (head tracking, etc.) :

```bash
# Activer l'environnement
source reachy_mini_env/bin/activate

# Exécuter un exemple
cd reachy_mini_toolbox
python examples/lookat_head_track_demo.py
# ou
python examples/head_track_demo.py
```

**Note** : Si le lien symbolique `.venv` est supprimé, vous pouvez le recréer avec :

```bash
ln -s reachy_mini_env .venv
```
