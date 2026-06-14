def clock_in(attendance_book: list) -> None:
    print("--- TIẾN TRÌNH CHẤM CÔNG VÀO (CLOCK-IN) ---")
    employee_id = input("Nhập mã nhân viên: ").strip().upper()
    
    if not employee_id:
        print("Lỗi: Mã nhân viên không được để trống")
        return

    for record in attendance_book:
        if record["id"] == employee_id:
            print(f"Lỗi: Mã nhân viên {employee_id} đã tồn tại trên hệ thống")
            return

    name = input("Nhập tên nhân viên: ").strip()
    if not name:
        print("Lỗi: Tên nhân viên không được để trống")
        return

    clock_in_time = input("Nhập giờ vào (HH:MM): ").strip()
    if len(clock_in_time) != 5 or ":" not in clock_in_time:
        print("Lỗi: Sai cấu trúc định dạng giờ ")
        return

    new_record = {
        "id": employee_id,
        "name": name,
        "times": (clock_in_time, None)
    }
    attendance_book.append(new_record)
    print(f"Thành công: Đã ghi nhận {employee_id} chấm công vào lúc {clock_in_time}")


def clock_out(attendance_book: list) -> None:
    print("--- TIẾN TRÌNH CHẤM CÔNG RA ---")
    employee_id = input("Nhập mã nhân viên cần chấm công ra: ").strip().upper()

    target_record = None
    for record in attendance_book:
        if record["id"] == employee_id:
            target_record = record
            break

    if not target_record:
        print(f"Lỗi: Không tìm thấy hồ sơ của nhân viên mang mã {employee_id}")
        return

    clock_out_time = input("Nhập giờ ra (HH:MM): ").strip()
    if len(clock_out_time) != 5 or ":" not in clock_out_time:
        print("Lỗi: Sai cấu trúc định dạng giờ giấc (Ví dụ chuẩn: 17:30)")
        return

    old_clock_in = target_record["times"][0]

    target_record["times"] = (old_clock_in, clock_out_time)
    print(f"Thành công: Đã ghi nhận {employee_id} chấm công ra lúc {clock_out_time}")
