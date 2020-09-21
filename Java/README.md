## Source Project: ##

https://boyslife.org/about-scouts/merit-badge-resources/programming/42481/java/

## Industry: ##

Internet.

## Changes: ##

Fixed the broken input scanning, added output of temperature in Celsius, converion to Kelvin, and output of Kelvin.

## How to Run: ##

`java <FTC_New | FTC_Old>`. I already compiled it (gotta love those hybrid interpreters!), so you don't need to bother with `javac`.

## Program Logic ##

```
<start>
   |
<for loop (5 reps)>
         |
    if input is a double
              |
           input -> Farenheit
           Farenheit -> Celsius
           Farenheit -> Kelvin
              |
           Display values
    else display error message, exit program
<end for loop>
  |
<exit program>
```
