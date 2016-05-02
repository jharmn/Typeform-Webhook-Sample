rm db/formconf.db
python create_db.py
nohup python app.py > /dev/null 2>&1 &
sleep 2
resttest.py http://localhost:5000 test/test.yaml
pkill -f 'python app.py'
