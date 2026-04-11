# 📚 Plan de Migración LetyMath → HTML con LaTeX

**Estado:** Estructuración inicial
**Última actualización:** 2026-04-08
**Objetivo:** Migrar letymath.com (Google Sites) a lety2e.com con estructura HTML/CSS/JS vanilla

---

## 🎯 Enfoque (Híbrido)

✅ **Template base** → generado automáticamente
✅ **Contenido personalizado** por curso
✅ **Videos YouTube** incrustados
✅ **Matemáticas en LaTeX** (no imágenes JPG)

---

## 📋 Mapeo de Tópicos × Cursos

### Matemáticas 1 (Fundamentals)
- ✅ operaciones-básicas (2 videos)
- ✅ jerarquía (1 video)
- ✅ ecuaciones (1 video)
- ✅ monomios (1 video)
- ✅ expresiones-algebraicas (0 videos - revisar)
- ✅ gráfica-con-tabulación (2 videos)
- ✅ pendiente-ordenada (0 videos - revisar)
- ✅ área-perímetro (0 videos - revisar)
- ✅ ecuaciones-con-ángulos (0 videos - revisar)

### Matemáticas 2 (Intermediate)
- 🔲 operaciones-con-fracciones (1 video)
- 🔲 jerarquía-con-fracciones (2 videos)
- 🔲 **[INCOMPLETO]** - Faltan tópicos de trigonometría, rectas, proporcionalidad

### Matemáticas 3 (Functions & Systems)
- 🔲 desigualdades (1 video)
- 🔲 método-de-sumas-y-restas (1 video)
- 🔲 método-de-sustitución (1 video)
- 🔲 método-determinantes-2x2 (1 video)
- 🔲 método-determinantes-3x3 (1 video)
- 🔲 completar-trinomio-cuadrado-perfecto (1 video)
- 🔲 gráfica-de-una-función-cuadrática (1 video)
- 🔲 función-cuadrática (1 video)
- 🔲 ecuación-general-de-la-circunferencia (1 video)
- 🔲 regreso-de-la-circunferencia (1 video)
- 🔲 ec-cuadráticas-incompletas (1 video)

### Matemáticas 4 (Advanced Functions)
- 🔲 evaluación-de-funciones (1 video)
- 🔲 función-escalonada (2 videos)
- 🔲 representación-de-funciones (0 videos)
- 🔲 dominio-máximo (2 videos)
- 🔲 composición-de-funciones (1 video)
- 🔲 operaciones-con-funciones-p1 (1 video)
- 🔲 análisis-de-una-función (1 video)

### Matemáticas 5 (Calculus)
- 🔲 dx-reglas-básicas (1 video)
- 🔲 dx-con-x-en-el-denominador (1 video)
- 🔲 regla-del-producto-p1 (1 video)

### Optativa
- 🔲 [Pendiente definir contenido]

---

## 🗂️ Estructura de Archivos (Actual)

```
letymath/
├── index.html                    ← Portada de LetyMath (ok)
├── assets/
│   └── logos/                    ← Iconos 2E (ok)
├── matematicas-1/
│   ├── index.html               ← Índice de curso (ok)
│   ├── operaciones-basicas.html ← Tema específico (necesita llenarse)
│   ├── jerarquia.html
│   ├── ecuaciones.html
│   ├── monomios.html
│   ├── expresiones-algebraicas.html
│   ├── grafica-tabulacion.html
│   ├── pendiente-ordenada.html
│   ├── area-perimetro.html
│   └── ecuaciones-angulos.html
├── matematicas-2/
│   └── index.html               ← Sin tópicos aún
├── matematicas-3/
│   └── index.html               ← Sin tópicos aún
├── matematicas-4/
│   ├── index.html               ← ok
│   ├── evaluacion-de-funciones.html
│   ├── funcion-escalonada.html
│   └── representacion-de-funciones.html
├── matematicas-5/
│   └── index.html               ← Sin tópicos aún
└── ...(style.css, nav.js, footer.js compartidos en raíz)
```

---

## 🎨 Template HTML para Tópicos

**Ubicación:** `matematicas-N/TOPICO.html`
**Estructura base:**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[TÍTULO] — LetyMath</title>
  <meta name="description" content="[DESCRIPCIÓN]">
  <link rel="stylesheet" href="../../style.css">
  <!-- KaTeX para fórmulas LaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
