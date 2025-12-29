class PromptController:
   
    def __init__(self):
        self.role = "General Assistant"
        self.system_instructions = {
            "General Assistant": "You are jerry, a sophisticated AI assistant. Be helpful, concise, and professional.",
            "Tutor": "You are jerry in tutor mode. Explain concepts clearly, provide examples, and help with learning.",
            "Coding Assistant": "You are jerry in coding mode. Help with programming, debug code, and provide best practices.",
            "Career Helper": "You are jerry in career counseling mode. Provide career advice, resume tips, and professional guidance."
        }
    
    def set_role(self, role):
  
        self.role = role
    
    def build_prompt(self, user_input, memory):
      
        system_instruction = self.system_instructions.get(
            self.role, 
            self.system_instructions["General Assistant"]
        )
        
        context = ""
        recent_memory = memory[-10:] if len(memory) > 10 else memory
        
        for msg in recent_memory:
            role = "User" if msg["role"] == "user" else "jerry"
            context += f"{role}: {msg['content']}\n"
        
        # Construct full prompt
        full_prompt = f"""System Instructions: {system_instruction}

Conversation History:
{context}

Current User Input: {user_input}

Please respond as jerry, considering the conversation context and your current role."""
        
        return full_prompt