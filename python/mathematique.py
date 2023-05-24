import httplib2
import urllib
import re
import base64
import os
 
http = httplib2.Http()
 
url = "http://www.root-me.org//challenge/programmation/ch1/ch1.php?frame=1"
header = {'Content-type':'application/x-www-form-urlencoded','Cookie':'challenge_frame=1; spip_session=[your_spip_sess]; PHPSESSID=[your_phpsessid]'}
param = ""
 
url_result = "http://www.root-me.org/challenge/programmation/ch1/ep1_v.php?resultat="
 
response, content = http.request(url, 'GET', param, header)
 
exp = re.findall(r'U<sub>n\+1</sub> = \[ [\d.-]* \+ U<sub>n</sub> \] . \[ n \* [\d.-]* \]', content)[0].split(' ')
 
A = int(exp[3])
B = int(exp[11])
sign = exp[7]
 
term = int(re.findall(r'Trouver le terme n&deg;[\d.]*', content)[0].split(' ')[3].split(';')[1])
 
U0 = int(re.findall(r'U<sub>0</sub> = [\d.-]*', content)[0].split(' ')[2])
 
if sign == '-':
    B = B*-1
 
term = term+1
 
somme = (term-1)*(term)/2
 
U = term*A + U0 + somme*B
 
response, content = http.request(url_result+str(U), 'GET', param, header)
 
print content
