import FinanceDataReader as fdr

# rank 매기기
""" df["aver"] = df.postcode.rank(method="average")
print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(method="max")
print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "average"]]) """

# 전치 칼럼, 로우 변환
# print(df.transpose())


# 누적계산
# print(df["postcode"].expanding().sum())
# print(df["postcode"].expanding())

# 내림차수 기준
# print(df.postcode.idxmax(axis=0))
# print(df.postcode.idxmin(axis=0))

# empty 추가
""" print(df.empty)
print(df.aver.empty) """

# 검색
""" print(df.isin[xxx])
print(df.isin[xxxx, xxxxx])
print(df.isin[xxxx, xxxxx, "xxxxx"]) """

# 기간계산
""" period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf) """

# 인덱스 시간 - 간격 생성
""" i = pd.date_range("2023-11-10", periods=10, freq="1H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df) 

print("\n----------------------\n") """

#특정 시간 찾기
# print(df.at_time("09:00"))

#범위 찾기
""" print(df.between_time(start_time="12:00", end_time="00:00"))
print(df.between_time(start_time="03:00", end_time="09:00"))"""

# x일 간격 생성 - 기간별 찾기
# i = pd.date_range("2023-11-10", periods=10, freq="3D")
""" i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print(df.first("3D"))
print(df.first("7D"))
print(df.last("7D")) """

# 코스피지수
""" import FinanceDataReader as fdr 

ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n----------------/n") """

# 최고가 확인
""" res = ksp["High"].max()
print(res)

res = ksp["High"].idxmax()
print(res) """

# 최저가
""" res = ksp["Low"].min()
print(res)

res = ksp["Low"].idxmin()
print(res) """ 

# 3000 최초일
""" cond = ksp["Close"] >= 3000
cond = ksp["Close"] >= 2000
res = ksp[cond].index[0]
print(res) """

# res = ksp["Volume"] > ksp["Volume"].shift()
# print(res)

# 위 값 참조 처리
# ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
# print(ksp)

ksp["up"] != ksp["up"].shift().cumsum()

# ksp["grp"] = (ksp["up"] != ksp["up"].shift().cumsum())
# print(ksp)

# 연속 증가값 확인
""" ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)

print(ksp["up_cnt"].max()) """

# 변환
""" import pandas as pd
target = "./data/apt.csv"

df = pd.read_csv(target, encoding="cp949")

df.to_csy("./data/apt.csv", encoding="utf8")

print(df.head()) """


""" import pandas as pd

df = pd.read_csv("./data/apt.csv", index_col=0)

print(df.head())

df.rename(columns={"분양가격(제곱미터)":"분양가"})
print(df)
print(df.dftypes)

df = df["분양가"].convert_dtypes()
print(df.dtypes) """

# array 변환
""" arr = df.to_numpy()
print(arr)
print(arr[2])
print(len(arr)) """


# print(df.describe)

print(df.transpose())
print("\n----------------\n")
print(df.T.head())