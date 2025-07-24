player1 = input("Enter Player 1's name: ")
player2 = input("Enter Player 2's name: ")      


#Primero introducir los jugadores
#Ahora asignarles un string que sea "piedra papel o tijera  "


player1_choice = input("{player1}, Elige entre: 'piedra', 'papel', or 'tijera': ")
player1_choice = player1_choice.lower()

player2_choice = input("{player2}, Elige entre: 'piedra', 'papel', or 'tijera': ")
player2_choice = player2_choice.lower()

# Ahora comparar las elecciones de los jugadores
if player1_choice == player2_choice:
    print("¡Es un empate!") 
elif (player1_choice == "piedra" and player2_choice == "tijera") or \
     (player1_choice == "papel" and player2_choice == "piedra") or \
     (player1_choice == "tijera" and player2_choice == "papel"):   

        print(player1 + " gana con " + player1_choice + " contra " + player2_choice + " de " + player2 + "!")

elif (player2_choice == "piedra" and player1_choice == "tijera") or \
     (player2_choice == "papel" and player1_choice == "piedra") or \
     (player2_choice == "tijera" and player1_choice == "papel"):    

    print(player2 + " gana con " + player2_choice + " contra " + player1_choice + " de " + player1 + "!")
 



