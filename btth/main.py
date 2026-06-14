from hrm_package.ui_display import display_records as view_board
from hrm_package.attendance_logic import clock_in as check_in, clock_out as check_out
from hrm_package.time_calc import evaluate_flex_time as analyze_violations

def run_attendance_system():
    attendance_book = [
        {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
        {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)},
        {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
    ]

    while True:
        print("=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===")
        print("1. Xem bảng chấm công ngày")
        print("2. Chấm công Vào (Clock-in)")
        print("3. Chấm công Ra (Clock-out)")
        print("4. Đánh giá vi phạm")
        print("5. Thoát chương trình")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            view_board(attendance_book)
        elif choice == "2":
            check_in(attendance_book)
        elif choice == "3":
            check_out(attendance_book)
        elif choice == "4":
            analyze_violations(attendance_book)
        elif choice == "5":
            print("Hệ thống đóng an toàn. Chào tạm biệt")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5")

if __name__ == "__main__":
    run_attendance_system()
