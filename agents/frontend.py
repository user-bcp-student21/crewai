"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'frontend'
LABEL = 'Desarrollador frontend'
SPEC_FILE = 'frontend_spec.md'
EXTRACT_CODE = True

INSTRUCTIONS = (
    "Responsabilidad exclusiva de Frontend: implementa en Angular la interfaz "
    "y el recorrido de usuario descritos por la Feature, usando el contrato de "
    "API aprobado sin inventar endpoints, campos ni respuestas. En frontend_spec.md "
    "enumera pantallas, campos, acciones, validaciones visibles y mensajes, y "
    "vincúlalos con los criterios de aceptación. Implementa solo los componentes, "
    "plantillas, estilos y servicios Angular necesarios para consumir la API. "
    "Representa los estados de carga, vacío, éxito y error; bloquea envíos "
    "duplicados mientras una petición está en curso. Asegura etiquetas "
    "asociadas a sus campos, navegación por teclado y foco visible. Describe "
    "pasos concretos para comprobar el recorrido y sus errores, sin afirmar "
    "que se ejecutaron pruebas si no hay resultados reales. No implementes ni "
    "cambies endpoints, lógica de servidor, autorización, modelo de datos, "
    "persistencia o migraciones; si falta un contrato o una decisión de otro "
    "rol, indícalo como pendiente en vez de asumirlo."
)
agent = Agent(role='Desarrollador frontend',
              goal="Implementar el recorrido Angular según el contrato de API aprobado.",
              backstory=(
                  "Eres desarrollador frontend especializado en Angular. Transformas "
                  "recorridos de usuario y contratos de API aprobados en pantallas, "
                  "componentes y servicios cliente accesibles; manejas respuestas y "
                  "estados de interfaz sin modificar el backend ni la persistencia."
              ),
              llm=llm, verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output=(
                    'frontend_spec.md con el recorrido de usuario según el contrato de API, '
                    'campos, validaciones, acciones, mensajes, estados de carga, vacío, éxito y '
                    'error, prevención de envíos duplicados, accesibilidad por teclado y pasos '
                    'para comprobar el recorrido y sus errores. Incluye código Angular en bloques '
                    'markdown, uno por archivo, con la primera línea // nombre.component.ts, '
                    '// nombre.component.html, // nombre.component.css o // nombre.service.ts.'
                ), agent=agent)
