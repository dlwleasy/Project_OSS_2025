from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 하루 소비 다이어리 추가")
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
            import datetime
            today = datetime.date.today().isoformat()
            print("다이어리에 작성할 내용을 입력하세요 (입력 후 Enter):")
            content = input("> ")

            try:
                with open("diary.txt", "a", encoding="utf-8") as f:
                    f.write(f"[{today}] {content}\n")
                print(" 다이어리에 저장되었습니다.\n")
            except Exception as e:
                print(f" 저장 중 오류 발생: {e}\n")

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
