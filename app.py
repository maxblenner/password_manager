import database_manager as dbm
import login as lg


def store_pw(u_mail,app_email,apw,app_name,app_url):
    dbm.storePass(app_email,apw,app_name,app_url)



#u_mail = lg.email
app_name = input('Please provide the name of the website')
app_email = input('Please provide the email for this website')
apw = input('Please provide the password for the website')
app_url = input('Please provide link to the website')

store_pw(u_mail,app_email,apw,app_name,app_url)

