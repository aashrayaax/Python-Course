a = input("Enter the word : ")
t = {
    "Namashkaar" : "Hello",
    "Kya" : "What",
    "Kab" : "When",
    "Nahi" : "No"
}

if(a=="Namashkaar"):
   print(t.get(a))
if(a=="Kya"):
   print(t.get(a))
if(a=="Kab"):
   print(t.get(a))
if(a=="Nahi"):
   print(t.get(a))