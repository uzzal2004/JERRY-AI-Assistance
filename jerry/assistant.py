class jerryAssistant:    ##Main jerry Assistant class
 
    def __init__(self, engine, prompt_controller, memory):
        self.engine = engine
        self.prompt_controller = prompt_controller
        self.memory = memory
        self._greet_user()
    
    def _greet_user(self):
        
        greeting = "Hello! I'm jerry, your personal AI assistant. How may I assist you today?"
        self.memory.add("assistant", greeting)
    
    def respond(self, user_input):
     
        try:
       
            self.memory.add("user", user_input)
         
            history = self.memory.get_history()
            
            prompt = self.prompt_controller.build_prompt(user_input, history)
           
            response = self.engine.generate(prompt)
         
            self.memory.add("assistant", response)
            
            return response
            
        except Exception as e:
            error_response = f"I apologize, but I encountered an error: {str(e)}"
            self.memory.add("assistant", error_response)
            return error_response