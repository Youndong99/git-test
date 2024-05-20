

# 딕셔너리 만들기
dic={}
dic=dict()

# 딕셔너리 특징
dic={'kor':80,'eng':90,'mat':77}
dic['kor']
dic['kor']=85
dic['scl']=92

# 딕셔너리 활용
del dic['met']  # 삭제하기
dic.clear()     # 전체 삭제
'eng'in dic     # 확인하기 (키 기준)
len(dic)        # 전체 개수

dic.keys()      # 모든 키 얻기
dic.values()    # 모든 값 얻기
dic.items()     # 모든 순서쌍 얻기

tuple(dic)
list(dic)
set(dic)

li=['ab','cd','ef']
dict(li)

li=[['a',1],['b',2],['c',3]]
dict(li)
