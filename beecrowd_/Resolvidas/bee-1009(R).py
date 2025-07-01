a = str(input())
b = str(input())
c = str(input())

cadeia =  {"vertebrado": {
           "ave": {
               "carnivoro": 
                   {"aguia"}, 
                "onivoro": 
                   {"pomba"}},
            "mamifero": {
                "onivoro": 
                    {"homem"}, 
                "herbivoro": 
                    {"vaca"}}
            },   
            "invertebrado": {
                "inseto": {
                    "hematofago": 
                        {"pulga"}, 
                        "herbivoro": 
                        {"lagarta"}},
                    "anelideo": {
                        "hematofago": 
                            {"sanguessuga"}, 
                        "onivoro": 
                            {"minhoca"}}
                }}

d = cadeia[a][b][c]

print(*d)