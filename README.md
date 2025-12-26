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
```bash
uv run python src/hello.py
```

**Note** : Si le lien symbolique `.venv` est supprimé, vous pouvez le recréer avec :
```bash
ln -s reachy_mini_env .venv
```
