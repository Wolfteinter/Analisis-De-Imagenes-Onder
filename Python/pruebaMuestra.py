initX = -1
initY = -1
posX=0
posY=0
tam=3
for i in range(pow(tam,2)):
    #matrix[posX%tam][posY] = pixels[initX+posX%i,initY+posY]
    print(initX+posX%tam,initY+posY%tam)
    posX+=1
    if(i%3==2):
        posY+=1
