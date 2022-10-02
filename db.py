from point import Point
#taille souhaitee de l'ecran
width, height   = 960, 540
#padding
offset          = 100

#recup les points d'un excel
points = [[10,20],
          [20,5],
          [5,15],
          [0,30],
          [40,20],
          [30,30],
          [20,20],
          [35,0],
          [30,10],
          [100,20]]

#Trouver les coordonnées max pour la redimension des points
maxHInPoints = 0
maxWInPoints = 0

for i in range(len(points)):
    if points[i][0] > maxWInPoints :
        maxWInPoints = points[i][0]
    if points[i][1] > maxHInPoints :
        maxHInPoints = points[i][1]
    
#sens de la division pour la redimension
if maxHInPoints/maxWInPoints > (height-(2*offset))/(width-(2*offset)) :
    divBy = "height"
else:
    divBy = "width"

#proportionner les points pour que ca rentre dans le cadre de l'UI    
data = []
for i in range(len(points)):
    if divBy == "height":
        data.append(Point(((points[i][0])*(height-(2*offset))/maxHInPoints + offset), (points[i][1])*(height-(2*offset))/maxHInPoints + offset))

    else:
        data.append(Point(((points[i][0])*(width-(2*offset))/maxWInPoints + offset), (points[i][1])*(width-(2*offset))/maxWInPoints + offset))
