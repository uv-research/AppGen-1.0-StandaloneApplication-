# input1 = """
#                 var x = document.createElement("INPUT");
#                 x.setAttribute("type", "number");
#                 x.setAttribute("value", "");
#                 x.setAttribute("id", """

# input2 = """)
#                 document.body.appendChild(x);
#     """

init1 = """init = function() {"""

init2 ="""
}
"""
initCall = """init();"""

# def writeInit():
#     b = open("./finalApp/script.js","w")
#     b.write(init)
#     b.close()


def writeInput(id):
    with open("./finalApp/script.js", 'a') as file:
        file.write("""
    var x"""+str(id)+""" = document.createElement("INPUT");
    x"""+str(id)+""".setAttribute("type", "number");
    x"""+str(id)+""".setAttribute("value", "");
    x"""+str(id)+""".setAttribute("id", """+str(id)+""")
    document.body.appendChild(x"""+str(id)+""");
        """)
        file.close()

def writeSubmit():
    with open("./finalApp/script.js", 'a') as file:
        file.write("""
    y = document.createElement("INPUT")
    y.setAttribute("type", "submit")
    y.setAttribute("class", "btn btn-primary")
    y.setAttribute("onclick", "onSubmit()")
    document.body.appendChild(y)
    """)
        file.close()

def writeInit():
    with open("./finalApp/script.js",'r+') as file:
        lines = file.readlines()
        length = len(lines)
        file.seek(0)
        lines.insert(0, init1)
        lines.insert(length, init2)
        file.writelines(lines)
        file.close()

def writeSubmitFunction(count, operation):
    with open("./finalApp/script.js", 'a') as file:
        file.write("""
onSubmit = function() {
    var add = 0;
    var operator = '"""+operation+"""'
    for(var i=0; i<"""+str(count)+"""; i++) {
        if(operator === "addition" || operator === "add" || operator === "sum") {
            add = add + Number(document.getElementById(i).value);
        }
        if(operator === "difference" || operator === "subtract" || operator === "subtraction") {
            if(i === 0) {
                add = Number(document.getElementById(i).value);
            } else {
                add = add - Number(document.getElementById(i).value);
            }
        }
    }
    var y = document.createElement("div");
    y.setAttribute("id", "result");
    document.body.appendChild(y);
    document.getElementById('result').innerHTML = add;
}

"""+initCall+"""
    """)
        file.close()
