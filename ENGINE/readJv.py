readC=False
readT=False

#vsce package
def read_line_for_line(file,output_file):
    for line in file:
        words = line.split()  
        textClass=''
        #we will see if this line is a class
        if len(words)>0:
            if words[0] in "class":
                words[1]=words[1].replace(':','')
                words[1]=words[1].replace('(',':')
                words[1]=words[1].replace(')','')
                textClass='public class '+words[1]+'{'

        #If we are reading a class, update it
        if textClass=='':
            read_word_for_word(words,output_file)
            add_semicolon(line,output_file)
        else:
            output_file.write(textClass)
        output_file.write('\n')


def add_semicolon(line,output_file):
    if '#' in line:
        pass 
    if '//' in line:
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
    elif 'do' in line:
        pass
    else:
        if not line.isspace():
            output_file.write(';')

def read_word_for_word(words,output_file):
    for word in words:
        code=read_syntax(word)  
        output_file.write(code)

def read_syntax(word):
    #we will replace the syntax 
    answer=''
    global readC,readT
    if 'import' in word:
        answer='using '
    elif 'class' in word:
        answer='public '+word 
    elif 'start' in word:
        answer='Start(){'
    elif 'update' in word:
        answer='Update(){'
    elif 'on_collider_enter' in word:
        answer=word.replace('on_collider_enter', 'onColliderEnter')
    elif 'on_collider_exit' in word:
        answer='onColliderExit('
    elif 'if' in word:
        answer='if ('
    elif 'for' in word:
        answer='for ('
    elif 'while' in word:
        answer='while ('
    elif 'do' in word:
        answer=word.replace('do', '){')
    elif 'else' in word:
        answer='}'+word+'{'
    elif ':' in word:
        answer=word.replace(':', '{')
    elif 'end' in word:
        answer='}'
    elif '#' in word:
        answer=word.replace('#', '//')
    elif '--' in word:
        answer=word.replace('--', '//')
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
        readT=not readT
    #this is if the user need a variable public or private
    '''
    if '>' in answer:
        answer=answer.replace('>', 'public ')
    elif '<' in answer:
        answer=answer.replace('<', 'private ')
    '''

    #this is for create a component
    if '<' in word and '>' in word:
        nameComponent = word[word.find('<') + 1:word.find('>')]
        answer = f"{word.split('=')[0]}=GetComponent<{nameComponent}>()"

    
    
    #we will see if is reading c++ or <lio>
    if readC:
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
