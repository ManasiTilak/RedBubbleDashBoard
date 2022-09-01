from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QDialog, QLineEdit, QComboBox
from PyQt5 import uic
import sys
import os
import time
# from scraped import scrape
from scraped import scrape, transfer
#from downloaded import setdriver
from downloaded import setdriver
#import string manipulation to clean the folder names
import string_manipulation
#from cleaned
from cleaned import image_edit
#from database_settings
from database_setting import add_user, get_username, fetchdata_username

class Upload_UI(QMainWindow):
    def __init__(self):
        
        super(Upload_UI, self).__init__()
        #loading the GUI Window
        uic.loadUi("./gui_win/upload.ui", self)
        #finding elements - display
        self.choose_user = self.findChild(QComboBox, "chooseUser")
        self.display_user = self.findChild(QLabel, "displayUser")
        #finding elements - buttons
        self.delete_user = self.findChild(QPushButton, "deleteUser")        
        self.edit_user = self.findChild(QPushButton, "editUser")
        self.main_upload = self.findChild(QPushButton, "mainUpload")
        self.select_user = self.findChild(QPushButton, "selectUser")
        #on click above buttons
        self.delete_user .clicked.connect(self.delete_account)
        self.edit_user .clicked.connect(self.edit_account)
        self.main_upload .clicked.connect(self.upload_main)
        self.select_user .clicked.connect(self.select_account)

        #adding items to combobox
        items = get_username.get_usernames()
        for item in items:
            self.choose_user.addItem(item[0])

    def delete_account(self):
        print("delete")

    def edit_account(self):
        print("edit")

    def upload_main(self):
        print("upload")

    def select_account(self):   
        #get selected username
        selected_username = self.choose_user.currentText()
        user_datas = fetchdata_username.fetch_userdata(selected_username)
        for user_data in user_datas:
                user_string = '\n'.join(user_data)
                print(user_string)
                # print(user_data[i].join)
        self.display_user.setText(user_string)

class NewUserRed_UI(QMainWindow):
    def __init__(self):
        
        super(NewUserRed_UI, self).__init__()
        # initializing variables for img folder and excel
        self.new_imgfolder = ""
        self.new_excel = ""
        #loading the GUI Window
        uic.loadUi("./gui_win/newuser_red.ui", self)
        #finding elements
        self.username_input = self.findChild(QLineEdit, "newUsername")
        self.email_input = self.findChild(QLineEdit, "newEmail")
        self.password_input = self.findChild(QLineEdit, "newPassword")
        self.new_imagefolder = self.findChild(QPushButton, "newImagefolder")
        self.new_excel = self.findChild(QPushButton, "newExcel")
        self.newuser_done = self.findChild(QPushButton, "newuserDone")
        #on click above buttons
        self.new_imagefolder.clicked.connect(self.new_getfolder)
        self.new_excel.clicked.connect(self.new_getexcel)
        self.newuser_done.clicked.connect(self.newuser_logic)

    def new_getfolder(self):
        getfolder = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "PNG Files (*.png);;JPG Files(*.jpg)")
        self.new_imgfolder = string_manipulation.string_manipulate(str(getfolder[0]))
    
    def new_getexcel(self):
        getexcel = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "Excel Files (*.xlsx)")
        self.new_excel = str(getexcel[0])
    
    def newuser_logic(self):
        # getting label data
        new_username = str(self.username_input.text())
        new_email = str(self.email_input.text())
        new_password = str(self.password_input.text())
        new_folder = str(self.new_imgfolder)
        new_excel = str(self.new_excel)

        if len(new_username) > 0 and len(new_email) > 0 and len(new_password) > 0:
            add_user.add_new(new_username, new_email, new_password, new_folder, new_excel)
            self.hide()
            # print((new_username, new_email, new_password, new_folder, new_excel))
        else:
            print("Username, Password and Emails are mandatory fields.")



class Clean_UI(QMainWindow):
    def __init__(self):
        
        super(Clean_UI, self).__init__()
        self.new_original_name = ""
        #loading the GUI Window
        uic.loadUi("./gui_win/clean.ui", self)
        #finding elements
        self.original_folder = self.findChild(QPushButton, "cleanOriginal")
        self.clean_done_button = self.findChild(QPushButton, "cleanDone")
        #on click above buttons
        self.original_folder.clicked.connect(self.clean_getoriginalfolder)
        self.clean_done_button.clicked.connect(self.clean_logic)
    
    def clean_getoriginalfolder(self):

        chosen_original_folder = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "PNG Files (*.png);;JPG Files(*.jpg)")
        self.new_origin_name = string_manipulation.string_manipulate(str(chosen_original_folder[0]))
        if len(self.new_origin_name) == 0:
            print("Please choose a folder")
    
    def clean_logic(self):
        print("Clean Button was Clicked.")
        to_clean_folder = self.new_origin_name
        if len(to_clean_folder) != 0:
            image_edit.navigate_images(to_clean_folder)

