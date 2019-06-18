from angular.app.componentOperations import *

def writeHtmlPart1():
    a = open("./finalApp/src/app/app.component.html","a")
    a.write(part1)
    a.close()

def writeHtmlPart2():
    a = open("./finalApp/src/app/app.component.html","a")
    a.write(part2)
    a.close()  

def writeInputs(id):
    with open("./finalApp/src/app/app.component.html", 'a') as file:
        file.write("""
    <input type="number" placeholder='number"""+str(id)+"""' name='number"""+str(id)+"""' [ngModel]='number"""+str(id)+"""' /><br/>""")
        file.close()

        