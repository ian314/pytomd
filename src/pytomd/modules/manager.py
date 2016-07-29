'''
Created on Jul 28, 2016

@author: iitow
'''
import os
import sys
from scanner import Scanner
from transform import divider,header,bold,inline,bold_regex

class Manager(object):
    ''' This class manages all files and scanners
    '''
    def __init__(self,path,output):
        ''' Manager Constructor
        :param path: String
        :param output: String
        '''
        self.fileObjs = []
        self.path = path
        self.output = output
        self.files = self._files(self.path)
        self.preface = self.preface_reader()
        self.writer(self.preface)
        self._files(self.path)
        self.run()
    
    def preface_reader(self):
        ''' Adds preface to output file
        '''
        output = self.output.rsplit('/',1)[0]
        file = "%s/PREFACE.md" % (output)
        if os.path.exists(file):
            with open(file, 'r') as preface:
                output = preface.readlines()
                return output
        print "[error] Preface not found @ %s" % (file)
        print "please create one"
        sys.exit(1)
        return None
    
    def writer(self,lines,type='w'):
        ''' Performs all writes
        :param lines: List
        :param type: String, w,a
        '''
        if lines:
            with open(self.output, type) as readme:
                readme.writelines(lines)

    def _files(self,path):
        ''' performs scan on all files
        :param path: String
        '''
        for root, directories, filenames in os.walk(path):
            for filename in filenames:
                if '.' in filename:
                    if filename.split('.')[1] == 'py':
                        filepath =  "%s/%s" % (root, filename)
                        scn = Scanner(path,filepath,self.output)
                        fileObj = scn._scan()
                        self.fileObjs.append(fileObj)
    def run(self):
        output = []
        for fileObj in self.fileObjs:
            output.append("\n%s" % (divider()))
            output.append("\n%s" % (divider()))
            output.append("\n File @ %s\n" % (bold(fileObj.name)))
            for dataObj in fileObj.data:
                type = dataObj.type
                name = dataObj.name
                tags = dataObj.tags
                fields = dataObj.fields
                example = dataObj.example
                name_str = "%s %s" % (dataObj.type,dataObj.name)
                output.append("\n\n%s: " % (bold(name_str),))
                output.append("\n\n%s" % (bold_regex(dataObj.doc)))
            self.writer(output,type='a')









