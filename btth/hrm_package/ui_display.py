from tabulate import tabulate

def display_records(attendance_book: list) -> None:
    if not attendance_book:
        print("Dữ liệu chấm công ngày hiện tại đang trống")
        return

    table_data = []
    for record in attendance_book:
        clock_in, clock_out = record["times"]
        display_clock_out = clock_out if clock_out is not None else "[Đang làm việc]"
        
        table_data.append([
            record["id"],
            record["name"],
            clock_in,
            display_clock_out
        ])

    headers = ["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"]
    
    print("--- BẢNG CHẤM CÔNG HÀNG NGÀY ---")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
