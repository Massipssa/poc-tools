REQUIREMENT_FILE="requirements/requirements.txt"

echo "Create virtual environment"
python3 -m venv venv

echo "Install requirements"
pip install -r "$REQUIREMENT_FILE"

echo "Create python package"
wheel




