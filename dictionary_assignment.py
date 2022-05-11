# 1. 파일 명은 dictionary_assignment.py 로 해주세요
# 2. 본인을 포함한 3명의 이름으로 각각 딕셔너리를 생성한 후,
# 각각 Key 값은 영문으로 이름, 나이, 생일, 성별, 전화번호
# 그리고 이에 맞는 Value 값을 가지도록 해주세요.
# 3. 이름, 나이, 생일, 성별, 전화번호에 해당하는 리스트를 생성해준 후,


# 각 리스트는 모두 숫자 1, 숫자2, 숫자3을 요소로 가지도록 해주세요.
# 4. 이름, 나이, 생일, 성별, 전화번호에 해당하는 리스트의 요소를
# Key 값을 통해 Value를 얻어 이를 리스트의 요소로 수정해주세요.
# 5. 각 이름, 나이, 생일, 성별, 전화번호에 해당하는 리스트를
# print()를 사용하여
# 이름 리스트는 [] ex) 이름 리스트는 [“youngbeen”, “minjeong”, “sujin”] 나이 리스트는 []
# 생일 리스트는 []
# 성별 리스트는 []
# 전화번호 리스트는 []
# 처럼 터미널창에 출력되도록 해주세요.
#dictionary생성
Dic1 = {"name" : "고유진", "age" : "21", "birthday" : "20021230", "sex": "여성", "phone" : "010-4916-2994"}
Dic2 = {"name" : "이나현", "age" : "20", "birthday" : "20030307", "sex": "여성", "phone" : "010-8910-1441"}
Dic3 = {"name" : "김신아", "age" : "23", "birthday" : "20000620", "sex": "여성", "phone" : "010-5576-6891"}
#이름 리스트
name = [1,2,3]
   #수정
name[0:3] = [Dic1["name"],Dic2["name"],Dic3["name"]]
   #출력
print("이름 리스트는 %s" %name)
#나이 리스트
age = [1,2,3]
   #수정
age[0:3] = [Dic1["age"], Dic2["age"], Dic3["age"]]
   #출력
print("나이 리스트는 %s" % age)
#생일 리스트
birthday = [1,2,3]
   #수정
birthday[0:3] = [Dic1["birthday"], Dic2["birthday"], Dic3["birthday"]]
   #출력
print("생일 리스트는 %s" % birthday)
#성별 리스트
sex = [1,2,3]
   #수정
sex[0:3] = [Dic1["sex"], Dic2["sex"], Dic3["sex"]]
   #출력
print("성별 리스트는 %s" % sex)
#전화번호 리스트
phone = [1,2,3]
   #수정
phone[0:3] = [Dic1["phone"], Dic2["phone"],Dic3["phone"]]
   #출력
print("전화번호 리스트는 %s" % phone)

