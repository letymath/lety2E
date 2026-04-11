# 🚀 Guía Rápida: Generando HTML LetyMath

**Estado:** Listos para empezar ✅
**Fecha:** 2026-04-08

---

## 📦 Archivos Creados para Ti

### 1. **MIGRACION_LETYMATH.md**
   - Plan completo de migración
   - Mapeo de tópicos × cursos
   - Decisiones pendientes
   - Timeline sugerido

### 2. **TEMPLATE-TOPICO.html**
   - Template HTML lista para copiar-pegar
   - Incluye KaTeX para fórmulas
   - Secciones: Concepto, Fórmulas, Videos, Ejemplos, Ejercicios
   - Solo reemplaza los `[BRACKETS]` con tu contenido

### 3. **mapeo_imagenes.py** + **mapeo_imagenes_completo.csv**
   - Script que mapea las 300+ imágenes antiguas a tópicos
   - CSV con página → tópico → archivos JPG
   - Puedes editar el mapeo si necesitas ajustes

---

## 🎯 Próximos Pasos (Orden Recomendado)

### **PASO 1: Revisar el Mapeo JPG → Tópicos** (15 min)
1. Abre: `letymath/mapeo_imagenes_completo.csv`
2. Verifica si el mapeo de páginas a tópicos es correcto
3. Particularmente revisa:
   - Páginas 61-80 (Matemáticas 2) → Necesita detalles
   - Páginas 81-97 (Matemáticas 3) → Está marcado como "[REVISAR]"
4. **Edita el script `mapeo_imagenes.py`** si el mapeo es incorrecto

### **PASO 2: Copiar y Personalizar el Template** (5 min)
1. Abre: `letymath/TEMPLATE-TOPICO.html`
2. Guarda una copia con el nombre del tópico:
   ```
   letymath/matematicas-1/operaciones-basicas.html
   letymath/matematicas-2/operaciones-con-fracciones.html
   etc.
   ```
3. Reemplaza los `[BRACKETS]`:
   - `[TÍTULO]` → "Operaciones Básicas"
   - `[DESCRIPCIÓN]` → Meta description
   - `[VIDEO_ID_1]` → ID del video YouTube
   - Contenido real en cada sección

### **PASO 3: Agregar Contenido Real** (Variable)
Para cada tópico:
1. **Concepto:** Explicación del tema
2. **Fórmulas:** Define todas las fórmulas (en LaTeX)
3. **Videos:** Incrustar 1-2 videos del CSV
4. **Ejemplos:** 2-3 ejemplos paso a paso
5. **Ejercicios:** 3-5 ejercicios con soluciones desplegables

### **PASO 4: Validar Navegación** (5 min)
1. Verifica que los links funcionen:
   - Botón "Tema Anterior" → página correcta
   - Botón "Volver al Índice" → `matematicas-N/index.html`
   - Botón "Tema Siguiente" → página correcta
2. Prueba desde ambas profundidades:
   - `letymath/matematicas-1/operaciones-basicas.html`
   - La estructura relativa es: `../../nav.js`

---

## 📋 Checklist por Curso

### ✅ Matemáticas 1 (9 tópicos)
- [ ] operaciones-basicas.html
- [ ] jerarquia.html
- [ ] ecuaciones.html
- [ ] monomios.html
- [ ] expresiones-algebraicas.html
- [ ] grafica-tabulacion.html
- [ ] pendiente-ordenada.html
- [ ] area-perimetro.html
- [ ] ecuaciones-angulos.html

### ⏳ Matemáticas 2 (2+ tópicos)
- [ ] operaciones-con-fracciones.html
- [ ] jerarquia-con-fracciones.html
- [ ] [Otros?]

### ⏳ Matemáticas 3 (7+ tópicos)
- [ ] desigualdades.html
- [ ] método-de-sumas-y-restas.html
- [ ] método-de-sustitución.html
- [ ] método-determinantes-2x2.html
- [ ] método-determinantes-3x3.html
- [ ] completar-trinomio-cuadrado-perfecto.html
- [ ] gráfica-de-una-función-cuadrática.html
- [ ] función-cuadrática.html
- [ ] ecuación-general-de-la-circunferencia.html
- [ ] regreso-de-la-circunferencia.html
- [ ] ec-cuadráticas-incompletas.html

