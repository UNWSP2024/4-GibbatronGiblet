# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():

    ######################
    movie_number = int(input("Enter the number of movies you want to see: "))
    title = 0
    tickets = 0

    for movie in range(movie_number):
        title = input(f"What is the name of movie #{movie + 1}?")
        current_tickets = int(input("How many tickets do you want for this movie?"))
        tickets += current_tickets
    print(f"You want {tickets} tickets.")

    #Written by Logan Gibson on 9/25/25. The program's name is "Movie Ticket Purchaser"

    ######################


if __name__ == '__main__':
    main()