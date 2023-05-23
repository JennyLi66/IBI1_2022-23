Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import xml.etree.ElementTree as ET
from openpyxl import Workbook
search_term = 'autophagosome'
tree = ET.parse('/Users/jenny/Desktop/IBI 1/go_obo.xml')
root = tree.getroot()
wb  = Workbook()
ws = wb.active
ws.append(['GO ID', 'Term Name', 'Definition', 'Number of Child Nodes'])
>>> def count_child_nodes(id):
...     term = root.find(f".//term[id='{id}']")
...     child_terms = []
...     for is_a in term.findall("def/defstr/..[@type='is_a']"):
...         child_term_id = is_a.text
...         child_term = root.find(f".//term[id='{child_term_id}']")
...         child_terms.append(child_term)
...     count = len(child_terms)
...     for child_term in child_terms:
...         count += count_child_nods(child_term.find('id').text)
...     return count
... 
>>> for term in root.iter('term'):
...     defstr = term.find('def').find('defstr').text
...     if search_term in defstr:
...         id = term.find('id').text
...         name = term.find('name').text
...         definition = defstr
...         num_child_nodes = count_child_nodes(id)
...         ws.append([id, name, definition, num_child_nodes])
... 
...         
>>> wb.save('/Users/jenny/Desktop/IBI 1/autophagosome.xlsx')
>>> 
>>> 
>>> 
>>> 

>>> 
