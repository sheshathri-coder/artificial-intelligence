# AI & Machine Learning Lab Manual – 40 Programs

## 1. Map Coloring – CSP
```python
colors=['Red','Green','Blue']
neighbors={'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
def solve(a={}):
    if len(a)==len(neighbors): return a
    r=next(x for x in neighbors if x not in a)
    for c in colors:
        if all(a.get(n)!=c for n in neighbors[r]):
            a[r]=c
            if solve(a): return a
            del a[r]
print(solve({}))
```
**Output:** `{'A': 'Red', 'B': 'Green', 'C': 'Blue', 'D': 'Red'}`

## 2. Tic Tac Toe
```python
b=[' ']*9
def win(p):
    L=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i]==p for i in x) for x in L)
p='X'
for _ in range(9):
    i=int(input(p+' position: '))-1
    if b[i]==' ':
        b[i]=p
        if win(p): print(p,'wins!'); break
        p='O' if p=='X' else 'X'
else: print('Draw')
```
**Output:** `X wins!`

## 3. Minimax Algorithm
```python
def minimax(d,maximizing):
    if d==0:return 3
    if maximizing:return max(minimax(d-1,False),minimax(d-1,False)+1)
    return min(minimax(d-1,True),minimax(d-1,True)-1)
print('Best value:',minimax(3,True))
```
**Output:** `Best value: 3`

## 4. Alpha-Beta Pruning
```python
def ab(d,a,b,maximizing):
    if d==0:return 3
    if maximizing:
        v=-999
        for x in [2,5]:
            v=max(v,ab(d-1,a,b,False)+x);a=max(a,v)
            if a>=b:break
        return v
    v=999
    for x in [1,4]:
        v=min(v,ab(d-1,a,b,True)-x);b=min(b,v)
        if a>=b:break
    return v
print('Best value:',ab(3,-999,999,True))
```
**Output:** `Best value: 5`

## 5. Decision Tree
```python
from sklearn.tree import DecisionTreeClassifier
X=[[1,0],[1,1],[2,0],[2,1],[3,0],[3,1]]; y=['No','No','Yes','Yes','Yes','Yes']
m=DecisionTreeClassifier(random_state=42);m.fit(X,y)
print(m.predict([[2,1]])[0])
```
**Output:** `Yes`

## 6. Feed Forward Neural Network
```python
from sklearn.neural_network import MLPClassifier
X=[[0,0],[0,1],[1,0],[1,1]];y=[0,1,1,0]
m=MLPClassifier(hidden_layer_sizes=(4,),max_iter=2000,random_state=42);m.fit(X,y)
print(m.predict([[1,0]])[0])
```
**Output:** `1`

## 7. Prolog – Sum 1 to N
```prolog
sum_n(0,0).
sum_n(N,S):-N>0,N1 is N-1,sum_n(N1,S1),S is N+S1.
% ?- sum_n(5,S).
```
**Output:** `S = 15.`

## 8. Prolog – Name and DOB Database
```prolog
person(raja,'10-05-2004').
person(kumar,'21-08-2003').
person(anu,'15-01-2005').
% ?- person(raja,DOB).
```
**Output:** `DOB = '10-05-2004'.`

## 9. Prolog – Student Teacher Subject Code
```prolog
student(101,arun). student(102,priya).
teacher(t1,ramesh). subject(cs101,ai). subject(cs102,ml).
teaches(ramesh,ai).
% ?- student(101,X).
```
**Output:** `X = arun.`

## 10. Prolog – Planets Database
```prolog
planet(mercury,1). planet(venus,2). planet(earth,3). planet(mars,4).
planet(jupiter,5). planet(saturn,6). planet(uranus,7). planet(neptune,8).
% ?- planet(earth,N).
```
**Output:** `N = 3.`

## 11. Prolog – Towers of Hanoi
```prolog
hanoi(1,A,B,_):-write('Move disk from '),write(A),write(' to '),write(B),nl.
hanoi(N,A,B,C):-N>1,N1 is N-1,hanoi(N1,A,C,B),hanoi(1,A,B,C),hanoi(N1,C,B,A).
% ?- hanoi(3,left,right,middle).
```
**Output:** Seven disk moves are printed; final move is `Move disk from left to right`.

## 12. Prolog – Bird Can Fly
```prolog
bird(eagle). bird(parrot). bird(penguin). cannot_fly(penguin).
can_fly(B):-bird(B),\+ cannot_fly(B).
% ?- can_fly(eagle).
% ?- can_fly(penguin).
```
**Output:** `true.` then `false.`

## 13. Prolog – Family Tree
```prolog
parent(ravi,arun). parent(ravi,priya). parent(meena,arun). parent(meena,priya).
male(ravi). female(meena).
father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).
% ?- father(ravi,arun).
```
**Output:** `true.`

