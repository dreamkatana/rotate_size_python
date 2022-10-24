from PIL import Image
import os, sys

#Carrega imagens jpg do diretorio e as rotaciona
#João Eduardo https://github.com/dreamkatana/
#size está com o valor padrão 400x400
def resize_rename_rotate(srcfile, targetdir="", size=(400,400)):
        targetfile = os.path.splitext(srcfile)[0]
        extension = os.path.splitext(srcfile)[1]
 
        with Image.open(srcdir + srcfile) as im:
          #rotaciona a imagem em 90 graus ate completar 360 graus
          for i in range(0, 360, 90):
            im.rotate(i).resize(size).save(targetdir + targetfile + str(i) + extension)
            #im.rotate(40).resize(size).save(targetdir+targetfile+extension,"jpeg")
        #im.close()
        #im = Image.open(srcfile)  # open file
        #im.rotate(270) # degrees counter-clockwise
        #im.rotate(45).show()
        #im.resize((128, 128)) # resize the file
        #im = im.save(targetdir+targetfile+extension,"jpeg")


if __name__=="__main__":
        #diretorio de destiona das imagens transformadas      
        targetdir = "/home/joaoeps/Dropbox/cursos/ml/20_and_50_filtered/validation/50/output/"
        #diretorio onde estão as imagens
        srcdir = "/home/joaoeps/Dropbox/cursos/ml/20_and_50_filtered/validation/50/"

for file in os.listdir(srcdir):  
  if file[-3:] == "jpg":
    print(file)
    resize_rename_rotate(file, targetdir)
    