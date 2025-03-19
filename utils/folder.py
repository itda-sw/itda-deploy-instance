import os
import shutil


def folder_init(path: str) -> bool:
    print("folder_init")
    if os.path.exists(path):
        user_input = (
            input(f"폴더 '{path}'가 이미 존재합니다. 삭제하고 새로 만들까요? (y/n): ")
            .strip()
            .lower()
        )
        if user_input == "y":
            shutil.rmtree(path)
            print(f"폴더 '{path}'가 삭제되었습니다.")
        else:
            print(f"폴더 '{path}'를 그대로 두고 작업을 종료합니다.")
            return False
    os.makedirs(path)
    print(f"폴더 '{path}'가 생성되었습니다.")
    return True
