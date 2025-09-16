import pandas as pd
import sys
import os

def read_excel_rows(file_name, start_row, end_row):
    try:
        print(f"파일 경로: {os.path.abspath(file_name)}")
        print(f"파일 존재 여부: {os.path.exists(file_name)}")
        
        df = pd.read_excel(file_name, header=None, engine='openpyxl')
        print(f"=== {file_name} 읽기 성공 ===")
        print(f"전체 행 수: {len(df)}, 전체 열 수: {len(df.columns)}")
        print()
        
        for i in range(start_row-1, min(end_row, len(df))):  # 1-based to 0-based
            row_data = df.iloc[i].fillna('').astype(str).tolist()
            print(f"행 {i+1}: {row_data}")
            print()
            
    except Exception as e:
        print(f"❌ 오류: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    read_excel_rows('기능정의서_test_250916.xlsx', 3, 6)
