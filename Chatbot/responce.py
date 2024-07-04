import random

R_avcourse= "college provide different types of courses like \n 1)computer engineering \n 2)civil engineering \n 3)mechanical engineering \n 4)electrical engineering \n 5)chemical engineering "

R_infocom="for more info refer this site == https://en.wikipedia.org/wiki/Computer_engineering"

R_infocivil="for more info refer this site == https://en.wikipedia.org/wiki/Civil_engineering"

R_infomech="for more info refer this site == https://en.wikipedia.org/wiki/Mechanical_engineering"

R_infoele="for more info refer this site == https://en.wikipedia.org/wiki/Electrical_engineering"

R_infochem="for more info refer this site == https://en.wikipedia.org/wiki/Chemical_engineering"

R_duration="each course have duration of 4 years .\n In which each year consist of 2 semister"

R_spec="Our college is Autonomous institute .\n we give 100 % guarantee of placement.\n Our college get A grade from NAAC Comitee "

R_compa="Many companies are come to our college like Microsoft , Apple , Google, Infosys etc. "

R_fees="all courses have same fees approximate 1.5 lack per year"

R_hostel="yse hostel is available in our college but it charges are not in college fees"

R_sports="Yes sports are available in our college like cricket,TT,basketball,etc. "

R_addmi="This is our official website from where u can apply for admission .\n simply fill all details in form \n This is web site=https://www.sanjivanicoe.org.in/ "

R_name="Name of ur college is Sanjivani College of engineering,Kopargaon"

R_lab="Yes in our college labs and library also available and they are open from 7Am to 7Pm"

def unknown():

response = ["Could you please re-phrase that? ",

"...",

"I dont understand your question",

"What does that mean?"][

random.randrange(4)]

return response