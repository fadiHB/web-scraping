import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
def get_citations_needed_count(url):
    '''
    get_citations_needed takes in a url for the web that want to scrapered 
    and returns an integer that represent the number of citations_needed
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    result = soup.find_all(title = 'Wikipedia:Citation needed')
    return len(result)

def get_citations_needed_report(url):
    '''
    get_citations_needed_report takes in a url for the web that want to scrapered 
    and returns a string that represent the citations_needed_repor
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    lst = []
    words = "citation needed"
    print('#'*100)
    print('P.S: there are 5 Citation , two of them are together in the sane paragraph , you cans notice that in the first one from the results')
    print('#'*100)
    for i in soup.select('p'):
        p_elements = i.getText()
        # print(p_elements)
        counter = 0
        if words in p_elements:
            counter += 1
            if counter == 2:
                parts= p_elements.split('[citation needed]')
                lst.append(parts[0])
                lst.append(parts[1])
                print(parts[0])
                print('///'*20)
                print(parts[1])
                print('///'*20)
                continue
                
            lst.append(p_elements)
            print(p_elements)
            # print(p_elements[0:p_elements.find('needed]')+len('needed ')])
            print('==='*20)
    return

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))





# Page = soup.find(class_ ="mw-parser-output")
# p_elements = Page.find_all('p')
# result = []
# # print(len(p_elements))
# # print(p_elements[0])
# # print(type(p_elements[0]))

# for i in  p_elements:
#     if i.findChildren('spam'):
#         result.append(i)
# print(len(result))





    # print(i)
    # print()
    # lst.append(i.find_parent('p',text='inner'))

    # lst.append(i.find_parent('p').get_text())
    # lst.append(i.find_parent('p').text)

# print(lst[0])

# print(lst[0])

# final_rsult = []
# for i in lst:
#     final_rsult.append(i)

# print(lst[0])
# for i in lst[0]:
#     print (i)
#     print('============================================')

# print(lst[0][0])

# print(len(lst[0]))