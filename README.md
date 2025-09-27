# Vigenere Cipher Breaker

This project is my homework task.  
The goal was to **break a Vigenere cipher** when the key length is known.

---

## Approach

I used a simple idea:

1. The Vigenere cipher repeats the key over and over again.  
   If the key length is 3, then every 1st, 4th, 7th letter is shifted the same way,  
   every 2nd, 5th, 8th letter is shifted the same way, and so on.

2. That means the encrypted text can be split into groups, and each group looks like a **Caesar cipher**.

3. To guess the shift for each group, I looked at **letter frequencies** in Czech language.  
   (For example, the letter `E` is very common.)

4. I calculated which shift makes the frequencies look most similar to Czech.  
   This gave me one letter of the key.

5. After finding all letters of the key, I decrypted the full text.

---

## Example

Input (encrypted text):  