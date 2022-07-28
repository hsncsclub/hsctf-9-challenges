## cryptography/quagmire-i
#### Author: wooshi
#### 193 solves / 264 points

Bob was on his way to school and go to Mr. Connolly’s first period AP CSA class, but it was a rainy day and he got stuck in the quagmire in his town, making him late to school (specifically the first closest to his home, there are apparently four quagmires in his town)! Could you figure out what Mr. Connolly told Bob’s class? His classmate Alice sent this text message after class (written in Quagmire I):

```sh
Plaintext keyword: CONNOLLYROCKS
Indicator keyword: HSCTF
Indicator position: A
Ciphertext: LZXORNZBUYWNRARNOVGCLSQWJEFJFE
```

(Please wrap the flag in the flag format “flag{}”, and use only uppercase letters within the braces.)

Flag: flag{FILLTHISBOWLWITHYOURFAVEFRUITS}

## Solution
Using the Quagmire I cipher (as detailed [here](https://sites.google.com/site/cryptocrackprogram/user-guide/cipher-types/substitution/quagmire)), decrypt the ciphertext as shown below:

```sh
CONLYRKSABDEFGHIJMPQTUVWXZ
ZABCDEFGHIJKLMNOPQRSTUVWXY
KLMNOPQRSTUVWXYZABCDEFGHIJ
UVWXYZABCDEFGHIJKLMNOPQRST
LMNOPQRSTUVWXYZABCDEFGHIJK
XYZABCDEFGHIJKLMNOPQRSTUVW
```

Ciphertext: LZXOR NZBUY WNRAR NOVGC LSQWJ EFJFE

Plaintext:  FILLT HISBO WLWIT HYOUR FAVEF RUITS