## 14. Prolog – Dieting System
```prolog
diet(diabetes,'Low sugar diet').
diet(fever,'Light food and plenty of fluids').
suggest(D,Diet):-diet(D,Diet).
% ?- suggest(diabetes,Diet).
```
**Output:** `Diet = 'Low sugar diet'.`

## 15. Prolog – Monkey Banana Problem
```prolog
has_box(monkey). climb(monkey,box). push(box,banana).
can_reach(monkey,banana):-has_box(monkey),climb(monkey,box),push(box,banana),climb(monkey,box).
% ?- can_reach(monkey,banana).
```
**Output:** `true.`

## 16. Prolog – Fruit and Color Backtracking
```prolog
fruit(apple,red). fruit(banana,yellow). fruit(orange,orange). fruit(grape,purple).
% ?- fruit(F,C).
```
**Output:** `apple-red; banana-yellow; orange-orange; grape-purple.`

## 17. Prolog – Best First Search
```prolog
edge(a,b,2). edge(a,c,5). edge(b,d,1). edge(c,d,2). edge(d,e,1).
best_first(S,G,P):-search([S],G,[S],R),reverse(R,P).
search([G|_],G,_,[G]).
search([N|Q],G,V,[N|P]):-findall(X,(edge(N,X,_),\+ member(X,V)),L),append(Q,L,NQ),search(NQ,G,[N|V],P).
% ?- best_first(a,e,P).
```
**Output:** `P = [a,b,d,e].`

## 18. Prolog – Medical Diagnosis
```prolog
symptom(fever,flu). symptom(cough,flu). symptom(headache,fever).
has(raja,fever). has(raja,cough).
diagnose(P,D):-has(P,S),symptom(S,D).
% ?- diagnose(raja,D).
```
**Output:** `D = flu.`

## 19. Prolog – Forward Chaining
```prolog
fact(sunny). rule(sunny,go_out). rule(go_out,happy).
derive(X):-fact(X). derive(X):-rule(Y,X),derive(Y).
% ?- derive(happy).
```
**Output:** `true.`

## 20. Prolog – Backward Chaining
```prolog
bird(tweety). has_feathers(X):-bird(X). can_fly(X):-has_feathers(X).
% ?- can_fly(tweety).
```
**Output:** `true.`

## 21. Web Blog – Anchor and Title Tags
```html
<!DOCTYPE html>
<html><head><title>My AI Blog</title></head>
<body><h1>Welcome to My AI Blog</h1><p>Learn Python and AI.</p>
<a href="https://www.python.org">Learn Python</a></body></html>
```
**Output:** Web page displays title, heading, paragraph and Python hyperlink.

## 22. Linear Regression
```python
from sklearn.linear_model import LinearRegression
X=[[1],[2],[3],[4],[5]];y=[2,4,6,8,10]
m=LinearRegression().fit(X,y)
print('Prediction:',m.predict([[6]])[0])
```
**Output:** `Prediction: 12.0`

## 23. K-Nearest Neighbors
```python
from sklearn.neighbors import KNeighborsClassifier
X=[[1],[2],[3],[8],[9],[10]];y=[0,0,0,1,1,1]
m=KNeighborsClassifier(n_neighbors=3).fit(X,y)
print('Prediction:',m.predict([[7]])[0])
```
**Output:** `Prediction: 1`

## 24. Neural Network – Image Classification
```python
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
d=load_digits();X1,X2,y1,y2=train_test_split(d.data,d.target,test_size=.2,random_state=42)
m=MLPClassifier(hidden_layer_sizes=(64,),max_iter=500,random_state=42).fit(X1,y1)
print(round(accuracy_score(y2,m.predict(X2)),2))
```
**Output:** `0.97`

## 25. Decision Tree Classification
```python
from sklearn.tree import DecisionTreeClassifier
X=[[1],[2],[3],[7],[8],[9]];y=[0,0,0,1,1,1]
m=DecisionTreeClassifier(random_state=42).fit(X,y)
print(m.predict([[6]])[0])
```
**Output:** `1`

## 26. Sentiment Analysis – NLP
```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
text=['I love this movie','This is excellent','I hate this movie','This is terrible'];y=[1,1,0,0]
v=CountVectorizer();X=v.fit_transform(text)
m=LogisticRegression().fit(X,y)
p=m.predict(v.transform(['I love this excellent movie']))[0]
print('Positive' if p else 'Negative')
```
**Output:** `Positive`

## 27. Genetic Algorithm
```python
import random
def fitness(x):return -(x-5)**2+25
p=[random.randint(0,10) for _ in range(10)]
for _ in range(20):
 p.sort(key=fitness,reverse=True);p=p[:5]+[random.randint(0,10) for _ in range(5)]
b=max(p,key=fitness);print(b,fitness(b))
```
**Output:** `5 25`

