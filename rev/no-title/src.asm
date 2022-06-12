# match 
array [119, 113, 215, 125, 223, 163, 121, 211, 127, 231, 223, 111, 197, 209, 163, 215, 195, 197, 193, 117, 209, 211, 235, 223, 117, 209]
# indicies
array [7,  18, 2,  5,  16, 1,  3,  14, 6,  13, 21, 12, 4, 17, 9,  10, 19, 24, 20, 11, 25, 22, 15, 23, 0,  8]
jump main


# input via r4, output via r4
fun: const 5
pop r5
xor r4 r4 r5
add r4 r4 r4
add r4 r4 r7
ret


# r3 = indicies[i], r4 = tmp, r[5] = l[i], r1 = i
swap: const 26
pop r2
mov r1 r0
swap_start: add r3 r1 r2
load r3 r3
load r4 r3

load r5 r1
store r3 r5

store r1 r4

add r1 r1 r7
sub r3 r1 r2
jump swap_start ifl

ret


main: const 26
pop r1
const 1
pop r7
inp_start:getc
sub r1 r1 r7
jump inp_start ifnz
call swap

# l[i] = r4
mov r1 r0
add r6 r2 r2 
loop_start: load r4 r1
call fun
const 23
pop r5
xor r4 r4 r5
add r4 r4 r7

add r5 r1 r6
load r5 r5

xor r4 r4 r5
puts "Wrong!\n" ifnz
ret ifnz 

add r1 r1 r7
sub r3 r1 r2
puts "Correct!\n" ife
ret ife
jump loop_start