# Multiprocessing Spider -  Web Scraping 

from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string



def random_url():
	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
	url = ''.join(['http://',starting,'.com'])
	return url

def handle_local_links(url, link):
	if link.startswith('/'):
		return ''.join([url,link])
	else:
		return link

def get_links(url):
	try:
		response  = requests.get(url)
		soup = bs.BeautifulSoup(response.text, 'lxml')
		body = soup.body
		links = [link.get('href') for link in body.find_all('a')]
		links = [handle_local_links(url, str(link.encode('ascii'))) for link in links]
		#link = [str(link.encode('acii')) for link in links]
		return links

	except TypeError as e:
		print(e)
		print('Got a TypeError')
		return []

	except IndexError as e:
		print(e)
		print('Got a IndexError')
		return []
		
	except AttributeError as e:
		print(e)
		print('Got a AttributeError')
		return []

	except Exception as e:
		print(e)
		print('Got a unknown Exception')
		return []


def main():
	how_many  = 50
	p = Pool(processes= how_many)
	parse_links = [random_url()  for _ in range(how_many)]
	links_data = p.map(get_links,[link for link in parse_links])
	links_data  = [url for url_list in links_data for url in url_list] ## creates new list for list of list items 
	p.close()

	with open('urls.txt', 'w') as file:
		file.write(str(links_data))

if __name__ == '__main__':
	main()



		

		


#random_url()



'''
sample = [[1, 2, 3], [5, 6, 7]]
list_1 = [1, 2, 3]
list_2 = [5, 6, 7]


data = [url for inner_list in sample for url in inner_list]

print(data)
print(list_1+list_2)
'''