class Download_UI(QMainWindow):
    def __init__(self):
        super(Download_UI, self).__init__()
        #loading the GUI Window
        uic.loadUi("./gui_win/download.ui", self)
        #finding elements
        self.num_imagesdownload_input = self.findChild(QLineEdit, "downloadNumber")
        self.download_done_button = self.findChild(QPushButton, "downloadDone")
        #on click download done
        self.download_done_button.clicked.connect(self.download_logic)
    
    def download_logic(self):
        #getting user input
        num_images = 0
        try:
            num_images = int(self.num_imagesdownload_input.text())
            if num_images > 0:
                print(f"number of images to download are {num_images}")
                setdriver.start_driver(num_images)
            else:
                print("Number of images must be greater than 0")
        except ValueError:
            print("Please enter a number in the pages field")
        
class Scrape_UI(QMainWindow):
    def __init__(self):
        super(Scrape_UI, self).__init__()
        #loading the GUI Window
        uic.loadUi("./gui_win/scrape.ui", self)
        #finding elements
        self.scrape_done_button = self.findChild(QPushButton, "rawscraperDone")
        self.url_input = self.findChild(QLineEdit, "urlInput")
        self.page_input = self.findChild(QLineEdit, "pageInput")
        #on click scrape done
        self.scrape_done_button.clicked.connect(self.scrape_logic)
    
    def scrape_logic(self):
        #getting user input
        raw_url = self.url_input.text()

        #get position of the number in the url
        char = raw_url.find("page=")
        index = char+5

        total_page = 0
        #total page input is taken as int and checking that number of pages is an integer
        try:
            total_page = int(self.page_input.text())
            '''checking if 'page=' exists in the raw_url.
             if there it doesnt, index returns -1.
             if it does, we make sure that no text was entered in number of pages.
             then we clean change page=1 to page=0 so we can start looping get links
             then we call get links.
             '''
            if char == -1:
                print("Please Check your URL")
                
            else:
                if total_page> 0:
                    new_url = raw_url[:index] + str(0) + raw_url[index + 1:]
                    for i in range (1,total_page + 1):
                        scrape.get_links(new_url, i, index) #this would save links in file 'scrape.txt'
                    no_lines = scrape.get_num_lines('scrape_links.txt')
                    '''
                    this cleans the text and removes bad links. 
                    it then transfers the links in scrape_links_modified.txt
                    '''
                    scrape.clean_text(no_lines)
                    modified_lines = scrape.get_num_lines('scrape_links_modified.txt')
                    transfer.transfer_links(modified_lines)
                    time.sleep(15)
                    self.hide()
                else:
                    print("Number of images must be greater than 0")
        except ValueError:
            print("Please enter a number in the pages field")
     
class Main_UI(QMainWindow):
    def __init__(self):
        super(Main_UI, self).__init__()
        #loading the GUI Window
        uic.loadUi("./gui_win/RedbubbleDash.ui", self)
        #finding the buttons
        self.scrape_button = self.findChild(QPushButton, "scrapeButton")
        self.download_button = self.findChild(QPushButton, "downloadButton")
        self.clean_button = self.findChild(QPushButton, "cleanButton")
        self.upload_button = self.findChild(QPushButton, "uploadButton")
        self.red_button = self.findChild(QPushButton, "redButton")
        self.raw_button = self.findChild(QPushButton, "rawButton")

        #defining onclick events
        self.scrape_button.clicked.connect(self.to_scrape)
        self.download_button.clicked.connect(self.to_download)
        self.clean_button.clicked.connect(self.to_clean)
        self.upload_button.clicked.connect(self.upload)
        self.red_button.clicked.connect(self.red)
        self.raw_button.clicked.connect(self.raw)
    
    def to_scrape(self):
        self.scrapewin = Scrape_UI()
        self.scrapewin.show()
    
    def to_download(self):
        self.scrapewin = Download_UI()
        self.scrapewin.show()

    def to_clean(self):
        self.scrapewin = Clean_UI()
        self.scrapewin.show()

    def upload(self):
        self.scrapewin = Upload_UI()
        self.scrapewin.show()

    def red(self):
        self.scrapewin = NewUserRed_UI()
        self.scrapewin.show()
        

    def raw(self):
        print("raw")

    def scrape():
        print("scrape")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main_UI()
    main.show()
    sys.exit(app.exec_())
