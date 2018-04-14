from MovieBooking import *



if __name__=='__main__':
    showmoviesall()

    moviec+=1
    newmovie(moviec,"AmericanPie",120,200)

    moviec+=1
    newmovie(moviec,"La La Land",100,80)
    showmoviesall()

    showmovie(2)

    book(2,3)

    showmovie(2)

    refundseat(2,3)

    showmovie(2)

    removemovie(4)

    showmoviesall()
