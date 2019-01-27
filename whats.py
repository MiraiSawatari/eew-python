import tests as notify
from numpy.random import *
import sys
import re
text="".join(sys.argv).replace("whats.py","").replace(":pp:","\n").replace("#緊急地震速報#地震","").replace("-","").replace(sys.argv[-1],"")
text=re.sub('あと[0-9][0-9]秒',"",text)
text=re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
text = '\n'.join(text.splitlines()[2:])
notify.balloon_tip("緊急地震速報 #"+str(randint(1500000)),text)
