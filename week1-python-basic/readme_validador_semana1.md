# Validador de Datos de Prueba - Ejercicio Semana 1

## Contexto del Proyecto

Este script es mi primer ejercicio práctico de Python como parte de mi transición desde testing manual hacia automatización. Representa la aplicación directa de conceptos básicos de Python aprendidos durante la primera semana de estudio.

## Propósito del Ejercicio

Como QA tester con experiencia en testing manual, este ejercicio conecta mis conocimientos previos de validación de datos con los fundamentos de programación en Python. El objetivo es crear un validador que simule las validaciones que normalmente documentaría en casos de prueba manuales.

## Conceptos Aplicados (Semana 1)

- Variables y tipos de datos
- Input del usuario
- Operadores de comparación y lógicos
- Condicionales (if/else)
- Métodos de string (`.isdigit()`, `.isalpha()`, `.index()`)
- Operador `in` para búsqueda
- Conversión de tipos (string a int)
- Manejo de banderas booleanas
- Contadores básicos

## Funcionalidad Implementada

El script valida cuatro campos típicos de formularios:

**Username:**
- Mínimo 3 caracteres
- Solo letras (alfabético)

**Password:**
- Mínimo 6 caracteres
- Debe contener números

**Email:**
- Debe contener @ y punto
- @ debe estar antes del punto

**Edad:**
- Debe ser numérico
- Rango válido: 18-100

## Ejecución

```bash
python validador_datos.py
```

## Limitaciones Conocidas

Como ejercicio de primera semana, este script tiene limitaciones intencionales:

1. **Sin funciones:** El código no está modularizado porque las funciones se estudian en semana 2
2. **Validaciones básicas:** Las validaciones son simples y no cubren todos los casos edge
3. **Sin manejo de excepciones:** Error handling se verá en contenido futuro
4. **Lógica de contadores:** Implementación básica que se refactorizará con mejor comprensión

## Defectos Identificados

**Bug en validación de password:** 
La línea `if password.isdigit()` valida que la password sea SOLO números, cuando debería validar que CONTENGA números. Este es un error conceptual del uso del método `.isdigit()`.

**Solución pendiente:** Se corregirá en iteración futura usando loops o métodos más apropiados.

## Progresión del Aprendizaje

Este ejercicio será refactorizado en semanas posteriores para demostrar evolución:

- **Semana 2:** Modularización con funciones
- **Semana 3:** Lectura de datos desde archivo CSV
- **Semana 4:** Integración con framework pytest
- **Semana 8:** Validaciones para datos de testing automatizado

## Reflexión Técnica

Como profesional de QA, este ejercicio me permitió:
- Aplicar pensamiento de testing a código funcional
- Comprender la diferencia entre validar datos manualmente vs programáticamente
- Identificar casos edge que normalmente documentaría en test cases
- Experimentar la importancia de entender métodos antes de usarlos (`.isdigit()`)

El código no es perfecto ni profesional - es exactamente lo que debería ser: un primer ejercicio práctico que refleja honestamente mi nivel actual de Python mientras demuestra capacidad de aplicar conceptos aprendidos.

## Próximos Pasos

- Corregir validación de password
- Agregar más casos de validación
- Documentar código con comentarios más detallados
- Crear versión mejorada aplicando conceptos de semana 2

---

**Nota:** Este README es intencionalmente transparente sobre limitaciones y errores. Como QA tester en transición a automatización, considero que documentar el proceso de aprendizaje (incluyendo errores) es tan valioso como el código mismo.

**Fecha:** 30/09/2025
**Status:** Ejercicio completado - Pendiente refactoring
**Nivel:** Python Básico - Semana 1