</head>
<body data-section="letymath">
  <script src="../../nav.js"></script>

  <main class="topic-content">
    <article>
      <h1>[TÍTULO del Tema]</h1>

      <!-- Sección de Contenido -->
      <section class="theory">
        <h2>Concepto</h2>
        <p>Explicación del tema usando LaTeX inline: $ax^2 + bx + c = 0$ y bloques:</p>
        <div class="math-block">
          $$f(x) = \sqrt{x^2 + 2x + 1}$$
        </div>
        <p>Más texto...</p>
      </section>

      <!-- Sección de Videos -->
      <section class="videos">
        <h2>Videos Explicativos</h2>
        <div class="video-container">
          <iframe width="100%" height="400" src="https://www.youtube.com/embed/VIDEO_ID"
            title="[Título Video]" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
        </div>
        <!-- Segundo video si aplica -->
      </section>

      <!-- Sección de Ejemplos -->
      <section class="examples">
        <h2>Ejemplos Resueltos</h2>
        <div class="example">
          <h3>Ejemplo 1</h3>
          <p><strong>Problema:</strong> [Enunciado]</p>
          <p><strong>Solución paso a paso:</strong></p>
          <ol>
            <li>Paso 1: $...$</li>
            <li>Paso 2: $...$</li>
            <li>Respuesta: $...$</li>
          </ol>
        </div>
      </section>

      <!-- Navegación entre temas -->
      <nav class="topic-nav">
        <a href="tema-anterior.html" class="prev-btn">← Tema Anterior</a>
        <a href="index.html" class="back-btn">Volver al Índice</a>
        <a href="tema-siguiente.html" class="next-btn">Tema Siguiente →</a>
      </nav>
    </article>
  </main>

  <script src="../../footer.js"></script>
  <script>
    // Renderizar LaTeX con KaTeX
    document.addEventListener("DOMContentLoaded", function() {
      renderMathInElement(document.body, {
        delimiters: [
          {left: "$$", right: "$$", display: true},
          {left: "$", right: "$", display: false}
        ]
      });
    });
  </script>
</body>
</html>
```

---

## 📸 Mapeo JPGs → Tópicos (Correlación con imágenes antiguas)

Tenemos **~300 imágenes JPG** (pag_1_foto_1.jpg hasta pag_97_foto_N.jpg)

**Estrategia:**
1. Cada imagen representa una página del documento antiguo
2. Identificar cuál tópico cubre cada página
3. **Transcribir el contenido a LaTeX** (no incrustar imágenes)
4. Mantener referencias a las imágenes como recurso de referencia

**Ejemplo:**
- `pag_5_foto_1.jpg`, `pag_5_foto_2.jpg` → "operaciones-básicas"
- `pag_15_foto_1.jpg` a `pag_18_foto_N.jpg` → "jerarquía"

---

## 🚀 Próximos Pasos

### Fase 1: Preparación (esta semana)
- [ ] **Auditar:** ¿Cuál página cubre qué tópico?
- [ ] **Documentar:** Crear mapeo JPG → Tópico
- [ ] **Validar:** Corroborar con video URLs

### Fase 2: Template & Estructura (próxima semana)
- [ ] **Crear skill** para generar HTML automáticamente O template manual
- [ ] **Completar** `matematicas-2/` a `matematicas-5/` con tópicos
- [ ] **Verificar** rutas relativas (`../../nav.js`, etc.)

### Fase 3: Contenido (en paralelo)
- [ ] **Transcribir** contenido de imágenes JPG a LaTeX
- [ ] **Incrustar** videos YouTube
- [ ] **Crear** ejemplos resueltos paso a paso

### Fase 4: Verificación Final
- [ ] **Testing:** Revisar navegación completa
- [ ] **SEO:** Verificar meta descriptions
- [ ] **Responsive:** Testear en móvil

---

## 💡 Decisiones Pendientes

1. **¿Usar Skill o Hacerlo Manual?**
   - Skill: Más rápido, pero requiere scripting
   - Manual: Más control, pero tedioso para 28+ tópicos

2. **¿Niveles de Profundidad en Contenido?**
   - Básico: Solo concepto + 1 video + 1 ejemplo
   - Intermedio: + 2-3 ejemplos + ejercicios
   - Completo: + notas, casos extremos, relaciones

3. **¿Incluir Ejercicios Interactivos?**
   - HTML puro (sin backend)
   - O referencias a PDFs descargables

---

## 📞 Preguntas para Lety

- [ ] ¿Visitas la carpeta de imágenes antiguas para verificar qué tópicos cubren?
- [ ] ¿Profundidad deseada: básica, intermedia o completa?
- [ ] ¿Quieres ejercicios interactivos o PDFs descargables?
- [ ] ¿Quieres una skill automatizada o prefieres hacerlo paso a paso?
