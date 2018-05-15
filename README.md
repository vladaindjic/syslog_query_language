# syslog_query_language
Syslog Query Language

Fajlovi od interesa:
  - syslog.pg sadrzi gramatiku jezika
  - ir.py sadrzi medjukod i Parglare akcije. Metode remove_not i inv su zaduzene za primenu De Morganovih zakona, dok su optimize i str_mongo namenjene za optimizaciju mongo upita, odnosno njegovu konverziju u string
  - sysqo_time_util.py sadrzi funkcije koje olaksavaju rad sa datumom
  - sysql.py sadrzi klasu koja predstavlja mini kompajler
  
Krace objasnjenje sa primerima je dostupno u [sledecem PDF-u](https://drive.google.com/file/d/1KcTYrm0SQofon1eHzAUoJD1NVvmBbHQ1/view?usp=sharing).

Mini kompajler je implementiran u programskom jeziku Python3. Koriscene su sledece biblioteke:
  - click           6.7
  - parglare        0.5    
  - pip             10.0.1 
  - python-dateutil 2.7.3  
  - pytz            2018.4 
  - rfc3339         6.0    
  - setuptools      39.1.0 
  - six             1.11.0 
  - tzlocal         1.5.1  
  - wheel           0.31.1 
