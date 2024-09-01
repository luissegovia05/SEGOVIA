class Persona:
    def __init__(self, nombre: str, apellido: str, direccion: str, telefono: str, edad: int, email: str):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad
        self.email = email

   
    def get_nombre(self) -> str:
        return self.nombre

    def get_apellido(self) -> str:
        return self.apellido

    def get_direccion(self) -> str:
        return self.direccion

    def get_telefono(self) -> str:
        return self.telefono

    def get_edad(self) -> int:
        return self.edad

    def get_email(self) -> str:
        return self.email

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_apellido(self, apellido: str):
        self.apellido = apellido

    def set_direccion(self, direccion: str):
        self.direccion = direccion

    def set_telefono(self, telefono: str):
        self.telefono = telefono

    def set_edad(self, edad: int):
        self.edad = edad

    def set_email(self, email: str):
        self.email = email


class Empleado(Persona):
    def __init__(self, nombre: str, apellido: str, direccion: str, telefono: str, edad: int, email: str, 
                 salario: float, jefe_inmediato: str, anos_experiencia: int):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self.salario = salario
        self.jefe_inmediato = jefe_inmediato
        self.anos_experiencia = anos_experiencia
        self.nombre_cargo = self.calcular_cargo()

    def get_salario(self) -> float:
        return self.salario

    def get_jefe_inmediato(self) -> str:
        return self.jefe_inmediato

    def get_anos_experiencia(self) -> int:
        return self.anos_experiencia

    def get_nombre_cargo(self) -> str:
        return self.nombre_cargo

    def set_salario(self, salario: float):
        self.salario = salario
        self.nombre_cargo = self.calcular_cargo()  

    def set_jefe_inmediato(self, jefe_inmediato: str):
        self.jefe_inmediato = jefe_inmediato

    def set_anos_experiencia(self, anos_experiencia: int):
        self.anos_experiencia = anos_experiencia
        self.nombre_cargo = self.calcular_cargo()   

    def set_nombre_cargo(self, nombre_cargo: str):
        self.nombre_cargo = nombre_cargo

    def calcular_cargo(self) -> str:
        if self.anos_experiencia < 3:
            return 'Junior'
        elif 3 <= self.anos_experiencia < 6:
            return 'Semi-Senior'
        else:
            return 'Senior'


def main():
    print("Ingrese los datos personales del empleado:")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    edad = int(input("Edad: "))
    email = input("Email: ")
    
    salario = float(input("Salario: "))
    jefe_inmediato = input("Jefe Inmediato: ")
    anos_experiencia = int(input("Años de Experiencia: "))
    
    empleado = Empleado(nombre, apellido, direccion, telefono, edad, email, salario, jefe_inmediato, anos_experiencia)
    
    print("\nDetalle del Empleado:")
    print(f"Nombre: {empleado.get_nombre()} {empleado.get_apellido()}")
    print(f"Dirección: {empleado.get_direccion()}")
    print(f"Teléfono: {empleado.get_telefono()}")
    print(f"Edad: {empleado.get_edad()}")
    print(f"Email: {empleado.get_email()}")
    print(f"Salario: {empleado.get_salario()}")
    print(f"Jefe Inmediato: {empleado.get_jefe_inmediato()}")
    print(f"Años de Experiencia: {empleado.get_anos_experiencia()}")
    print(f"Cargo: {empleado.get_nombre_cargo()}")


if __name__ == "__main__":
    main()