### ⏳ Matemáticas 4 (7 tópicos)
- [ ] evaluacion-de-funciones.html
- [ ] función-escalonada.html
- [ ] representacion-de-funciones.html
- [ ] dominio-máximo.html
- [ ] composición-de-funciones.html
- [ ] operaciones-con-funciones-p1.html
- [ ] análisis-de-una-función.html

### ⏳ Matemáticas 5 (3 tópicos)
- [ ] dx-reglas-básicas.html
- [ ] dx-con-x-en-el-denominador.html
- [ ] regla-del-producto-p1.html

### ⏳ Optativa
- [ ] [Pendiente definir tópicos]

---

## 💡 Tips Prácticos

### Escribir Fórmulas en LaTeX
```html
<!-- Inline: $a^2 + b^2 = c^2$ -->
<p>El teorema de Pitágoras es $a^2 + b^2 = c^2$.</p>

<!-- Display (en su propia línea): -->
<div class="math-display">
  $$\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
</div>
```

### Incrustar Videos YouTube
```html
<!-- Obtener el VIDEO_ID de: https://www.youtube.com/watch?v=VIDEO_ID -->
<iframe width="100%" height="400"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Título del Video"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>
```

### Ejercicios Desplegables
```html
<div class="exercise">
  <p><strong>1.</strong> Resuelve: $2x + 3 = 7$</p>
  <details>
    <summary>Ver solución</summary>
    <p>$2x = 4 \Rightarrow x = 2$</p>
  </details>
</div>
```

---

## 🔗 Estructura de Carpetas Actual

```
letymath/
├── index.html                              ← Portada (ok)
├── TEMPLATE-TOPICO.html                   ← Copia esto para cada tema
├── mapeo_imagenes.py                       ← Script auxiliar
├── mapeo_imagenes_completo.csv             ← Referencia
├── assets/logos/                           ← Iconos (ok)
├── matematicas-1/
│   ├── index.html                          ← Índice curso (ok)
│   ├── operaciones-basicas.html            ← Crea a partir del template
│   ├── jerarquia.html
│   ├── ecuaciones.html
│   └── ... (resto de tópicos)
├── matematicas-2/
│   ├── index.html                          ← Incompleto
│   └── [tópicos: pendiente]
├── matematicas-3/
│   ├── index.html                          ← Incompleto
│   └── [tópicos: pendiente]
└── ... (4 y 5 similar)
```

---

## ❓ Preguntas Frecuentes

**P: ¿Cómo cambio el nombre de un tópico en el índice?**
R: Abre `matematicas-N/index.html` y cambia el texto en los `<a href>` cards.

**P: ¿Dónde obtengo los IDs de YouTube?**
R: En la URL: `https://www.youtube.com/watch?v=**ESTE_ES_EL_ID**`

**P: ¿La navegación nav/footer funcionará correctamente?**
R: Sí, siempre y cuando mantengas la estructura:
- `letymath/matematicas-1/tema.html` → usa `src="../../nav.js"` (2 `../`)

**P: ¿Necesito crear una skill?**
R: No es necesario. El enfoque híbrido (template + copiar-pegar) es suficiente.
Si quieres automatizar completamente, sí podemos crear una.

**P: ¿Puedo usar las imágenes JPG directamente en el HTML?**
R: Técnicamente sí, pero preferimos LaTeX para:
- Mejor calidad en cualquier resolución
- Texto indexable (SEO)
- Más consistente con tu brand
- Fácil de editar

---

## 🎬 Ahora Tú

1. Abre `MIGRACION_LETYMATH.md` y revisa el plan completo
2. Verifica el `mapeo_imagenes_completo.csv`
3. Elige un tópico para empezar (sugiero: "operaciones-basicas.html")
4. Copia el `TEMPLATE-TOPICO.html` y personalízalo
5. **¡Envíame preguntas según avances!**

---

**¿Necesitas ayuda con algo específico?** Pregúntame en cualquier momento.
