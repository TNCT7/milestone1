from bs4 import BeautifulSoup

simple_HTML ='''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_html_data = BeautifulSoup(simple_HTML,'html.parser')

def find_h1():
    h1_data = simple_html_data.find("h1")
    print(h1_data.string)

def find_p():
    p_data = simple_html_data.find_all('p')
    return p_data

def find_p_list_with_no_diff_class():
    p_data = find_p()
    p_data_list = [p.string for p in p_data if 'subtitle' not in p.attrs.get('class',[])]
    print(p_data_list[0])

def find_li():
    p_list = simple_html_data.find_all('li')
    p_list_list = [p.string for p in p_list]
    print(p_list_list)

find_h1()
find_p()
find_p_list_with_no_diff_class()
find_li()