from datetime import datetime

def evaluate_flex_time(attendance_book: list) -> None:
    print("--- BÁO CÁO ĐÁNH GIÁ VI PHẠM CA LÀM VIỆC ---")
    
    has_completed_record = False
    
    limit_time = datetime.strptime("10:00", "%H:%M")
    
    for record in attendance_book:
        clock_in_str, clock_out_str = record["times"]
        
        if clock_in_str and clock_out_str:
            has_completed_record = True
            
            in_time = datetime.strptime(clock_in_str, "%H:%M")
            out_time = datetime.strptime(clock_out_str, "%H:%M")
            
            if in_time > limit_time:
                print(f"Nhân viên {record['id']} ({record['name']}) - Vi phạm: Đến muộn quá 90 phút")
                continue
                
            work_duration = out_time - in_time
            total_seconds = work_duration.total_seconds()
            required_seconds = 9 * 3600 
            
            if total_seconds < required_seconds:
                print(f"Nhân viên {record['id']} ({record['name']}) - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ")
            else:
                print(f"Nhân viên {record['id']} ({record['name']}) - Hợp lệ: Hoàn thành ca làm việc")
                
    if not has_completed_record:
        print("Hệ thống chưa ghi nhận được nhân viên nào hoàn thành đủ cặp giờ Vào/Ra")
