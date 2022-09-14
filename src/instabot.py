# -*-coding:utf-8 -*

import os
from os import path
import sys
import random
from datetime import datetime
from time import sleep
import inspect
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import utils.file_utils as file_utils
import utils.mylog as mylog
import utils.jsonprms as jsonprms
from utils.humanize import Humanize
from utils.mydecorators import _error_decorator, _trace_decorator

class Bot:
      
        #def __init__(self):                
                

        def trace(self,stck):                
                self.log.lg(f"{stck.function} ({ stck.filename}-{stck.lineno})")


        # 
        @_trace_decorator
        @_error_decorator()
        def search(self):
                # //*[@id="mount_0_0_Js"]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input
                # //*[@id="mount_0_0_5O"]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input
                pass

        # init
        @_trace_decorator
        @_error_decorator()
        def init_webdriver(self):
                options = webdriver.ChromeOptions()
                if (self.jsprms.prms['headless']):
                        options.add_argument("--headless")
                else:
                        options.add_argument("user-data-dir=./chromeprofile")
                # anti bot detection
                options.add_argument('--disable-blink-features=AutomationControlled')
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_experimental_option('useAutomationExtension', False)
                # pi / docker
                if (self.jsprms.prms['box']):
                        options.add_argument("--no-sandbox")
                        options.add_argument("--disable-dev-shm-usage")
                        options.add_argument("--disable-gpu")
                        prefs = {"profile.managed_default_content_settings.images": 2}
                        options.add_experimental_option("prefs", prefs)
                options.add_argument(f"user-agent={self.jsprms.prms['user_agent']}")
                options.add_argument("--start-maximized")
                driver = webdriver.Chrome(executable_path=self.chromedriver_bin_path, options=options)
                # anti bot detection
                # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
                driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                # resout le unreachable
                driver.set_window_size(1900, 1080)
                driver.implicitly_wait(self.jsprms.prms['implicitly_wait'])
                return driver
        
        def init_main(self, command, jsonfile):
                try:
                        self.root_app = os.getcwd()
                        self.log = mylog.Log()
                        self.log.init(jsonfile)
                        self.trace(inspect.stack()[0])
                        jsonFn = f"{self.root_app}{os.path.sep}data{os.path.sep}conf{os.path.sep}{jsonfile}.json"                        
                        self.jsprms = jsonprms.Prms(jsonFn)
                        self.chromedriver_bin_path = self.jsprms.prms['chromedriver']
                        self.test = self.jsprms.prms['test']
                        self.login = self.jsprms.prms['login']
                        self.password = self.jsprms.prms['password']
                        self.log.lg("=HERE WE GO=")                        
                        keep_log_time = self.jsprms.prms['keep_log_time']
                        keep_log_unit = self.jsprms.prms['keep_log_unit']
                        self.log.lg(f"=>clean logs older than {keep_log_time} {keep_log_unit}")   
                        file_utils.remove_old_files(f"{self.root_app}{os.path.sep}log", keep_log_time, keep_log_unit)
                        # self.dbcontext = self.get_db_context(self.jsprms.prms['dbpath'])
                        # self.log.lg(f"Visited so far {self.dbcontext.visited_count()}")
                except Exception as e:
                        self.log.errlg(f"Wasted ! : {e}")
                        raise

        def newtab(self,url):            
                self.driver.execute_script("window.open('{0}');".format(url))
                self.driver.switch_to.window(self.driver.window_handles[-1]) 
                

     

        def main(self, command="", jsonfile="", param1="", param2=""):                          
                try:
                        # InitBot
                        if command == "":
                                nb_args = len(sys.argv)
                                command = "test" if (nb_args == 1) else sys.argv[1]
                                # fichier json en param
                                jsonfile = "default" if (nb_args < 3) else sys.argv[2].lower()                                
                                param1 = "default" if (nb_args < 4) else sys.argv[3].lower()
                                param2 = "default" if (nb_args < 5) else sys.argv[4].lower()
                                param3 = "default" if (nb_args < 6) else sys.argv[5].lower()      
                                print("params=", command, jsonfile, param1, param2)
                        # logs
                        print(command)     

                        # debug
                        command = "login"

                                                 
                        self.init_main(command, jsonfile)
                        self.trace(inspect.stack()[0])    
                        self.driver = self.init_webdriver() 
                        #print(self.driver.execute_script("return navigator.userAgent;"))
                        #input("attention lancement du merdier : ")
                        
                        if (command == "login"):
                                self.driver.get("https://instagram.com")                                               
            
                        input("Wait for key: ")
                        self.driver.close()
                        ##)  

                        #ONGLETS
                        #driver.switch_to.window(driver.window_handles[-1])       

                except KeyboardInterrupt:
                        print("==Interrupted==")
                        pass
                except Exception as e:
                        print("GLOBAL MAIN EXCEPTION")
                        self.log.errlg(e)
                        # raise
                        #
                finally:
                        print("do disconnect")                        
            




              
               
    

        
                

        

