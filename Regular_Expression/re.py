import re

text = """8320135247 its.malaythakkar@gmail.com 31/10/2002 malaythakkar.me 157.32.102.241
          <main><h1>(999)-111-6666</h1></main> https://malaythakkar.me 123-45-6789
       """

phone_pattern = r'\(\d{3}\)-\d{3}\-\d{4}|\d{10}'
email_pattern = r'([a-z0-9]+[_.]{0,1}[a-z0-9]*)+@[a-z]+(\.[a-z]{2,3}){1,2}$'
date_pattern = r'\d{2}/\d{2}/\d{4}'
url_pattern = r'https?://\S+|^[a-z0-9._%+-]+\.[a-zA-Z]{2,}'
ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
html_tag_pattern = r'<[^>]+>'
ssn_pattern = r'\d{3}-\d{2}-\d{4}'
credit_card_pattern = r'\b(?:\d[ -]*?){13,16}\b'


matches = re.findall(phone_pattern, text)
matches1 = re.findall(email_pattern, text)
matches2 = re.findall(date_pattern, text)
matches3 = re.findall(url_pattern, text)
matches4 = re.findall(ipv4_pattern, text)
matches5 = re.findall(html_tag_pattern, text)
matches6 = re.findall(ssn_pattern, text)
matches7 = re.findall(credit_card_pattern, text)


print(matches)
print(matches1)
print(matches2)
print(matches3)
print(matches4)
print(matches5)
print(matches6)
print(matches7)

 