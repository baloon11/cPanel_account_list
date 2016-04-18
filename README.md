#### cPanel API Django web-application. Getting info about accounts.
This Django web-application performs the task of determining the number of accounts of the list of cPanels.

#### Overview
Suppose, you have a few cPanels and you need to get info about the number of accounts on each of them.  
You may to deploy this Django project on own server or locally to get this information.


The app gives you the opportunity to survey cPanels after pressing the special button or  
you always can see the actual information that the app gets using custom Django command and cron.

#### Usage

This project uses `SQLite3`.  
So you need to create it and syncronize with models:  
    `python manage.py syncdb`

Create superuser:  
    `python manage.py createsuperuser`  

Also you need to add custom Django command in cron  
(This following example assume that you are using a virtualenv):  

###### Ubuntu  
in console `crontab -e`  
Then add this command in the file:  
`*/5 * * * * /path/to/virtualenv/bin/python /path/to/project/manage.py checking_by_cron`

###### In CentOS,
maybe, you need to do something like this:  
in console `vim /etc/crontab`  
Then add this command in the file:  
`*/5 * * * * root /path/to/virtualenv/bin/python /path/to/project/manage.py checking_by_cron`  
Where `checking_by_cron` is custom Django command.

Then in the Django admin panel you need to add cPanel`s domains and log/pass for each of them.


#### Requirements
    Python 2.7.10
    pip install pycpanel==0.1.5
    pip install Django==1.6


#### Note
If you want to use this functionality as console script  
you can use this repository:  
`https://github.com/baloon11/cPanel-API-python-script-Getting-info-about-accounts`
