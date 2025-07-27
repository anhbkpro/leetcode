## Alias collections
```bash
cd utility
chmod +x install_aliases.sh
./install_aliases.sh
source /Users/anh.lai/.zshrc
```

## Virtual environment

1. Create virtual environment:
```bash
python -m venv venv
```
1. Activate virtual environment:
```bash
source .venv/bin/activate
```
1. Verify activation:
```bash
which python
python --version
pip list
pip install -r requirements.txt
```
1. Deactivate
```bash
deactivate
```

## Run tests
```bash
# Built-in unittest
python3 -m unittest intervals/summary_ranges_test.py -v

# Pytest
pytest intervals/summary_ranges_test.py
pytest intervals/summary_ranges_test.py -v
```
