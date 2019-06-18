from angular.app.componentOperations import *

def writeComponentPart1():
    a = open("./finalApp/src/app/app.component.ts","a")
    a.write(part3)
    a.close()

def writeAddOperation(count):
    with open("./finalApp/src/app/app.component.ts", 'a') as file:
        file.write("""
      this.result = 0;
      this.formdata = formData;
      for(var i=0; i< """+str(count)+"""; i++ ) {
        this.result = this.result + this.formdata['number' + i];
      }
    }
  }""")
        file.close()

def writeSubOperation(count):
    with open("./finalApp/src/app/app.component.ts", 'a') as file:
        file.write("""
      this.result = 0;
      this.formdata = formData;
      for(var i=0; i< """+str(count)+"""; i++ ) {
        if(i === 0) {
          this.result = this.formdata['number' + i];
        } else {
          this.result = this.result - this.formdata['number' + i];
        }
      }
    }
  }""")
        file.close()   