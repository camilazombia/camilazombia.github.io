# Agendamiento de citas

## Resumen

Diseño de una plataforma de agendamiento para Hacienda. La propuesta reúne la solicitud de citas y la gestión operativa de agendas, con responsabilidades diferenciadas para administrador, coordinador y agente.

## Rol y equipo

Trabajé en los flujos, las interfaces y las definiciones de comportamiento del sistema. El alcance incluyó reglas de agendamiento y permisos por perfil. No se cuenta con el detalle completo del equipo.

## Contexto y problema

El proceso estaba fragmentado: se enviaba un Excel al proveedor para habilitar la agenda, el formulario de solicitud presentaba problemas de experiencia de uso y el calendario en Teams no mostraba suficiente detalle. Esta separación dificultaba entender el proceso completo desde la configuración hasta la atención.

## Proceso

Partí de los flujos existentes descritos y definí la estructura de una plataforma con gestión por perfiles y un formulario de solicitud. El trabajo de diseño precisó reglas, límites y comportamiento de las agendas dinámicas. No se afirman pruebas con usuarios, despliegue o resultados operativos que no estén documentados.

## Decisiones clave de diseño

- Separar administrador, coordinador y agente para hacer explícita la responsabilidad de cada perfil.
- Concentrar el control general, incluido el correo, en el administrador para definir la configuración del servicio.
- Dar al coordinador una vista de su sede para situar la gestión en su contexto operativo.
- Diseñar agendas dinámicas en las que agregar un bloque ajuste los demás para contemplar el comportamiento conjunto del horario.
- Definir límites de solicitudes como reglas del sistema para evitar decisiones implícitas en el formulario.

## Solución

La propuesta incluye un formulario de solicitud de citas, un perfil administrador con control total y configuración de correo y reglas, y un dashboard del coordinador para su sede con creación de agendas dinámicas. El perfil agente forma parte del modelo de roles; sus permisos detallados requieren confirmación.

## Resultados y aprendizajes

Antes, la operación dependía de archivos enviados al proveedor, un formulario y un calendario separado. El diseño reúne estas necesidades en una propuesta de plataforma, con roles y comportamiento de agenda definidos. Esto describe un entregable de diseño, no una implementación confirmada ni una reducción de tiempos medida. El aprendizaje es tratar reglas y permisos como parte central de la experiencia.

[DATO PENDIENTE: HC-01 | validación de permisos del agente y estado de implementación].

## Cierre

El caso muestra cómo hacer visible la lógica de un servicio para quienes lo administran y para quienes solicitan una cita. Los ejemplos visuales serán ficticios.
