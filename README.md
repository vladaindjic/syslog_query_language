# Syslog Query Language 
Syslog Query Language is DSL used for query logs stored in MongoDB. It is compiled to MongoDB's query language by mini compiler implemented using Python Parglare library. This project is part of one implementation of [Security Information and Event Management (SIEM)](https://github.com/vladaindjic/siem).

Files of interests:
  - syslog.pg contains grammar of DSL
  - ir.py contains IR (itermediate representation) and Parglare actions. Methods *remove_not* and *inv* are responsible for applying De Morgan's laws, while *optimize* and *str_mongo* are responsible for generating and optimizing MongoDB's queries.
  - sysqo_time_util.py contains date and time utility functions
  - sysql.py contains class which represents mini compiler
  
Short explanations with examples can be found in [following PDF](https://drive.google.com/file/d/1KcTYrm0SQofon1eHzAUoJD1NVvmBbHQ1/view?usp=sharing). 
Note that PDF is written in Serbian. Google Translate can be used to translate the document easily.

Syslog Query Language's Compiler is implemented in Python3 programming language. This project also uses following libraries:
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
