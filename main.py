import os
import profileEdit as pe
from tkinter.filedialog import askopenfilename
def DumpFile():
    # Choose a file to load
    g_inputFilePath = askopenfilename(initialdir=pe.GetCurrentDirectory()+os.sep+"input", defaultextension=".jkr", filetypes=[("Balatro Profile Files", "*.jkr")])
    if g_inputFilePath == "" or g_inputFilePath ==(): # win and linux
        print("No file selected.")
        exit()
    print(f"Selected file: {g_inputFilePath}")

    # save to dumped dir
    pe.dump(g_inputFilePath)
    print("File dumped to", pe.GetCurrentDirectory()+os.sep+"dumped"+os.sep+"dumped.txt")
    print("What to do next? Search for 'all_unlocked' in the dumped.txt and set it to false. Save the file and choose 'recompress' option.")

def RecompressFile():
    g_inputFilePath = askopenfilename(initialdir=pe.GetCurrentDirectory()+os.sep+"dumped", defaultextension=".txt", filetypes=[("Balatro Profile Dump", "*.txt")])
    if g_inputFilePath == "" or g_inputFilePath ==(): # win and linux
        print("No file selected.")
        exit()
    print(f"Selected file: {g_inputFilePath}")
    savepath = pe.recompress(g_inputFilePath)
    print("File recompressed to", savepath)
    print("What to do next? Replace the original profile.jkr with the newly created file. Have fun gambling!")

# Credits to problemsalved
# Also worth noting you NEED python3.11, otherwise zlib.compress() will  not work
if __name__ == '__main__':
    # show menu of 2 options
    print("Usage: Place your profile.jkr in the input folder and select option '1' to dump it.")
    print("1. Dump a file")
    print("2. Recompress a file")
    choice = input("Enter your choice: ")
    if choice == "1":
        DumpFile()
    elif choice == "2":
        RecompressFile()
    else:
        print("Invalid choice")
        exit()



