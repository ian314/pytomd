'''
Created on May 2, 2016

:author: iitow
'''
import ast
import os
import re
import sys

        
class Scanner(object):
    ''' scans all python files for attributes
    '''
    def __init__(self,base_path,file,output):
        ''' Scanner Constructor
        :param base_path: String, base of git repo
        :param file: String, to be parsed
        :param output: String, place to put README.md
        '''
        self.base_path = base_path
        self.file = file
        self.output = output
        self.handle = self.get_ast()
        self.examples = []

    def get_ast(self):
        ''' Get ast obj tree
        '''
        with open(self.file, 'r') as f:
            data  = f.read()
        return ast.parse(data)
    
    def _scan(self):
        ''' Performs the scan & adds markdown
        '''
        lines = []
        lines.append("\n**********************************************")
        lines.append("\n**********************************************")
        file = "\nfile @ **%s**\n" % self.file.split(self.base_path,1)[1]
        lines.append(file)
        text = ast.get_docstring(self.handle)
        doc = "\n      %s\n" % (text)
        doc = self.bold(doc)
        lines.append(doc)
        for node in ast.walk(self.handle):
            if isinstance(node,ast.ClassDef):
                cls = '\n####class %s####\n' % (node.name)
                text = ast.get_docstring(node)
                doc = "\n      %s \n" % (text)
                doc = self.bold(doc)
                lines.append(cls)
                lines.append(doc)
            if isinstance(node,ast.FunctionDef):
                func = "\n ***def %s*** \n" % (node.name)
                text = ast.get_docstring(node)
                doc = "\n      %s \n" % (text)
                doc = self.bold(doc)
                lines.append(func)
                lines.append(doc)
        return lines
    
    def bold(self, line,regex=r'(?<=:)[^:\n]*'):
        ''' Bolds params and attribs
        :param line: String
        :param: regex: raw String
        '''
        if isinstance(line,str):
            matches = re.findall(regex, line)
            for match in matches:
                old = ':%s:' % match
                new = '\n**%s:**' % (match)
                if new:
                    line = line.replace(old, new)
        return line


class Manager(object):
    ''' This class manages all files and scanners
    '''
    def __init__(self,path,output):
        ''' Manager Constructor
        :param path: String
        :param output: String
        '''
        self.path = path
        self.output = output
        self.files = self._files(self.path)
        self.preface = self.preface_reader()
        self.writer(self.preface)
        self._files(self.path)
    
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
                        file_attrs = scn._scan()
                        self.writer(file_attrs,type='a')
        