import os

class SavedFile:
    def __init__(self, filename):
        self.filename = filename
    
    def check_save(self):
        if os.path.exists(self.filename):
            print("the file has been saved succesfully.")
        else:
            print("The file may have not been saved.")

# Crear una instancia de la clase ArchivoGuardado
File = SavedFile(r'My_model\My_model_regression')

# Verificar si el archivo se ha guardado correctamente
File.check_save()