# PETI · Plan Estratégico de Tecnologías de Información
## Empresa: Grupo CISCLON / CISCLOUD (Perú / Tacna)

**Curso:** SI-886 · Planeamiento Estratégico de TI  
**Docente:** Dr. Oscar Juan Jimenez Flores  
**Institución:** Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna  
**Ciclo Académico:** 2026-II  

---

## 1. Descripción del Proyecto

Repositorio oficial del Plan Estratégico de Tecnologías de Información (PETI) para el **Grupo CISCLON / CISCLOUD**, holding tecnológico-industrial peruano con más de 20 años de trayectoria (fundado en noviembre de 2003), con centros de operación corporativa en Tacna y Lima, y cobertura de servicios gestionados de TI (MSP), infraestructura cloud, ciberseguridad, ERP Odoo y automatización industrial (rama CATESO).

---

## 2. Estructura del Repositorio

```
peti/
├── 02_identidad/
│   ├── MV01_declaraciones.md             # Ficha de registro de declaraciones (Paso A)
│   ├── MV01_diagnostico_declaraciones.py # Script en Python con diagnóstico cuantitativo y cualitativo
│   ├── 2.1_mision.md                     # Sección 2.1 del PETI: Diagnóstico y propuesta de Misión
│   └── 2.2_vision.md                     # Sección 2.2 del PETI: Evaluación de Visión y Derivación de Capacidades de TI
├── docs/
│   └── evidencias/
│       └── S04/
│           ├── anexo_C_grafico_diagnostico.png # Visualización gráfica de cumplimiento estratégico
│           └── salidas/
│               └── diagnostico.txt       # Reporte textual completo generado por la herramienta MV01
├── SI886-PLANTILLA-TALLER.docx           # Plantilla oficial institucional UPT
├── SI886-S04-TALLER-Grupo4.docx          # Informe formal completo listo para entrega
└── SI886-S04-TALLER-Grupo4.pdf           # Informe exportado a formato PDF
```

---

## 3. Instrucciones de Ejecución

Para reproducir el diagnóstico y regenerar las evidencias cuantitativas y visuales:

```bash
# 1. Asegurar dependencias de Python
pip install matplotlib numpy python-docx

# 2. Ejecutar el script de diagnóstico
python 02_identidad/MV01_diagnostico_declaraciones.py
```

---

## 4. Trazabilidad de Versiones y Etiquetas Git

- `v0.4`: PETI v0.4 — Identidad estratégica (Misión, Visión y Visión de TI).
- `taller-04`: Taller 04 · SI886 (Entrega formal procedimental).
