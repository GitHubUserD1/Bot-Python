palabras = {
    "CRINGE": "Se refiere a algo vergonzoso o incómodo.",
    "PRO": "Se utiliza para describir a alguien que es muy bueno en algo, experto o profesional.",
    "NOOB": "Persona novata o inexperta en un juego o actividad.",
    "LOL": "Abreviatura de 'Laughing Out Loud', se utiliza para expresar risa o diversión.",
    "TBT": "Abreviatura de 'Throwback Thursday', utilizado en redes sociales para compartir recuerdos del pasado los jueves.",
    "SHIPPEAR": "Apoyar o desear que dos personas ficticias o reales formen una relación romántica.",
    "SELFIE": "Fotografía tomada de uno mismo, generalmente con un teléfono inteligente.",
    "SQUAD": "Grupo de amigos cercanos.",
    "FOMO": "Abreviatura de 'Fear Of Missing Out', el temor de perderse algo interesante o divertido.",
    "SUS": "Abreviatura de 'Suspect' o sospechoso, utilizado para indicar desconfianza o incredulidad hacia algo o alguien.",
    "STAN": "Ser un gran admirador o seguidor de una persona, grupo, programa de televisión, etc.",
    "FLEX": "Presumir o alardear sobre algo, generalmente relacionado con logros personales o posesiones.",
    "BFF": "Abreviatura de 'Best Friends Forever', mejores amigos para siempre.",
    "GHOSTING": "Dejar de comunicarse repentinamente con alguien sin explicación.",
    "VIBES": "Se refiere a una atmósfera o energía particular que se siente en un lugar o situación."
}

while True:
    word = input("¿Hay alguna palabra que no entiendas? ¡Escribela aquí!: ").upper()
    if word in palabras.keys():
        print(palabras[word])
    else:
        print("Lamentablemente desconozco esta palabra y su significado, lo siento.")
        break
