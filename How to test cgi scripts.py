'''Import regular stuff'''
import cgi, os, sys

#change the path to include my app
sys.path.insert(1,'webapp\\')

#Import functions
import login

#Set the REQUEST_METHOD environ Var to "GET"
os.environ["REQUEST_METHOD"] = "GET"

#Then set QUERY_STRING = to the data you want to be put into the feield storage
#Using the syntax that URL's use after the '?'

#EX. In http://applequest.fallenofftheedge.com/cgi.py?key=data
#   Just this part with out the bracets              [key=data]
os.environ["QUERY_STRING"] = "key=send_login&username=joshgud777&password=SWgrad15"

def main():
    '''Call the function you with to test that needs there vars set'''
    login.main()
    
if __name__ == '__main__':
    '''This should output headders with cookies set to set the id and informat-
    ion needed to have sessisions and also print a redirect page to game.py''' 
    main()
