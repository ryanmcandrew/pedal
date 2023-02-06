sudo snap install androidsdk
sudo apt install cython
sudo ln -s /usr/bin/cython3 /usr/local/bin/cython    

git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
cd /project/folder
buildozer init

buildozer android debug deploy run