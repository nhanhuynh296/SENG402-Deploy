cd ../server
python3 -m venv ./server/venv
gunicorn --bind 0.0.0.0:5000 run:app
sudo nano /etc/systemd/system/seng402.service

```
[Unit]
Description=Gunicorn instance to serve seng402
After=network.target

[Service]
User=tnh33
Group=www-data
WorkingDirectory=/home/tnh33/seng402-deploy/server
Environment="PATH=/home/tnh33/seng402-deploy/server/bin"
ExecStart=/home/tnh33/seng402-deploy/server/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 run:app

[Install]
WantedBy=multi-user.target
```

sudo systemctl start seng402
sudo systemctl enable seng402


root /var/www/html;

sudo systemctl restart nginx
cd /etc/nginx/sites-enabled
sudo nano seng402-front.conf

npm run build && sudo cp -r ~/seng402-deploy/client/dist /var/www/

curl localhost:5000

systemctl status seng402

/home/tnh33/seng402-deploy/server/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 run:app

cd ~/seng402-deploy/client/src/components