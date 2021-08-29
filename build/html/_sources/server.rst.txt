.. _server:

Server documentation
=====================

.. warning::
    Before making any changes to the experimental servers 
    make sure you check out the experiment `calendar <https://econlab.ucsc.edu/public/show_calendar.php/>`_ 
    so you don't make changes during someone else's experiment.

.. note::
    All servers use CentOS, so you use ‘yum’ to install packages.

.. note::
    Example files are hosted under the leeps@ucsc.edu Google Drive account

Experimental Servers
--------------------
* econ-leeps-3.ucsc.edu - Runs oTree 3
* econ-leeps-4.ucsc.edu - Runs oTree 3
* econ-leeps-5.ucsc.edu - Runs oTree 5

ORSEE
------
This stands for Online Recruitment System for Economic Experiments.

This is the website that is used to schedule experiments and invite subjects.

`ORSEE Documentation <http://www.orsee.org/web/>`_ 

`ORSEE Admin Page <https://econlab.ucsc.edu/admin/>`_ 


Main Website
-------------
`leeps.ucsc.edu <https://leeps.ucsc.edu/home/>`_ 

`Main Website Admin Page <https://leeps.ucsc.edu/admin/>`_ 


Server Maintenance Contact Information
----------------------------------------
Name: Doug Niven

Email: dniven@ucsc.edu

This is the person that will grant us new servers and SSL certificates.

If Doug is no longer available, contact UCSC ITS directly.


Reverse Proxy Service 
----------------------------------------
.. note::
    You need to be the root user to edit the Nginx configuration. You can do this by running ‘sudo -su root’.

Nginx is used for all the experimental servers and the Main Website. I'm not sure about ORSEE.

Nginx is also being used for SSL.

SSL certificates found in /etc/ssl 

Nginx config found in /etc/nginx/conf.d 

`Nginx Configuration Example <https://drive.google.com/file/d/17QIHpkjuK30eKnswYESwlwoccxd_T70X/view?usp=sharing>`_ 


Experimental Server Specifics
------------------------------

Required services
******************
* PostgreSQL
   * Make sure you pip3 install psycopg2-binary
   * `PostgreSQL Installation Tutorial <https://www.hostinger.com/tutorials/how-to-install-postgresql-on-centos-7/>`_
* Redis
   * `Redis Installation Tutorial <https://linuxize.com/post/how-to-install-and-configure-redis-on-centos-7/>`_
* Git
   * sudo yum install git
* Nginx
   * `Nginx Installation Tutorial <https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-7>`_
* Python 3.7
   * `Python 3.7 Installation Tutorial <https://tecadmin.net/install-python-3-7-on-centos/>`_
* Python virtual environment
   * `Python virtual environment Tutorial <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`_
* Tmux
   * sudo yum install tmux
   * `Refer to this to understand tmux <https://tmuxcheatsheet.com/>`_

Important Commands
*******************

.. note::
    Tmux allows you to continuously run services even when logging out

* tmux - Creates new tmux session
* tmux a - Attaches to last tmux session
* Ctrl + B + D - Detaches from current tmux session
* Ctrl + B + % - Creates new tmux pane
* Ctrl + B + (Arrow Key) - Move between tmux panes 
* Ctrl + B + [ - Allows you to scroll in a tmux window

Service Files
**************

.. note::
    Service files allow you to run processes in the background.

* `Service file tutorial <https://www.shubhamdipt.com/blog/how-to-create-a-systemd-service-in-linux/>`_  

Commands to know
```````````````````
* sudo systemctl start otree.service
* sudo systemctl restart otree.service
* sudo systemctl stop otree.service

If you would like to see the output of the service file run the command below:

.. note::
    I like to perform the command below in Tmux to show the output is saved even when I logout of the server.

.. code-block:: bash

    sudo journalctl -f -u otree.service

`Example service file <https://drive.google.com/file/d/13N89xUwcoNPd65XAkDuOG_-gQejAeIeu/view?usp=sharing>`_


Adding experiments
*******************
.. warning::
    Before doing this, ensure that all the data from other experiments have been downloaded.
    Make sure your project only contains your app, not the entire oTree configuration.

Steps
`````
* Git pull your project in the oTree folder and add it to settings.py
* Make sure you export the database URL before running the command below
   * export DATABASE_URL=postgres://postgres:password@localhost/django_db 
   * You can find the specific DATABASE_URL inside one of the service files in /home/leeps
* Run ‘otree resetdb’ to add new database columns
* Run ‘otree collectstatic’ to cache static files
* If the experiment doesn’t show up, run ‘sudo systemctl restart otree.service’  


