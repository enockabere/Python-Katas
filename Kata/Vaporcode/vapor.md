# Python code to converts any sentence into a V A P O R W A V E sentence

## Description
Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.

## BDD
The user should:
  -Input a string turn into VaporWave

|      Input          |       Output       |
|---------------------|--------------------|
| string eg = "Hello" | H  E  L  L  O      |


## Pseudocode
- Define **function** to turn string into vaporwave sentence
- Declare  variable **x** to accept input and store a string
- Use **IF condition** and **isUpper()** method to check whether entered string is uppercase.

        then, use join() method to join all items x with double spaces.
- **Else** use Upper()method to turn string to uppercase

    then, use join() method to join all items x with double spaces.


- **Return** Vaporwave sentence

## Python code

```text
def Vapor():
    vaporString = input("Enter String:-\n")
    
    #check if string is uppercase
    
    if vaporString.isupper():
        result="  ".join(vaporString)
        
    #else turn string to uppercase
    else:
        vaporString.upper()
        result="  ".join(vaporString)
    print("*"*5, 'Vaporwave Sentence',"*"*5,"\n", result )
Vapor()
```
## Kata link
[viewkata](https://www.codewars.com/kata/5966eeb31b229e44eb00007a)
