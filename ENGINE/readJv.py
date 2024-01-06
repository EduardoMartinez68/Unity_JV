readC=False
readT=False
readComment=False

#vsce package
def read_line_for_line(file,output_file):
    global readComment
    for line in file:
        words = line.split()  

        textClass=''
        #we will see if this line is a class
        sizeWord=len(words)
        if sizeWord>0:
            #we will see if the line is a import 
            if words[0]=='import' and sizeWord>=2:
                textClass=create_library_section(words)
                print(textClass)
            if words[0] in "class":
                words[1]=words[1].replace(':','')
                words[1]=words[1].replace('(',':')
                words[1]=words[1].replace(')','')
                textClass='public class '+words[1]+'{'

        #If we are reading a class, update it
        if textClass=='':
            read_word_for_word(words,output_file)
            #add_semicolon(line,output_file)
        else:
            output_file.write(textClass)
        readComment=False
        output_file.write('\n')



def create_library_section(words):
    section=''

    #get the library import      
    package=words[1] 

    #read all the library from the index 2
    for library in words[2:]:
        library=library.replace("'",'')
        #We will see if we have the same library as the package.
        if library=='.':
            section+=f'using {package};\n'
        else:
            #create the import 
            section+=f'using {package}.{library};\n'
    
    return section

def add_semicolon(line,output_file):
    if '--' in line:
        pass 
    elif '//' in line:
        pass 
    elif ':' in line:
        pass
    elif 'end' in line:
        pass 
    elif '{' in line:
        pass
    elif '@' in line:
        pass
    elif '}' in line:
        pass
    elif 'if' in line:
        pass
    elif 'else' in line:
        pass
    elif 'for' in line:
        print(line)
    elif 'while' in line:
        pass
    else:
        if not line.isspace():
            output_file.write(';')
            
def read_word_for_word(words,output_file):
    #we will see if the array not is empty
    if not words:
        return 
    
    #if the array not is empty we will watch if in the words exist a <code> for not add semicolon 
    semicolon=False
    for index, word in enumerate(words): #we will read all word
        code=read_syntax(word)   #get the new syntax cpp of unity

        #we will watch if not is reading code C#
        if not readC:
            semicolon=this_word_is_a_code(word,semicolon) 
            if '--' in word:
                if not index==0:
                    output_file.write(';')

        output_file.write(code)
    
    #we will watch if not is reading code C#
    if not readC:
        if not semicolon: #if there is not <code> we add semicolon
            output_file.write(';')

def this_word_is_a_code(word,semicolon):
    #we will see if the word is a function 
    if ':' in word:
        return True
    
    if '@' in word:
        return True
    
    #we will see if the word is a code 
    codes=['if','else','end',':','--','for','foreach','while','@']
    for code in codes:
        if word==code:
            return True 
        
    return semicolon

def read_syntax(word):
    #we will replace the syntax 
    answer=''

    #we will see if the word is with that
    global readC,readT,readComment

    #we will see if exist a component 
    if 'import'==word:
        answer='using '
    elif 'class'==word:
        answer='public '+word 
    elif 'start'==word:
        answer='Start(){'
    elif 'update'==word:
        answer='Update(){'
    elif 'if'==word:
        answer='if ('
    elif word=='do':
        answer=word.replace('do', '){')
    elif 'for'==word:
        answer='for ('
    elif 'foreach'==word:
        answer='foreach ('
    elif 'while'==word:
        answer='while ('
    elif 'else'==word:
        answer='}'+word+'{'
    elif ':' in word:
        answer=word.replace(':', '{')
    elif 'end'==word:
        answer=word.replace('end', '}')


    #we will see if this is a command 
    elif '#' in word:
        answer=word.replace('#', '//')
    elif '--' in word:
        word=word.replace('--', '//')
        readComment=True
    elif 'str' in word:
        answer=word.replace('str', 'string ')
    elif 'print' in word:
        answer=word.replace('print', 'Debug.Log')
    elif '<RB>' in word:
        answer=word.replace('<RB>', 'GetComponent<RigidBody>()')
        return answer
    elif '@' in word:
        readC=not readC
        return ''
    else:
        answer=word 

    if "'" in answer:
        answer=answer.replace("'", '"')
        #readT=not readT

    #this is for create a component
    if '<' in word and '>' in word:
        nameComponent = word[word.find('<') + 1:word.find('>')]
        answer = f"{word.split('=')[0]}=GetComponent<{nameComponent}>()"

    
    #we will see if is reading c++ or <lio>
    if readC or readComment or readT:
        return word+' '
    else:
        answer=answer
        return answer+' '

def read_file(pathFile,pathFileUnity):
    try:
        with open(pathFile, 'r') as file:
            #create the file c# of unity
            with open(pathFileUnity, 'w') as output_file:
                read_line_for_line(file,output_file)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {pathFile}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

#path