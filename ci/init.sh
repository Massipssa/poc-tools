set -e

source .env

function package() {
  echo "-------------------------------"
  echo "Create dist package"
  echo "-------------------------------"
  python setup.py sdist bdist_wheel
}

function upload() {
  echo "-------------------------------"
  echo "Upload the package using twine"
  echo "-------------------------------"
  twine upload -u "$TWINE_USERNAME"\
      -p "$TWINE_PASSWORD"\
      --repository-url "$TWINE_REPOSITORY_URL"\
       dist/*
}


while (( "$#" )); do
  case "$1" in
    --help)
      echo "--help"
      exit 0
      ;;
    --package)
      package
      shift 1
      ;;
    --upload)
      upload
      shift 1
      ;;
    *)
      break
      ;;
  esac
done
