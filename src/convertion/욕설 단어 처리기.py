#욕설->우리말 치환 딕셔너리
curse_mapping = {
    "찐따": "아웃사이더",
    "염병": "장티푸스",
    "존나": "엄청",
    "ㅈㄴ": "엄청",
    "시발": "빌어먹을",
    "ㅅㅂ": "빌어먹을",
    "씨발": "빌어먹을",
    "병신": "어리석은 사람",
    "ㅂㅅ": "어리석은 사람",
    "븅신": "어리석은 사람",
    "개새끼":"못된 아이",
    "개자식":"못된 아이",
    "ㄱㅅㄲ":"못된 아이",
}
def clean_text(text, mode="replace"):
    # mode = "replace" | "star"
    for swear, replacement in curse_mapping.items():
        if mode == "replace":
            text = text.replace(swear, replacement)
        elif mode == "star":
            text = text.replace(swear, "*" * len(swear))
    return text


while True:
    mode=input("변환 방법을 선택하세요(replace/star): ")
    if mode not in ["replace","star"]:
        print("잘못된 입력입니다. 다시 시도해주세요.")
        continue
    elif mode=="replace":
        users_input=input("문장을 입력하세요: ")
        switched_text=clean_text(users_input, mode='replace')
        print(switched_text)
    elif mode=="star":
        users_input=input("문장을 입력하세요: ")
        switched_text=clean_text(users_input, mode='star')
        print(switched_text)
        

   

   