import base64
import sys

the_pdf = open('./pdf/ainterview-pdf.pdf',"rb").read()
encodeStr = base64.b64encode(the_pdf)
base64_text = open('./pdf/ainterview-pdf.txt',"w+")
base64_text.write(str(encodeStr,"utf-8"))
base64_text.close()
print("success")