git checkout master
git config core.filemode false
pip install -r requirements.txt --use-mirrors
rm -rf content
python github.py
make clean
make publish
git checkout gh-pages
cp output/index.html index.html
cp -r output/theme .
git add index.html theme/
git commit -m "drone.io commit"
git remote set-url origin git@github.com:NikhilKalige/pelican-plugins-site.git
git push origin gh-pages
