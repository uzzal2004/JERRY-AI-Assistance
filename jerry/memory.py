import json
import os

class Memory:
 
    def __init__(self, file_path="conversation_memory.json"):
        self.file_path = file_path
        self._initialize_memory()
    
    def _initialize_memory(self):
       
        if not os.path.exists(self.file_path):
            self._save_memory([])
    
    def add(self, role, message): ## Add a message to memory
      
        history = self.get_history()
        history.append({
            "role": role,
            "content": message
        })
        self._save_memory(history)
    
    def get_history(self):
       
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def clear(self):
 
        self._save_memory([])
    
    def _save_memory(self, history):
       
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)