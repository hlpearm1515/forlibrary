from spell_checker import SimpleSpellChecker
import sys

def load_dictionary(filename):
    words = []
    try:
        # utf-8 인코딩으로 파일을 엽니다 (한글 깨짐 방지)
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # 줄바꿈 문자(\n)를 제거하고 리스트에 추가
                word = line.strip()
                if word: # 빈 줄은 제외
                    words.append(word)
        print(f"📂 '{filename}'에서 {len(words)}개의 단어를 로딩했습니다.")
        return words
    except FileNotFoundError:
        print(f"❌ 에러: '{filename}' 파일을 찾을 수 없습니다.")
        sys.exit()

def main():
    # 파일에서 단어 불러오기
    dictionary = load_dictionary("dictionary.txt")
    checker = SimpleSpellChecker(dictionary)
    
    print("=== 맞춤법 교정기 테스트 (종료하려면 'exit' 입력) ===")
    print(f"현재 사전 단어: {dictionary}")
    print("-" * 50)

    while True:
        # 사용자 입력 받기
        user_input = input("\n단어를 입력하세요: ").strip()

        if user_input.lower() == 'exit':
            print("테스트를 종료합니다.")
            break
            
        if not user_input:
            continue

        # 교정 수행
        result = checker.check_sentence(user_input)
        
        # 결과 출력
        if user_input == result:
            print(f"✅ 정확한 단어입니다: {result}")
        else:
            print(f"🔧 교정된 단어: {user_input} -> {result}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n강제 종료됨")
        sys.exit()