# PQRS con IA

## Resumen

Diseño de una experiencia de gestión de PQRS con apoyo de IA ante un gran volumen de solicitudes. La propuesta organiza prioridades y recomendaciones sin quitar a la persona la decisión sobre cada cambio.

## Rol y equipo

Mi contribución se centró en la experiencia de revisión de sugerencias, las acciones de cambio y el módulo de correo dinámico. La composición del equipo y las etapas de implementación no están documentadas.

## Contexto y problema

El volumen de solicitudes planteaba un reto de lectura, clasificación y asignación. Incorporar IA exigía una experiencia que permitiera revisar sus recomendaciones antes de aplicarlas, en lugar de presentar una clasificación automática como una decisión definitiva.

## Proceso

Definí la experiencia alrededor de las tareas descritas: priorizar, comprender la solicitud, revisar su clasificación y asignar responsabilidad. El diseño conectó las sugerencias con controles por campo y una acción conjunta. No se atribuyen al trabajo entrenamiento del modelo, pruebas de precisión o validación de impacto.

## Decisiones clave de diseño

- Mostrar un resumen para apoyar la lectura sin presentar la síntesis como sustituto de la solicitud original.
- Separar tipo de radicado, subtipo, dependencia y responsable para revisar decisiones específicas.
- Ofrecer Cambiar en cada campo para mantener el control humano.
- Incluir Aplicar todos los cambios sugeridos como acción explícita de la persona.
- Plantear transparencia y reversibilidad como criterios de diseño; su implementación requiere comprobarse.

## Solución

La IA organiza por prioridad, resume y recomienda clasificación y asignación. La interfaz permite cambiar cada campo o aplicar el conjunto de sugerencias. El módulo de envío incorpora correo dinámico y tokens inteligentes para componer mensajes. Los estados de confirmación y la persistencia de cambios requieren validación con la implementación.

## Resultados y aprendizajes

El entregable es una propuesta de gestión asistida que vincula recomendaciones con controles de revisión y composición de correo. No se dispone de mediciones de precisión, carga operativa o tiempo de respuesta. El aprendizaje es que una recomendación útil también debe ser comprensible y corregible.

[DATO PENDIENTE: PQ-01 | evidencia de reversión y evaluación de recomendaciones].

## Cierre

La IA sugiere y la persona decide. Ese principio guía la presentación de recomendaciones y las acciones disponibles, sin afirmar autonomía del sistema.
