from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 하루 소비 평가 이모지")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        elif choice == "5":
            try:
                score = int(input("하루 소비 평가 점수를 입력하세요(0-100점): "))
                if 0 <= score <= 35:
                    print("😡 (소비 조심!)")
                elif 36 <= score <= 60:
                    print("😊 (괜찮아요~)")
                elif 61 <= score <= 100:
                    print("🎉 (훌륭해요!)")
                else:
                    print("점수는 0~100 사이로 입력해주세요.\n")
            except ValueError:
                print("숫자를 입력해주세요.\n")


        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
