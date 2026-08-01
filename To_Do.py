import csv
import os

class Task:
    
    PRIORITIES = ("پایین", " متوسط", " بالا")
    
    def __init__(self, name: str, description: str = "", priority: str = "متوسط"):
        self.name = name.strip()
        self.description = description.strip()
        priority = priority.strip()
        self.priority = priority if priority in self.priorities else "متوسط"
        
    
    def to_dict(self) -> dict:
        """ مناسب برای  نوشتن در فایل تبدیل شی Task به دیکشنرس csv"""
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority,        
        }    
    
    @staticmethod
    def from_dict(data:dict) -> "Task":
        """" ساخت یک شی Task از روی یک دیکشنری"""
        
        return Task(
            name= data.get("name", " "),
            description= data.get("description", " "),
            priority= data.get("priority"," متوسط"),
        )
    
    def __str__(self) ->str:
        desc = self.description if self.description else "بدون توضیحات"
        return f"نام: {self.name} | اولویت: {self.priority} | توضیحات: {desc}"
    

class ToDoList:
    """"  کلاس ToDoListبرای مدیریت لیست کارها
   شامل امکانات افزودن وحزف و نمایش و ذخیره و بارگزاری کارها از فایل csv است 
   """
    FIELDNAMES = ["name", "description", "priority"]
    
    def __init__(self, filename: str= "task.csv"):
        self.filename = filename 
        self.task: list[Task] = []
        self.load_from_csv()    # در صورت وجود فایل لیست به صورت خودکار بارگذاری میشود
    
    def add_task(self, name: str, description: str = " ", priority: str = "متوسط") -> None:
        """ اضافه کردن یک کار جدید به لیست و ذخیره خودکار در فایل csv."""
        if not name.strip():
            print("نام کار نمیتوان خالی باشد.")
            return
        task = Task(name, description, priority)
        self.tasks.append(task)
        self.save_to_csv()
        print(f'کار"{task.name}"باموفقیت اضافه شد')
        
    def remove_task(self, name: str) -> None:
        """ حذف یک کاربر بر اساس نام از لیست و ذخیرع خودکار تغییرات  """
        for task in self.tasks:
            if task.name == name.strip():
                self.tasks.remove(task)
                self.save_to_csv()
                print(f'کار"{name}" با موفقیت حذف شد.')
                return
        print(f'کاری با نام "{name}" پیدا نشد.')
        
    def show_task(self) -> None:
        """" نمایش تمامی کارهای موجود در لیست"""
        if not self.taks:
            print("لیست کارها خالی است")
            return
        
        print("\n--- لیست کارها ---")
        for index, task in enumerate(self.task, satrt=1):
            print(f"{index}.{task}")
        print("------------------\n")
        
    def save_to_csv(self) -> None:
        """" ذخیره تمام کارهای لیست در فایل csv."""
        with open(self.filename, mode='w', newline= " ", encoding="uft-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())
                
    def load_from_csv(self) -> None:
        """"  بارگذاری کار ها از فایلcsv در صورت وجود فایل."""
        if not os.path.exists(self.filename):
            return
        with open(self.filename, mode="r", newline=" ", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            self.tasks = [Task.from_dict(row) for row in reader if row.get("name")]
            
def get_priority_input() -> str:
    """" گرفتن ورودی اولویت از کاربر با اعتبار سنجی."""
    print("اولویت را انتخای کنید: ")
    print("1. بالا")
    print("2. متوسط")
    print("3. پایین")
    choice = input("شماره اولولت(پیش فرض متوسط): " ).strip()
    mapping = {"1": "بالا" ,  "2": "متوسط" , "3": "پایین"}
    return mapping.get(choice, "متوسط")
        
def show_menu() -> None:
    print("\n==== منو مدیریت لیست کارها ====")
    print("1. اضافه کردن کار جدید ")
    print("2. حذف کار")
    print("3. مشاهده ی تمامی کارها ")
    print("4. خروج از برنامه")
    print("=========================================")
    
def main() -> None:
    todo_list = ToDoList("tasks.csv")
        
    while True:
        show_menu()
        choice = input(" گزینه ی مورد نظر را انتخاب کنید: ").strip()
            
        if choice == "1":
            name = input("نام کار: ").strip()
            desciption = input(" توضیحات (اختیاری): ").strip()
            priority = get_priority_input()
            todo_list.add_task(name, desciption, priority)
                
        elif choice == "2":
            todo_list.show_task()
            name = input("نام کاری که میخواهید حذف شود : ").strip()
            todo_list.remove_task(name)
                
        elif choice == "3":
            todo_list.show_task()
            
        elif choice == "4":
            print("لیست کارها ذخیره شد.خروج از برنامه.موفق باشید!")
            break
            
        else:
            print("گزینه نامعتبر است.لطفا عددی بین 1 تا 4 وارد کنید ") 
            
        
if __name__ == "__main__":
    main()
    