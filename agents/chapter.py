"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'chapter'
LABEL = 'Chapter'
SPEC_FILE = 'chapter_review.md'
EXTRACT_CODE = False

INSTRUCTIONS = " Contrasta cada criterio de aceptación con arquitectura, " \
"persistencia, implementación, pruebas y seguridad. Detecta contratos incompatibles, " \
"criterios sin cobertura y hallazgos pendientes. Para cada observación indica " \
"responsable, cambio requerido y cómo verificarlo. Justifica el veredicto con " \
"evidencia y señala las pruebas pendientes. Conserva las aprobaciones humanas; tu " \
"informe no las sustituye. Entrega chapter_review.md con VEREDICTO: APROBADO o " \
"RECHAZADO, motivos y correcciones. Conserva las aprobaciones humanas."
agent = Agent(role='Chapter Lead Backend JAva', goal="Completar la tarea asignada asegurando que todos " \
"las fases se hayan completado y ademas que todos los roles hayan cumplido con sus responsabilidades.",
              backstory="Soy Chapter Lead Backend JAva con 30 años de experiencia en revisión de capítulos.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='Un informe con VEREDICTO: APROBADO o RECHAZADO.', agent=agent)
