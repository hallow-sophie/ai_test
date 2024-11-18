import pandas as pd
import numpy as np

# 설정: 데이터 개수
n = 3000

# 첫 번째 컬럼: 1~151 사이의 랜덤한 숫자 생성
number = np.random.randint(1, 152, size=n)  # 1~151 사이의 랜덤 정수 생성

# 서울 중심으로 밀집된 분포를 만들기 위한 평균과 표준편차 설정
latitude_center = 37.5665  # 서울의 위도
longitude_center = 126.978  # 서울의 경도
latitude_std = 0.5  # 위도의 표준편차 (서울 근처로 밀집)
longitude_std = 0.5  # 경도의 표준편차 (서울 근처로 밀집)

# 서울을 중심으로 위도와 경도 값 생성 (가우시안 분포)
latitude = np.random.normal(latitude_center, latitude_std, n)
longitude = np.random.normal(longitude_center, longitude_std, n)

# 네 번째 컬럼: 2010~2020 사이의 랜덤한 연도 값
# year = np.random.randint(2010, 2021, size=n)  # 2010~2020 사이의 랜덤 정수 생성
year = np.linspace(2010, 2020, n).astype(int)  # 정수형으로 변환

# DataFrame 생성
data = pd.DataFrame({
    'num': number,
    'latitude': latitude,
    'longitude': longitude,
    'year': year
})

# CSV 파일로 저장
# data.to_csv('generated_data_with_year.csv', index=False, encoding='utf-8')

attributes_data = pd.read_csv('pokemon_attribute.csv', encoding='utf-8')

# 두 데이터프레임을 '번호' 컬럼을 기준으로 병합
merged_data = pd.merge(data, attributes_data, on='num', how='left')

# 병합된 데이터 확인
print(merged_data.head())

# 병합된 데이터 CSV 파일로 저장
merged_data.to_csv('pocket_monsters.csv', index=False, encoding='utf-8')


# 결과 확인
print(data.head())
