# return masked string
def maskify(cc):
    cc=cc.replace(cc[:-4],"#"*(len(cc)-4))
    return cc