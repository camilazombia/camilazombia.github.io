# Video Interview

## Resumen

Funcionalidad de entrevistas en video solicitada por clientes de Remote Latinos. El candidato responde preguntas según su rol, paso a paso, y la experiencia contempla la transcripción de la entrevista.

## Rol y equipo

Trabajé en el diseño del flujo guiado y en la definición de estados y casos límite de la grabación. Los clientes aportaron la necesidad funcional; no está documentada la composición completa del equipo.

## Contexto y problema

La necesidad era incorporar respuestas en video a preguntas relacionadas con el rol del candidato. El reto de experiencia consistía en acompañar una actividad secuencial que depende de la grabación y que debe contemplar errores y reintentos.

## Proceso

Organicé la secuencia de preguntas y la interacción de respuesta en video. El diseño consideró los estados grabando, error y reintento, junto con casos límite del recorrido. No se dispone de un protocolo de pruebas con candidatos ni de resultados de validación para atribuirlos al caso.

## Decisiones clave de diseño

- Presentar las preguntas paso a paso para dar foco a la respuesta actual.
- Relacionar las preguntas con el rol para mantener el contexto de la entrevista.
- Diferenciar grabación, error y reintento para comunicar el estado de la tarea.
- Incluir la transcripción como parte de la funcionalidad solicitada para acompañar la revisión del video.

## Solución

La propuesta combina preguntas por rol, respuesta secuencial en video y transcripción. Los estados de grabación y recuperación forman parte del relato de diseño. Las reglas exactas de duración, permisos de cámara, interrupciones y guardado deben confirmarse con las especificaciones del producto; no se inventan aquí.

## Resultados y aprendizajes

El resultado documentado es el diseño de una funcionalidad de entrevista con recorrido guiado y estados de grabación. No hay datos de finalización, errores o uso posterior. El aprendizaje es que diseñar una grabación implica definir también cómo se entiende y recupera un intento fallido.

[DATO PENDIENTE: VI-01 | matriz aprobada de estados, recuperación y límites de grabación].

## Cierre

El foco del caso está en acompañar una tarea exigente con pasos y estados comprensibles, sin atribuir mejoras de contratación no medidas.
