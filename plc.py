
"""
O que é a planta nesse caso? 
A planta representa o mundo físico, o painel de comando por exemplo. 
Ou seja, ela não possui memória nenhuma do CLP, apenas estados físicos, que podem ser manipulados através de botões ou algo do tipo.
Todos iniciam False. 
"""
class Plant:
    def __init__(self):
        self.start_button: False
        self.end_button: False 
        self.motor = False
        
"""
Aqui a classe representa o controlador, ele possui como atributos as imagens de input e de output.
Ou seja, físicamente, seriam os módulos de entrada e saída do CLP, podendo ser digitais ou analógicos.  
"""           
class PLC: 
    def __init__(self):
        # Por que usam-se dicionários para isso?
        # Caso preenchido ficariam preenchidos de acordo com o sensores e atuadores da planta, as classes se relacionam 
        self.input_image = {} 
        self.output_image = {} 
    
    def read_inputs(self,plant): 
        self.input_image["START"] = plant.start_button 
        self.input_image["END"] = plant.end_button
        self.output_image["MOTOR"] = plant.motor

    def take_input_image(self,input_image): 
        

class InputImage: 
    def __init__(self):
        
    
class OutputImage: 
    def __init__(self):
        