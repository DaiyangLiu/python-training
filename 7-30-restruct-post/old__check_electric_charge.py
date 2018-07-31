import requests
from bs4 import BeautifulSoup

textmod={'__VIEWSTATE':
'/wEPDwULLTE4NDE5OTM2MDEPZBYCAgMPZBYIAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUM5qW85qCL5Yy65Z+fHg5EYXRhVmFsdWVGaWVsZAUM5qW85qCL5Yy65Z+fHgtfIURhdGFCb3VuZGdkEBUGBuS4nOWMugnnlZnlrabnlJ8G6KW/5Yy6BumfteiLkQbntKvoj5gLLeivt+mAieaLqS0VBgbkuJzljLoJ55WZ5a2m55SfBuilv+WMugbpn7Xoi5EG57Sr6I+YAi0xFCsDBmdnZ2dnZxYBZmQCBQ8QDxYGHwAFBualvOWPtx8BBQbmpbzlj7cfAmdkEBUUB+S4nDHoiI0H5LicMuiIjQfkuJwz6IiNB+S4nDToiI0H5LicNeiIjQfkuJw26IiNB+S4nDfoiI0H5LicOOiIjQzpmYTkuK3kuLvmpbwH5pWZN+iIjQfmlZk46IiNB+WNlzHoiI0H5Y2XMuiIjQfljZcz6IiNC+aygeiLkTEw6IiNC+aygeiLkTEx6IiNC+aygeiLkTEy6IiNC+aygeiLkTEz6IiNCuaygeiLkTnoiI0LLeivt+mAieaLqS0VFAfkuJwx6IiNB+S4nDLoiI0H5LicM+iIjQfkuJw06IiNB+S4nDXoiI0H5LicNuiIjQfkuJw36IiNB+S4nDjoiI0M6ZmE5Lit5Li75qW8B+aVmTfoiI0H5pWZOOiIjQfljZcx6IiNB+WNlzLoiI0H5Y2XM+iIjQvmsoHoi5ExMOiIjQvmsoHoi5ExMeiIjQvmsoHoi5ExMuiIjQvmsoHoi5ExM+iIjQrmsoHoi5E56IiNAi0xFCsDFGdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZGQCEw88KwANAGQCFQ88KwANAGQYAwUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFDEltYWdlQnV0dG9uMQUMSW1hZ2VCdXR0b24yBQlHcmlkVmlldzEPZ2QFCUdyaWRWaWV3Mg9nZLHWUKnsT4U5B01iOoW0cLHinyY9',
'__EVENTVALIDATION':
'/wEWIgLS+p/fDgLorceeCQLc1sToBgL+zpWoBQK50MfoBgKj5aPiDQLtuMzrDQLrwqHzBQKX+9a3BALahLK2BQLahLa2BQLahIq2BQLahI62BQLahIK2BQLahIa2BQLahJq2BQLahN61BQL4w577DwKH0Zq2BQKH0d61BQKVrbK2BQKVrba2BQKVrYq2BQKY14SVBQKY1+jwDAKY1/zbCwKY18CmAwLr76OiDwKUlLDaCAL61dqrBgLSwpnTCALSwtXkAgLs0fbZDALs0Yq1BYiiagV69FGjEwsWCICpCTfoshaE',
'programId':'东区','txtyq':'沁苑9舍','Txtroom':'531','ImageButton1.x':'19','ImageButton1.y':'16'}


r = requests.post('http://202.114.18.218/Main.aspx', data= textmod)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

target_node = soup.find_all('input')[-1]
electric_value = target_node.get('value')
print("剩余电费 ： ",electric_value)

if float(electric_value) < 15 :
    print("大哥该交电费了！")



