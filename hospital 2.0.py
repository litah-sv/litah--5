lista = ["\ndor", "\ndificuldade para respirar", "\nfebre", "\nnauseas", "\nfadiga extrema"]

nome=str(input("nome do paciente:"))
(input("rg:"))
(input("idade do paciente:"))


for sintoma in lista:
    print(sintoma)

atual = str(input("\nQual sintoma está sentindo: "))

if atual=="dor":
    print("Amarelo — Urgente o paciente pode esperar até 60 minutos para o atendimento")

elif atual=="dificuldade para respirar":
    print("Vermelho — Emergência o paciente requer o atendimento imediato")
    
elif atual=="febre":
    print("Laranja — Muito urgente o paciente precisa do atendimento nos próximos 10 minutos")
    
elif atual=="nauseas":
    print("Verde — Pouco urgente o paciente pode esperar ate 120 minutos para o atendimento")
    
elif atual=="fadiga extrema":
    print("Azul — Não urgente o paciente pode esperar mais de 120 minutos para o atendimento")
    
continuar = input ("\nDeseja continuar com o atendimento? (s/n): ").strip().lower()
if continuar != 's':
    print("Atendimento encerrado.")
    