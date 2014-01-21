current_pip=`which pip`
if [[ ${current_pip} == '/usr/local/bin/pip' ]];
then
  echo It seems that no virtualenv has been activated
  echo Please, activate this virtualenv before building the project
  exit -1
fi

echo "## Installing requirements"
pip install -r requirements.txt


echo
echo "## Sweet. You the project has been built."
