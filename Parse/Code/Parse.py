from selenium import webdriver
from seleniumwire import webdriver
import re, os, time, requests


class Parse:

    def __init__(self):
        self.driver = webdriver.Safari(seleniumwire_options={'port': 12345})
        self.Malware_hrefs = []
        self.Normal_hrefs = []
        self.Mixed_hrefs = []
        self.first_line = None
    
    def go_to(self,url):
        self.driver.get(url)
    
    def trouve(self,element):
        output = self.driver.find_element_by_name(element)
        return output
    
    def quit(self):
        self.driver.quit()
        
    def add_line_in_file(self,line,file_):
        clean_line = re.sub(r'([\w)])[\s]+',r'\1,',line) #Enlève le ou les espaces et les remplace par des , 
        with open(file_,'a') as file:
            file.write(clean_line)
            file.write("\n")
        return clean_line
    
    def element_to_url(self,list_element):
        new_list = []
        for i in list_element:
            new_list.append(i.get_attribute("href"))
        return new_list
    
    def getUrls(self,lien):
        #Pour récupérer les href de chaque lien c'est get_attribute("href")
        self.go_to(lien)
        self.Malware_hrefs = self.driver.find_elements_by_partial_link_text('CTU-Malware-Capture-Botnet')
        self.Malware_hrefs = self.element_to_url(self.Malware_hrefs)
        self.Normal_hrefs = self.driver.find_elements_by_partial_link_text('CTU-Normal')
        self.Normal_hrefs = self.element_to_url(self.Normal_hrefs)
        self.Mixed_hrefs = self.driver.find_elements_by_partial_link_text('CTU-Mixed')
        self.Mixed_hrefs = self.element_to_url(self.Mixed_hrefs)
        
        
    def read_first_line(self,lien):
        r = requests.get(lien, stream=True,verify=False)
        for line in r.iter_lines():
            if line:
                return line.decode("utf-8")
    
    def read_url(self,url_list,type_of_file,file_name):
        for url in url_list:
            self.go_to(url)
            print('Pour ',str(url))
            try:
                l = self.driver.find_elements_by_partial_link_text(type_of_file)
                for i in l:
                    line = str(self.read_first_line(i.get_attribute("href"))) +','+str(i.get_attribute("href"))
                    clean_line = self.add_line_in_file(line,file_name)
                    print(clean_line)
            except:
                print('On a eu un problème ici --> ',type_of_file )
            print('------------------------------------------------------------------')
    
    def end_of_list(self):
        print("-------------------------------------END-------------------------------------")