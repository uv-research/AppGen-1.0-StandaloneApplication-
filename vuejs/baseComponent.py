from vuejs.componentOperations import *

def writePart1():
    a = open("./finalApp/src/components/HelloWorld.vue","a")
    a.write(part1)
    a.close()

def writePart2():
    a = open("./finalApp/src/components/HelloWorld.vue","a")
    a.write(part2)
    a.close()

def writePart3():
    a = open("./finalApp/src/components/HelloWorld.vue","a")
    a.write(part3)
    a.close()

def writePart4():
    a = open("./finalApp/src/components/HelloWorld.vue","a")
    a.write(part4)
    a.close()

def writeInputs(id):
    with open("./finalApp/src/components/HelloWorld.vue", 'a') as file:
        file.write("""
    <input  v-model.number='number"""+str(id)+"""' type="number" placeholder='number"""+str(id)+"""'><br/>""")
        file.close()

def writeInData(id):
    with open("./finalApp/src/components/HelloWorld.vue", 'a') as file:
        file.write("""
      number"""+str(id)+""": '',""")
        file.close()

def writeAddOperation(count):
    with open("./finalApp/src/components/HelloWorld.vue", 'a') as file:
        file.write("""
      this.result = 0;
      for(var i=0; i< """+str(count)+"""; i++ ) {
        this.result = this.result + this['number' + i];
      } """)
        file.close()

def writeSubOperation(count):
    with open("./finalApp/src/components/HelloWorld.vue", 'a') as file:
        file.write("""
      this.result = 0;
      for(var i=0; i< """+str(count)+"""; i++ ) {
        if(i === 0) {
          this.result = this['number' + i]
        } else {
          this.result = this.result - this['number' + i];
        }
      } """)
        file.close()