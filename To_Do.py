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