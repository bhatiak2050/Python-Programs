def rps(p1,p2):
    if p1[2]==p2[2]:
        print("Draw");
    if p1[2]=='rock' and p2[2]=='paper':
        print(p2[1], "Wins!");
    if p1[2]=='rock' and p2[2]=='sissor':
        print(p1[1], "Wins!");
    if p1[2]=='paper' and p2[2]=='rock':
        print(p1[1], "Wins!");
    if p1[2]=='paper' and p2[2]=='sissor':
        print(p2[1], "Wins!");
    if p1[2]=='sissor' and p2[2]=='rock':
        print(p2[1], "Wins!");
    if p1[2]=='sissor' and p2[2]=='paper':
        print(p1[1], "Wins!");

p1={1:"EMPTY", 2:"EMPTY"}
p2={1:"EMPTY", 2:"EMPTY"}
p1[1] = input("Enter Player one's name: ")
p2[1] = input("Enter Player two's name: ")         

for i in range(10):
         p1[2] = input("Player one: ")
         p2[2] = input("Player two: ")
         p1[2] = p1[2].lower()
         p2[2] = p2[2].lower()
         rps(p1,p2)
        
