import os, re
Pydir = 'D:\Python\PycharmProjects'
pattern = re.compile(r'(.py)$')
codelist = [0, 0, 0, 0]

def Countcode(pyloc) :
    global codelist
    with open(pyloc, encoding='utf-8') as f:
        code_line = 0
        blank_line = 0
        comment_line = 0
        total_line = 0
        txt = f.readlines()
        for line in txt:
            total_line += 1
            if line.strip().startswith('#'):
                comment_line += 1
            elif len(line.strip()):
                blank_line += 1
            else:
                code_line += 1

        codelist[0] = codelist[0] + code_line
        codelist[1] = codelist[1] + blank_line
        codelist[2] = codelist[2] + comment_line
        codelist[3] = codelist[3] + total_line
        print("pyloc %s\n code_line : %d blank_line : %d comment_line : %d total_line : %d " %
              (pyloc,code_line, blank_line, comment_line, total_line))
        return codelist


def Process_all_py(Pydir):
    list = os.listdir(Pydir) # 总是记不住这句 ！！！ 唉
    for f in list:
        fn = os.path.join(Pydir, f)
        if os.path.isdir(fn):
            Process_all_py(fn)
        else:
            pyloc = os.path.join(Pydir, fn)
            file, type = os.path.splitext(pyloc)
            if (pattern.match(type)):
                Countcode(pyloc)


if __name__=='__main__':
    Process_all_py(Pydir)

