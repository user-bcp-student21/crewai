"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'backend'
LABEL = 'Desarrollador backend'
SPEC_FILE = 'backend_spec.md'
EXTRACT_CODE = True

INSTRUCTIONS = """Implementa el backend de la funcionalidad usando el contrato de API aprobado por Arquitectura y, si existe, el contrato de Datos recibido como contexto previo.

Antes de proponer código, identifica los endpoints afectados, sus entradas, respuestas, estados HTTP y errores tal como están aprobados. Revisa el código existente y conserva convenciones y comportamiento compatible. No inventes rutas, campos, reglas de negocio, dependencias ni decisiones que falten: enumera los supuestos o bloqueos en backend_spec.md.

Valida en el servidor los campos obligatorios, formatos, límites y reglas de negocio definidos. Responde errores coherentes con el contrato, sin exponer secretos, credenciales, trazas ni detalles internos. Implementa servicios y acceso a datos con responsabilidades claras; define límites transaccionales y el comportamiento ante fallos según la operación.

En equipos de seis, define también el esquema y las migraciones estrictamente necesarias, con restricciones, conservación de datos y estrategia de reversión. Si el contrato de Datos está presente, síguelo y no vuelvas a diseñar tablas ni dupliques sus migraciones; señala incompatibilidades en vez de corregirlas unilateralmente.

Entrega backend_spec.md con el flujo, endpoints y contratos, validaciones, errores, persistencia/transacciones y decisiones pendientes. Incluye al menos un ejemplo válido y uno inválido con petición y respuesta esperada, más comandos reproducibles para comprobarlos. Propón comandos, pero nunca afirmes que se ejecutaron ni inventes resultados. Genera solo código Java necesario para cumplir el alcance aprobado, sin incluir frontend ni pruebas como si fueran implementación de producción."""
agent = Agent(role='Desarrollador backend', goal="Implementar los endpoints y servicios conforme a los contratos aprobados y las convenciones existentes, validando entradas y reglas de negocio, gestionando errores de forma segura y resolviendo persistencia y transacciones según el contrato de Datos, si existe, con evidencia verificable.",
              backstory="Eres responsable de traducir contratos aprobados de API y persistencia en una implementación Java consistente, validada y segura.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='''backend_spec.md con los endpoints y contratos aprobados, validaciones, errores, acceso a datos, transacciones, persistencia aplicable, un caso válido, un caso de error y comandos reproducibles. Después, código Java en bloques ```java```, un archivo por bloque: primera línea `// Nombre.java`, segunda línea `package pe.bcp.login.service;`. No incluyas resultados de ejecución no verificados.''', agent=agent)
