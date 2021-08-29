.. _recruiting:

Subject Recruitment Documentation
==================================

.. note::
    You need a faculty account to do this. Try asking a Professor.

Finding people to email: 
--------------------------
* Check `pisa.ucsc.edu/class_search <https://pisa.ucsc.edu/class_search/>`_
* Select the current quarter, and search for courses with the largest enrollment count.
* Protip: I recommend CSE3, LING80K, CSE12, CSE16, ECON1, ECON2, or any lower division classes (They typically have a high enrollment count).
* In `https://my.ucsc.edu <https://my.ucsc.edu>`_, faculty center, class roster search, find these classes, and copy their email lists. 
* Create a new spreadsheet, and copy-paste all roster results without a header
* Remove emails already in the system. 
* We want to exclude anyone already in the ORSEE system 
* Go to `https://econlab.ucsc.edu/admin <https://econlab.ucsc.edu/admin>`_ >> Participants' Overview >> Edit all participants >> Seach and show (without any conditions)
* Copy-paste everything into a CSV and delete all columns that aren’t emails
* This CSV file contains people that have been emailed before and people that are already in the database. 
* After you have pasted the emails into a CSV, replace the emails in the database column in the CSV above
* Once done, use this file to delete duplicates. This will generate a new CSV of people that haven’t been recruited before. (Make sure to execute the python script in the same directory as the other CSVs and change the file names in the CSV)

Compose a new email and paste it into BCC.

Email Template
--------------
.. code-block::

    Subject:
    Participate in paid economics experiments with LEEPS lab at UCSC

    Body:
    The LEEPS Lab at UCSC's Economics Department is looking for people to participate in economics experiments in 2021-22. There will also be online and in-person sessions in Spring-Summer 2021 with a guaranteed minimum of $5.

    Each session lasts 1 – 2 Hours.

    You'll earn at least $7, usually $15 - $25, depending on your luck and skill. 

    You're paid through Venmo at the end of the session.

    Experiments are held online.
    Help us study economics!



    We're seeking several hundred people to take part in many sessions this year. So there will be ample opportunity for you to participate!



    Interested? Register online at https://econlab.ucsc.edu/public/  >> click register 

    After you register, LEEPS Lab will email you invitations as sessions are scheduled. If the date and times work for you, simply sign-up. If not, just wait for the next invitation. You can unsubscribe at any time. 



    Questions comments and concerns, please email leeps@ucsc.edu









