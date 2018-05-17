# Run this script with `python ghnames.py` until it is correct then
# run `python ghnames.py >> _config.yml` to add it its output to the
# end of our _config.yml.  All students will be added as site authors.

# In Python """ starts a string that can span multiple lines
# Add student github names here.
names = """jbfelder
zman7895
chall12
samsr31
kmorbitzer
grassycheetah94
chausuble
jpanken
lisetted
anusha-suresh
nvola
abaker8
businessowl
jmo560
neatoskeeto
alexreher
WildGinger23
Ibbi2010
brianpugsley
nurahill"""


# The data format our blog uses is called YAML.  It's a common way of
# getting simple data into a program that processes text.
for name in sorted(names.split("\n"), key=str.lower): # the .split() method makes a list out of a string, split at a character. The sorted() function alphabetizes them. 
    print """  {0}:                    
    name: {0}
    prof: false
    gravatar:
    website: 
    github: {0}
    twitter: 
    about: "Here's a little about {0}"
    """.format(name)   # The format method inserts the nth argument at {n} (starting with the zeroth)