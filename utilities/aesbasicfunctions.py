# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 10:13:27 2014

@author: amyskerry
"""
import timeit
import pxssh
import pysftp

def is_string_a_number(string):
    try:
        float(string)
        return True
    except:
        return False
        
def extractdata(datafile):
    with open(datafile, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        colnames=reader.next()
        subjdata=[row for row in reader]
    return colnames, subjdata

def uniquifyordered(list):
    '''take a list and return it's unique elements, maintaining their order'''
    mynewset=sorted(set(mylist), key=mylist.index)
    return list(mynewset)
    
def runsshremotescript(hostname, username, password, remoteshscript):
    ssh = pxssh.pxssh()
    ssh.login (hostname, username, password)
    ###
    ssh.sendline ('pwd') #send command
    ssh.prompt() #I'm not clear on what this does "match the prompt"?
    cwd=ssh.before          # print everything before the prompt
    ##
    ssh.sendline('ls')
    ssh.prompt()
    files=ssh.before
    #print "the following files are in directory " + cwd
    #print files[4:]
    ssh.sendline('bash '+remoteshscript)
    ssh.prompt()
    print "executed " + remoteshscript
    ###
    ssh.logout()

def fetchviasftp(hostname,username,remotedir,remotefile,localdestination):
    srv = pysftp.Connection(host=hostname, username=username)
    ##
    srv.execute('ls')
    srv.chdir(remotedir)
    #srv.getcwd()
    #print srv.listdir()
    # Download the file from the remote server
    srv.get(remotefile)
    print 'fetched ' + remotefile +' to ' + localdestination
    # To upload the file, simple replace get with put. 
    #srv.put(remote_file)
    # Closes the connection
    srv.close()

