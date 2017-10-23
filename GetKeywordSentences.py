from FunctionsAndLists import *
from pprint import pprint

dict_of_MCP = {}


for i in MP_Constituency_Party:
    li = searchForKeywordSentencesInDS(i[0])
    if li:
        dict_of_MCP[i] = li
pprint(dict_of_MCP)
