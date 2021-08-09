def main():
    #escribe tu código abajo de esta línea
    print("AREA DE UN TRAPECIO")
    print("===================")
    bma=int(input("Dame la base mayor:"))
    bme=int(input("Dame la base menor:"))
    h=int(input("Dame la altura:"))

    a = (bma + bme) * h / 2

    print("Area="+str(a))

if __name__=='__main__':
    main()
