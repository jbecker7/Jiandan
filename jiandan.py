import pickle


class Class:
    def __init__(self, name):
        self.name = name
        self.assignments = {}
    
    def add_assignment(self, name, due_date):
        self.assignments[name] = {"due_date": due_date, "completed": False}
        
    def mark_complete(self, name):
        if name in self.assignments:
            self.assignments[name]["completed"] = True
        else:
            print(f"{name} not found.")
            
    def delete_assignment(self, name):
        if name in self.assignments:
            del self.assignments[name]
        else:
            print(f"{name} not found.")
            
    def view_assignments(self):
        for name, details in self.assignments.items():
            print(f"{name} - Due: {details['due_date']} - Completed: {'Yes' if details['completed'] else 'No'}")


class TaskManager:
    def __init__(self):
        self.classes = {}
        
    def add_class(self, name):
        self.classes[name] = Class(name)
        
    def add_assignment(self, class_name, name, due_date):
        if class_name in self.classes:
            self.classes[class_name].add_assignment(name, due_date)
        else:
            print(f"{class_name} not found.")
            
    def mark_complete(self, class_name, name):
        if class_name in self.classes:
            self.classes[class_name].mark_complete(name)
        else:
            print(f"{class_name} not found.")
            
    def delete_assignment(self, class_name, name):
        if class_name in self.classes:
            self.classes[class_name].delete_assignment(name)
        else:
            print(f"{class_name} not found.")
            
    def view_assignments(self, class_name):
        if class_name in self.classes:
            self.classes[class_name].view_assignments()
        else:
            print(f"{class_name} not found.")
    def view_all_assignments(self):
        for class_name, class_object in self.classes.items():
            print(f'Assignments for {class_name} :')
            class_object.view_assignments()
    
    def save_data(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.classes, file)
            
    def load_data(self, file_name):
        with open(file_name, 'rb') as file:
            self.classes = pickle.load(file)


            
