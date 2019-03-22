# VOC

Website for the VOC Foundation of South Africa, running on Django.


## TODO

- fix markdown tag
- add all links to research items
- document management
- navigation
- image management
- get dates for past news items
- news items and feed
- project register
- map
- video of locks lecture
- event calendar
- setup email forwarders and mailing list
- medal winners
- notify other sites of domain change

## Other sites and societies

- VOC Kamer Antwerpen
- Van Riebeeck http://www.vanriebeecksociety.co.za
- Van der Stel http://www.simonvdstel.org/
- SASNEV http://www.sasnev.co.za

## Quick deploy

**local**

rsync -r -zz -h --progress voc content templates media core manage.py .env.example requirements.txt <server>:<location>

**server**

python3.6 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python manage.py collectstatic

