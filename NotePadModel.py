import os
class Model:
    def __init__(self):
        self.key='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        self.offset=5

    def encrypt(self,plaintext):
        result=''
        for ch in plaintext:
            try:
                i=(self.key.index(ch)+self.offset)%len(self.key)
                result += self.key[i]
            except ValueError:
                result += ch
        return result
    def decrypt(self,ciphertext):
        result=''
        for ch in ciphertext:
            try:
                i=(self.key.index(ch)-self.offset)%len(self.key)
                result += self.key[i]
            except ValueError:
                result += ch
        return result
    def save_file(self,msg,url):
        if type(url) is not str:
            file=url.name
        else:
            file=url
        filename,file_extension = os.path.splitext(file)
        if file_extension in '.ntxt':
            encrypted=self.encrypt(msg)
            with open(file,'W',encoding='utf-8') as fw:
                fw.write(encrypted)
        else:
            content =msg
            with open(file,'w' ,encoding='utf-8') as fw:
                fw.write(content)
    def save_as(self,url,msg):
        if type(url) is not str:
            file=url.name
        else:
            file=url
        msg = self.encrypt(msg)
        with open(file, 'w') as fw:
            fw.write(msg)
    def read_file(self,url):
        filename,file_extension=os.path.splitext()
        fi = open(url,"r")
        if file_extension in '.ntext':
            msg1 = fi.read()
        fi.close()
        return  msg1, filename+file_extension
    def takeQuery(self):
        sr = s.Recognizer()
        sr.pause_threshold = 1
        print("speak")
        with s.Microphone() as m:
            try:
                audio = sr.listen(m)
                query = sr.recognize_google(audio, language='eng-in')  # google api client library
                return query

            except Exception as e:
                print("exception in this", e)
                print("not recognized")
