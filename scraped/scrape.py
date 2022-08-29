def main_navigator(url, pages, index):
    '''creates a new url , repacing original with 0 and calls the get links
    function
    '''
    new_url = url[:index] + str(0) + url[index + 1:]
    for i in range (1,pages+1):
        print(i)
        get_links(new_url, i, index)

def get_num_lines(file_name):
    
    with open(file_name, "r") as f2:
        number_lines = len(f2.readlines())
        print('Total lines:', number_lines)
        return (number_lines)

def clean_text(upper_limit):

    to_delete = (r'https://www.rawpixel.com/free-images')

    with open("scrape_links.txt", "r+") as f1:
        lines = f1.readlines()
        for i in range(0, upper_limit):#upper limit is the number of lines in the original text file
            if lines[i].find(to_delete):
                with open("scrape_links_modified.txt", "a") as fwrite:
                    fwrite.write(f'{lines[i]}')
        f1.truncate(0)

    print("Text is cleaned. Transferring the text to the excel file.")


def get_links(user_url, number, index):
    import requests
    from bs4 import BeautifulSoup
    '''Changes pages by changing number in ?page= in the link and gets the links
    '''
    original_url = user_url
    char = original_url.find("page=")#get position of the number in the url
    index = char+5
    modified_url = original_url[:index] + str(number) + original_url[index + 1:]
    print("I got here:")
    print(modified_url)
    #getting html
    r = requests.get(modified_url)
    html_content = r.text
    #parse the html
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # find a tag
    anchors = soup.find_all('a')

    all_links = set()


    for link in anchors:
        string = (str(link))
        unwanted = 'creativecommons'
        if string.__contains__('image') and unwanted not in string:
            linkText = "https://www.rawpixel.com"+link.get('href')
            all_links.add(linkText)
    #find  links

    for imgtag in all_links:
        with open("scrape_links.txt", "a") as f:
            f.write(f'{imgtag}\n')
    
    print("done scraping links")
