import random
"""
MY FIRST XOX GAME
"""
xkazanma = 0
ykazanma = 0
while True:
    try:
        kactur = int(input("Kaç Olan kazansın? :"))
        break
    except:
        print("Geçersiz tur sayisi")

while True:
    hamlesayisi = 0
    gameboard = {1: " ", 2: " ", 3: " ",
                 4: " ", 5: " ", 6: " ",
                 7: " ", 8: " ", 9: " "}

    keys = []
    for i in gameboard:
        keys.append(i)


    def oyunTahtası(board):
        print(gameboard[1] + " | " + gameboard[2] + " | " + gameboard[3])
        print("--+---+--")
        print(gameboard[4] + " | " + gameboard[5] + " | " + gameboard[6])
        print("--+---+--")
        print(gameboard[7] + " | " + gameboard[8] + " | " + gameboard[9])

    def botHamlesiX():
        global hamlesayisi
        while True:
            sira = "O"
            islem2 = random.randint(1,9)
            if gameboard[islem2] == "X":
                continue
            elif gameboard[islem2] == "O":
                continue
            else:
                gameboard[islem2] = "O"
                hamlesayisi += 1
                break
        oyunTahtası(gameboard)

    def hamleyapX():
        global hamlesayisi
        while True:
            sira = "X"
            islem = int(input("Sira " + sira + " da. Hamlenizi yapiniz:"))
            if gameboard[islem] == "O":
                print("Geçersiz işlem.")
            elif gameboard[islem] == "X":
                print("Geçersiz işlem.")
            else:
                gameboard[islem] = "X"
                hamlesayisi += 1
                break

        oyunTahtası(gameboard)


    def hamleyapO():
        global hamlesayisi
        while True:
            sira = "O"
            islem2 = int(input("Sira " + sira + " da.Hamlenizi yapiniz:"))
            if gameboard[islem2] == "X":
                print("Geçersiz işlem.")
            elif gameboard[islem2] == "O":
                print("Geçersiz işlem.")
            else:
                gameboard[islem2] = "O"
                hamlesayisi += 1
                break

        oyunTahtası(gameboard)


    def oyunBittimi(gameboard):
        global xkazanma
        global ykazanma
        if hamlesayisi >= 9:
            print("Oyun berabere")
            return True
        elif gameboard[1] == gameboard[2] == gameboard[3] == "X":
            print("X kazandı.")
            xkazanma +=1
            return True
        elif gameboard[1] == gameboard[4] == gameboard[7] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[1] == gameboard[5] == gameboard[9] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[2] == gameboard[5] == gameboard[8] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[3] == gameboard[5] == gameboard[7] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[3] == gameboard[6] == gameboard[9] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[4] == gameboard[5] == gameboard[6] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[4] == gameboard[5] == gameboard[6] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[1] == gameboard[2] == gameboard[3] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[7] == gameboard[8] == gameboard[9] == "X":
            print("X kazandı.")
            xkazanma += 1
            return True
        elif gameboard[1] == gameboard[4] == gameboard[7] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True
        elif gameboard[1] == gameboard[5] == gameboard[9] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True
        elif gameboard[2] == gameboard[5] == gameboard[8] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True
        elif gameboard[3] == gameboard[5] == gameboard[7] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True
        elif gameboard[3] == gameboard[6] == gameboard[9] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True
        elif gameboard[4] == gameboard[5] == gameboard[6] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True
        elif gameboard[4] == gameboard[5] == gameboard[6] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True
        elif gameboard[7] == gameboard[8] == gameboard[9] == "O":
            print("O kazandı.")
            ykazanma += 1
            return True

        return False


    oyunTahtası(gameboard)
    oyuntipi = input("Tek/Cift kişilik:")
    while (oyunBittimi(gameboard) == False):

        if oyuntipi == "Cift":
            hamleyapX()
            if oyunBittimi(gameboard) == True:
                break
            hamleyapO()
            if oyunBittimi(gameboard) == True:
                break
        elif oyuntipi == "Tek":
            hamleyapX()
            if oyunBittimi(gameboard) == True:
                break
            botHamlesiX()
            if oyunBittimi(gameboard) == True:
                break
    print("Oyun bitti.")
    print("X:" + str(xkazanma) + " O:" + str(ykazanma))
    if xkazanma == kactur:
        print("Oyunu X TARAFI KAZANMIŞTIR.")

        break
    elif ykazanma == kactur:
        print("OYUNU O TARAFI KAZANMIŞTIR.")
        break
    #if "Y" == input("Tekrar oynamak istermisiniz? Y/N"):
     #   continue
    #else:
     #   break