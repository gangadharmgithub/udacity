__author__='Gangadhar Mylapuram'
import webbrowser
import time
def main():
     total_breaks = 0
     while (total_breaks < 3):
        print ("Take a break @" + time.ctime())
        #image = Image.open("C:\\Users\\Gangadhar\\Downloads\\takeabreak.png");
        #image.show();
        #del image;
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)
        #response = input("Do you want a break after two hours (yes(y))? :")
        
        #if (response != "yes" and response != "y"):
        #    print ("Exiting the program TAKE A BREAK")
        #    break
        #else:
        time.sleep(7200)
        total_breaks = total_breaks + 1;
if (__name__ ==  "__main__"):
    main();
    
