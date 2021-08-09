def main():
    #escribe tu código abajo de esta línea
    print("AREA DE UN RECTANGULO")
    print("=====================")
    l=int(input("Dame la base:"))
    h=int(input("Dame la altura:"))

    p = 2 * (h + l)
    a = h * l

    print("Perimetro="+str(p))
    print("Area="+str(a))

if __name__=='__main__':
    main()
