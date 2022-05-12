#모든 알파벳과 공백 ''이 요소로 들어있는 리트 하나를 만들고, 리스트 명을 alphabet 으로 해주세요
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
#0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
#a b c d e f g h i j k l m n o p q r s t u v w x y z
#0부터 9까지 숫자와 문자 '-'가 들어있는 리스트 하나를 만들고, 리스트 명을 number로 해주세요
number = [0,1,2,3,4,5,6,7,8,9,10,"-"]

sentence1 = alphabet[22] + alphabet[4] + alphabet[26] + alphabet[0] + alphabet[17] + alphabet[4] + alphabet[26] + alphabet[18] + alphabet[10] + alphabet[7] + alphabet[20] + alphabet[26] + alphabet[11] + alphabet[8] + alphabet[10] + alphabet[4] + alphabet[11] + alphabet[8] + alphabet[14] + alphabet[13] 
print(sentence1)
sentence2 = alphabet[7] + alphabet[0] + alphabet[2] + alphabet[10] + alphabet[26] + alphabet[24] + alphabet[14] + alphabet[20] + alphabet[17] + alphabet[26] + alphabet[11] + alphabet[8] + alphabet[5] + alphabet[4]
print(sentence2)
sentence3 = alphabet[12] + alphabet[24] + alphabet[26] +  alphabet[13] + alphabet[0] + alphabet[12] + alphabet[4] + alphabet[26] + alphabet[8] + alphabet[18] + alphabet[26] + alphabet[10] + alphabet[14] + alphabet[24] + alphabet[20] + alphabet[9] + alphabet[8] + alphabet[13]  
print(sentence3)
#14 26 24 20 26 9 8 13 
#alphabet리스트에서 인덱싱을 이용해 문장 3개 
# 'we are skhu likelion' / 'hack your life' 
# / 'my name is 000' 를 만들어 각각 문자열 변수에 
# 저장해준 후, print()문을 이용해 터미널에 출력되도록 해주세요
birthday = str(number[2]) + str(number[0]) + str(number[0]) + str(number[2]) + str(number[1]) + str(number[2]) + str(number[3]) + str(number[0])
print("제 생일은 %s입니다." % birthday)
phone = str(number[0]) + str(number[1]) + str(number[0]) + str(number[11]) + str(number[4]) + str(number[9]) + str(number[1]) + str(number[6]) + str(number[11]) + str(number[2]) + str(number[9]) + str(number[9]) + str(number[4])
print("제 전화번호는 %s입니다." % phone)
studentid = str(number[2]) + str(number[0]) + str(number[2]) + str(number[2]) + str(number[1]) + str(number[2]) + str(number[0]) + str(number[7]) + str(number[0])
print("제 학번은 %s입니다." % studentid)

#number 리스트에서 인덱싱을 이용해 생일(8자리), 전화번호, 학번을
#만들고 각각 변수에 저장해준 후, print()문을 이용해 
#'제 생일은 20021230입니다'(생일은 본인 생일로, 나머지 출력 결과는 동일하게)
#'제 전화번호는 010-4916-2994입니다.'(본인 전화번호로, 나머지
# 출력 결과는 동일하게)'제 학번은 202212070입니다.'(본인 학번으로
# , 나머지 출력결과는 동일하게) 터미널에 출력되도록 해주세요