TLDR0: Use common seance. (If you actually had any to begin with.)
TLDR1: This folder is not the working Database of the ChessApp server.
TLDR2: Don't delete shit that is not yours. Do delete your archaic data.
TLDR3: Don't add massive amounts of data to the database file.

This sqlite3 database contains some users and passwords along with some fake
e-mails to allow the testing of the python files running on the server without
needing to make a database every time to test the scripts. This should not be
used to store actual user data you want on the server. (for legitimate or 
malicious intentions) Because of this the database located in the
"db" folder is not the same folder name as the
folder that the working database file is stored. You may add users to this
file as you see fit. You may also delete your or irrelevant data as you wish,
but please respect the project and allow other user-data that COULD be another
users to remain when committing your awesome modification.

Thanks,
@joshuagud777