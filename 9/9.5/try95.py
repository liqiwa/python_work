
from collections import OrderedDict
#9-13
words = {'liebiao':'liebiao,yuansu jihe','yuanzu':'bukebian xulie','zidian':'jianzhidui'}
for k,v in words.items():
	print(k+"\n"+v)


new_words = OrderedDict()
new_words['yuanzu'] = 'bukebian,xulie'
new_words['liebiao'] = 'liebiao,yuansu,jihe'
new_words['zidian'] ='jianzhidui'
for name,value in new_words.items():
	print(name.title() + "  " + value.title())

