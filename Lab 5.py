"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    LAB 5
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Create a file that include a main() and 2 other functions:
        • One function will use write() method to create an output file that contains three of your
        best friends’ full name.
        • Another function will have a list that contains 4 of your favorite movie titles. Use
        writelines() method to write the content of the list onto another file that you need to
        create.
"""
def main():
    outfile = open("BestFriends.txt", 'w')
    useWrite(outfile)
    outfile = open("FavoriteMovies.txt", 'w')
    useWriteLines(outfile)
    print("check if the files are created.")

def useWrite(outfile):
    outfile.write("Jacob Ricker\n")
    outfile.write("Richard Westhaver\n")
    outfile.write("Sam Watson\n")
    outfile.close()
    
def useWriteLines(outfile):
    listMovies = ["Forrest Gump", "Good Will Hunting", "Interstellar", "Arrival"]
    for i in range(len(listMovies)):
        listMovies[i] = listMovies[i] + "\n"
    outfile.writelines(listMovies)
    outfile.close()

main()