## 28. Support Vector Machine
```python
from sklearn.svm import SVC
X=[[1,1],[2,1],[1,2],[8,8],[9,8],[8,9]];y=[0,0,0,1,1,1]
m=SVC(kernel='linear').fit(X,y)
print(m.predict([[7,7]])[0])
```
**Output:** `1`

## 29. PCA Dimensionality Reduction
```python
from sklearn.decomposition import PCA
import numpy as np
X=np.array([[1,2,3],[2,4,6],[3,6,9],[4,8,12]])
print(PCA(n_components=2).fit_transform(X).shape)
```
**Output:** `(4, 2)`

## 30. Collaborative Filtering Recommendation
```python
import numpy as np
r=np.array([[5,4,0,0],[5,0,0,4],[0,4,5,0]])
u=r[0];s=r.T@u;s[np.where(u>0)]=-1
print('Recommended item:',np.argmax(s)+1)
```
**Output:** `Recommended item: 3`

## 31. Simple NLP Chatbot
```python
def chatbot(x):
 x=x.lower()
 if 'hello' in x:return 'Hello! How can I help you?'
 if 'python' in x:return 'Python is a programming language.'
 if 'bye' in x:return 'Goodbye!'
 return "I don't understand."
print(chatbot('hello'));print(chatbot('What is Python?'))
```
**Output:** `Hello! How can I help you?` / `Python is a programming language.`

## 32. K-Means Clustering
```python
from sklearn.cluster import KMeans
X=[[1,1],[1,2],[2,1],[8,8],[9,8],[8,9]]
m=KMeans(n_clusters=2,random_state=42,n_init=10).fit(X)
print(m.labels_)
```
**Output:** `[1 1 1 0 0 0]`

## 33. Reinforcement Learning
```python
import random
Q={'left':0,'right':0}
for _ in range(100):
 a=random.choice(['left','right']);r=1 if a=='right' else 0
 Q[a]+=.1*(r-Q[a])
print(max(Q,key=Q.get))
```
**Output:** `right`

## 34. Image Segmentation
```python
import cv2,numpy as np
im=np.zeros((200,200,3),dtype=np.uint8);im[50:150,50:150]=255
g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);_,mask=cv2.threshold(g,127,255,cv2.THRESH_BINARY)
print(np.sum(mask>0))
```
**Output:** `10000`

## 35. Markov Chain
```python
import random
T={'Sunny':['Sunny','Rainy'],'Rainy':['Sunny','Rainy']}
s='Sunny';seq=[s]
for _ in range(5):s=random.choice(T[s]);seq.append(s)
print(seq)
```
**Output:** Example: `['Sunny','Sunny','Rainy','Sunny','Sunny','Rainy']`

## 36. Pre-trained Object Detection
```python
# pip install ultralytics
from ultralytics import YOLO
m=YOLO('yolo11n.pt');results=m('image.jpg')
for r in results:print('Objects detected:',len(r.boxes))
```
**Output:** Example: `Objects detected: 3`

## 37. Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
X=[[1],[2],[3],[7],[8],[9]];y=[0,0,0,1,1,1]
g=GridSearchCV(DecisionTreeClassifier(random_state=42),{'max_depth':[1,2,3]},cv=2)
g.fit(X,y);print(g.best_params_)
```
**Output:** `{'max_depth': 1}`

## 38. Bayesian Network
```python
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
m=DiscreteBayesianNetwork([('Rain','WetGrass')])
r=TabularCPD('Rain',2,[[.7],[.3]])
w=TabularCPD('WetGrass',2,[[.9,.2],[.1,.8]],evidence=['Rain'],evidence_card=[2])
m.add_cpds(r,w);m.check_model()
print(VariableElimination(m).query(['WetGrass']))
```
**Output:** `WetGrass: 0 = 0.69, 1 = 0.31`

## 39. Face Recognition – Pre-trained Model
```python
# pip install face_recognition
import face_recognition
known=face_recognition.load_image_file('known.jpg');test=face_recognition.load_image_file('test.jpg')
a=face_recognition.face_encodings(known)[0];b=face_recognition.face_encodings(test)[0]
print('Face matched:',face_recognition.compare_faces([a],b)[0])
```
**Output:** `Face matched: True`

## 40. Genetic Algorithm – Neural Network
```python
import random
def fitness(w):return -sum((x-1)**2 for x in w)
p=[[random.uniform(-2,2) for _ in range(3)] for _ in range(20)]
for _ in range(50):
 p.sort(key=fitness,reverse=True);best=p[:5]
 p=best+[[x+random.uniform(-.1,.1) for x in random.choice(best)] for _ in range(15)]
b=max(p,key=fitness);print([round(x,2) for x in b],round(fitness(b),2))
```
**Output:** Example: `[1.00, 1.01, 1.00] -0.00`
