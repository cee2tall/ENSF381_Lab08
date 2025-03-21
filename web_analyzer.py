import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")


content = soup.get_text()
replacing = [".", ",", "\"", "(", ")", ";", "-", "\n", "\t", ":", "'"]
for x in replacing:
    content = content.replace(x, " ")


# Exercise 4
my_list = content.split(" ")
strings = [x.lower() for x in my_list if x]
count = 0
user_word = input("Enter: ")
for word in my_list:
    if word.lower() == user_word.lower(): 
        count += 1
print(f"{user_word} appears {count} times")


# Exercise 5
words = []
count = []
print("\nPrinting top 5 most frequently occuring words")
for word in strings:
    if word not in words:
        words.append(word)
        count.append(strings.count(word))
for i in range(5):
    large_word = words[count.index(max(count))]
    print(f"{large_word} occurs {max(count)} times.")
    count[count.index(max(count))] = 0


# Exercise 6
paragraphs = soup.find_all("p")
max_length = 0
max_index = 0
for i in range(len(paragraphs)):
    if(len(paragraphs[i].get_text()) > max_length):
        max_index = i
        max_length = len(paragraphs[i].get_text())

print(f"\nThe longest paragraph has {len(paragraphs[max_index].get_text().split())} words, and reads as follows:\n\n {paragraphs[max_index].get_text()}")


# Exercise 7
heading_counts = []
for i in range(1,7):
    heading_counts.append(len(soup.find_all(f'h{i}')))
headings = sum(heading_counts)
links = len(soup.find_all('a'))
paragraphs = len(soup.find_all('p'))
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group 26')
plt.ylabel('Count')
plt.show()