import os, platform, getpass

OS = platform.system()
username = getpass.getuser()


def cd(tokens):
    try:
        white = False
        try:
            temp = tokens[1]
        except:
            white = True
            if white:
                if OS == "Windows":
                    os.chdir("C:\\Users\\" + username)
                else:
                    os.chdir("/home/" + username)
        else:
            path=''.join(tokens[1:])
            path=path.replace('"','')
            path=path.replace("'","")
            os.chdir(path)
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
