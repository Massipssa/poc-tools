source .env
echo "Create dist package"
python setup.py sdist bdist_wheel

echo "Upload the package using twine"
twine upload -u "$TWINE_USERNAME"\
      -p "$TWINE_PASSWORD"\
      --repository-url "$TWINE_REPOSITORY_URL"\
       dist/*