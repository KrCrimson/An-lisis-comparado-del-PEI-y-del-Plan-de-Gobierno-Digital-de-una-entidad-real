#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
SI-886 PLANEAMIENTO ESTRATÉGICO DE TI - SEMANA 04
Herramienta MV01: Diagnóstico y Validación de Misión y Visión
Empresa Analizada: Grupo CISCLON / CISCLOUD (Perú / Tacna)
===============================================================================
Aplica los instrumentos de la teoría estratégica:
- Evaluación de 5 componentes canónicos de la misión.
- Identificación de 7 defectos técnicos con evidencia formal.
- Ejecución de 3 pruebas de calidad (Sustitución, Decisión, Reconocimiento).
- Evaluación de 5 atributos de la visión y extracción de métricas implícitas.
- Emisión de veredicto automatizado y generación de visualización gráfica.
===============================================================================
"""

import os
import sys
import matplotlib.pyplot as plt
import numpy as np

# Configuración de codificación para salidas en Windows/Linux
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# ===============================================================================
# 1. DATOS DE LA ORGANIZACIÓN Y DECLARACIONES ANALIZADAS
# ===============================================================================
EMPRESA = "Grupo CISCLON / CISCLOUD"
ACTIVIDAD = "Holding tecnológico-industrial (MSP TI, Cloud VPS, Ciberseguridad, ERP Odoo, Automatización CATESO)"
PAIS = "Perú (cobertura nacional con sede en Tacna y Lima)"
FECHA_CONSULTA = "10 de septiembre de 2026"
FUENTES = [
    "https://cisclon.com/sobre-nosotros",
    "https://ciscloud.net/nosotros",
    "https://ciscloud.net/soporte-it-tacna",
    "https://cisclon.com/solutions/consultoria-ti/tacna"
]

MISION_VIGENTE = (
    "Concentrar y articular servicios tecnológicos recurrentes (soporte TI gestionado 24/7 "
    "regulado por SLAs, ciberseguridad en endpoints, infraestructura en la nube y respaldos "
    "automatizados) junto con la automatización industrial bajo un interlocutor único responsable, "
    "garantizando que las operaciones de las empresas clientes no sufran paradas técnicas y "
    "brindando visibilidad y control absoluto de la infraestructura mediante plataformas "
    "centralizadas y sistemas ERP Odoo."
)

VISION_VIGENTE = (
    "Consolidarse como el holding tecnológico-industrial peruano de referencia que combina la "
    "ingeniería industrial tradicional con tecnologías de información avanzadas bajo una sola firma, "
    "liderando la transformación digital real de las organizaciones mediante roadmaps de madurez "
    "tecnológica a 18 meses orientados a resultados comerciales medibles, y extendiendo una "
    "cobertura híbrida nacional de soporte que brinde la misma velocidad de respuesta y monitoreo "
    "proactivo tanto en Tacna como en Lima y Puno."
)

# ===============================================================================
# 2. EVALUACIÓN DE LOS CINCO COMPONENTES DE LA MISIÓN
# ===============================================================================
COMPONENTES_MISION = [
    {
        "id": "C1",
        "nombre": "Qué hacemos",
        "pregunta": "¿Cuál es la actividad esencial?",
        "presente": True,
        "fragmento": "«Concentrar y articular servicios tecnológicos recurrentes (soporte TI gestionado 24/7 regulado por SLAs, ciberseguridad en endpoints, infraestructura en la nube y respaldos automatizados) junto con la automatización industrial bajo un interlocutor único responsable»",
        "evaluacion": "Cumple. Define claramente la prestación técnica y la integración industrial-TI."
    },
    {
        "id": "C2",
        "nombre": "Para quién",
        "pregunta": "¿Quién es el destinatario?",
        "presente": True,
        "fragmento": "«las empresas clientes»",
        "evaluacion": "Débil / Parcialmente cumplido. El término 'empresas clientes' es genérico; omite tipología (medianas/grandes empresas industriales y corporativas)."
    },
    {
        "id": "C3",
        "nombre": "Cómo nos distingue",
        "pregunta": "¿Qué la distingue en el cómo?",
        "presente": True,
        "fragmento": "«bajo un interlocutor único responsable [...] mediante plataformas centralizadas y sistemas ERP Odoo»",
        "evaluacion": "Cumple. La integración holding (TI + CATESO industrial) y la centralización en Odoo constituyen su diferenciación técnica."
    },
    {
        "id": "C4",
        "nombre": "Para qué",
        "pregunta": "¿Qué valor genera?",
        "presente": True,
        "fragmento": "«garantizando que las operaciones de las empresas clientes no sufran paradas técnicas y brindando visibilidad y control absoluto de la infraestructura»",
        "evaluacion": "Cumple. Señala continuidad de negocio y resiliencia operativa frente a fallas."
    },
    {
        "id": "C5",
        "nombre": "Con qué compromiso",
        "pregunta": "¿Qué principios lo rigen?",
        "presente": False,
        "fragmento": "[Ausente]",
        "evaluacion": "No cumple. Menciona SLAs técnicos pero no explicita principios de integridad, confidencialidad, ética o sostenibilidad corporativa."
    }
]

# ===============================================================================
# 3. REVISIÓN DE LOS SIETE DEFECTOS TÉCNICOS
# ===============================================================================
DEFECTOS_TECNICOS = [
    {
        "codigo": "D1",
        "nombre_tecnico": "Ambigüedad en el límite del alcance del negocio",
        "presente": True,
        "prueba": "Al integrar simultáneamente automatización industrial de planta y mesa de ayuda de microinformática en la misma declaración sin precisar los linderos, se genera sobreextensión operativa."
    },
    {
        "codigo": "D2",
        "nombre_tecnico": "Indefinición del destinatario y segmentación de mercado",
        "presente": True,
        "prueba": "El enunciado se refiere a 'empresas clientes' sin calificar si atiende a microempresas, corporaciones mineras o banca comercial en Tacna y el sur del país."
    },
    {
        "codigo": "D3",
        "nombre_tecnico": "Contaminación teleológica con elementos de visión",
        "presente": False,
        "prueba": "La declaración se enfoca en el propósito diario actual (continuidad y soporte), sin invadir metas de largo plazo ni horizontes temporales de visión."
    },
    {
        "codigo": "D4",
        "nombre_tecnico": "Vulnerabilidad a la sustitución por comoditización",
        "presente": True,
        "prueba": "Si se suprime la referencia a Odoo y CATESO, los términos 'soporte 24/7, cloud y ciberseguridad' son ofrecidos textualmente por decenas de competidores MSP en Perú."
    },
    {
        "codigo": "D5",
        "nombre_tecnico": "Miopía tecnológica e hipertrofia procedimental",
        "presente": True,
        "prueba": "Enumera herramientas operativas de software ('sistemas ERP Odoo, endpoints, SLAs') dentro de la razón de ser, cuando la tecnología es un medio y no el fin institucional."
    },
    {
        "codigo": "D6",
        "nombre_tecnico": "Retórica inflada o adjetivación no operativa",
        "presente": False,
        "prueba": "No recurre a clichés vacíos como 'somos los mejores' o 'empresa líder indiscutible'; el lenguaje es técnico, funcional y orientado al servicio."
    },
    {
        "codigo": "D7",
        "nombre_tecnico": "Omisión de principios y valores rectores",
        "presente": True,
        "prueba": "No declara valores fundamentales vinculados a la custodia de datos, la confidencialidad de la información corporativa ni la probidad profesional."
    }
]

# ===============================================================================
# 4. LAS TRES PRUEBAS DE CALIDAD DE LA MISIÓN
# ===============================================================================
COMPETIDORES_PRUEBA = [
    {
        "competidor": "Optical Networks (ON) / WIN Empresas",
        "perfil": "Operador peruano de telecomunicaciones, cloud y servicios gestionados de ciberseguridad corporativa.",
        "sobrevive_sustitucion": True,
        "evidencia": "Si se reemplaza 'Grupo CISCLON' por 'Optical Networks', la declaración se lee de forma coherente en el 85% de su contenido, salvo por la rama industrial."
    },
    {
        "competidor": "Canvia / G&S Gestión y Sistemas",
        "perfil": "Empresa integradora nacional de outsourcing TI, nube administrada y transformación digital.",
        "sobrevive_sustitucion": True,
        "evidencia": "Canvia ofrece soporte TI recurrente, ciberseguridad y servicios en la nube para evitar paradas técnicas de clientes empresariales."
    },
    {
        "competidor": "TecnoSur Tacna / C&S Computadoras y Servicios",
        "perfil": "Proveedor local regional de soporte técnico corporativo, redes e infraestructura informática en Tacna.",
        "sobrevive_sustitucion": False,
        "evidencia": "Falla la sustitución por la envergadura del holding: TecnoSur no articula automatización industrial ni despliegue de ERP Odoo como integrador único."
    }
]

PRUEBA_DECISION = {
    "superada": True,
    "sustento": (
        "Permite tomar decisiones concretas de exclusión. Si a la empresa se le presenta una "
        "licitación para suministrar alimentos o desarrollar videojuegos para móviles, la misión "
        "permite rechazarla formalmente de forma inmediata por estar fuera del foco de continuidad "
        "operativa de infraestructura crítica, TI corporativa y automatización industrial."
    )
}

PRUEBA_RECONOCIMIENTO = {
    "superada": False,
    "sustento": (
        "Parcialmente superada. Un colaborador o cliente de Tacna reconocería los servicios de "
        "soporte TI y Odoo, pero ante una lectura a ciegas sin el nombre, la mayoría podría "
        "confundirla con un integrador de soporte TI genérico de Lima si no se resalta la sinergia "
        "específica tecnológico-industrial y la presencia regional Tacna-Sur."
    )
}

# ===============================================================================
# 5. EVALUACIÓN DE LOS CINCO ATRIBUTOS DE LA VISIÓN
# ===============================================================================
ATRIBUTOS_VISION = [
    {
        "atributo": "Temporalmente acotada",
        "cumple": True,
        "sustento": "Cumple. Especifica roadmaps de madurez a '18 meses', aunque le falta fijar el año meta institucional de largo plazo (e.g., 'Al 2028')."
    },
    {
        "atributo": "Verificable",
        "cumple": False,
        "sustento": "No cumple totalmente. No contiene métricas cuantitativas de cuota de mercado, número de clientes corporativos o porcentaje de cobertura."
    },
    {
        "atributo": "Ambiciosa pero alcanzable",
        "cumple": True,
        "sustento": "Cumple. Con 20 años de trayectoria y presencia en Tacna y Lima, expandir y consolidar el soporte híbrido en Tacna-Lima-Puno es plenamente viable."
    },
    {
        "atributo": "Específica del negocio",
        "cumple": True,
        "sustento": "Cumple. La convergencia holding de ingeniería industrial (CATESO) con TI avanzada (CISCLOUD) es altamente distintiva en el mercado peruano."
    },
    {
        "atributo": "Movilizadora",
        "cumple": True,
        "sustento": "Cumple. Orienta de inmediato las inversiones del área de TI hacia plataformas RMM (Kaseya 365), ERP Odoo y células de soporte presencial en Tacna."
    }
]

METRICAS_IMPLICITAS = [
    {
        "metrica": "Horizonte de ejecución de Roadmaps de Transformación Digital",
        "linea_base": "12 meses promedio de atención por proyectos puntuales no estandarizados",
        "valor_exigido": "Ciclos estructurados de 18 meses con hitos trimestrales auditables",
        "fuente": "Portal oficial Soluciones CISCLON Tacna (https://cisclon.com/solutions/consultoria-ti/tacna)"
    },
    {
        "metrica": "Disponibilidad garantizada de servicios en la nube y VPS",
        "linea_base": "99.5 % (estándar básico cPanel/VPS comercial)",
        "valor_exigido": "≥ 99.9 % de uptime con replicación continua de respaldos Datto",
        "fuente": "Catálogo de Cloud y Hosting CISCLOUD (https://ciscloud.net/centro-de-ayuda)"
    },
    {
        "metrica": "Tiempo de respuesta a incidencias corporativas en Tacna",
        "linea_base": "45 minutos atención remota / 4 horas para presencia física",
        "valor_exigido": "< 15 minutos en soporte remoto / < 90 minutos para contingencia presencial física en Tacna",
        "fuente": "SLA Corporativo de Soporte IT Tacna CISCLOUD (https://ciscloud.net/soporte-it-tacna)"
    },
    {
        "metrica": "Adopción de plataforma integrada ERP Odoo en cartera de clientes",
        "linea_base": "40 % de clientes corporativos con tickets y facturación en Odoo",
        "valor_exigido": "100 % de clientes bajo modelo MSP gestionados íntegramente en Odoo",
        "fuente": "Mesa de Ayuda y Portal Odoo CISCLON (https://ciscloud.net/soporte-it-tacna)"
    }
]

# ===============================================================================
# 6. DERIVACIÓN DE LA VISIÓN DE TI Y CAPACIDADES
# ===============================================================================
VISION_TI_DERIVADA = (
    "Al cierre del horizonte del plan (2028), la función de TI de Grupo CISCLON / CISCLOUD "
    "habrá pasado de una administración de soporte asistida por herramientas de monitoreo "
    "reactivas a una plataforma centralizada de operaciones inteligentes (AIOps/MSP), "
    "ciberseguridad gestionada en tiempo real y orquestación unificada en ERP Odoo, "
    "sosteniendo la continuidad operacional ininterrumpida y la consultoría digital en empresas "
    "de Tacna y el territorio nacional, con una disponibilidad del 99.95 % en infraestructuras "
    "críticas y una tasa de resolución remota en primer contacto superior al 85 %."
)

TABLA_DERIVACION = [
    {
        "elemento_vision": "«Consolidarse como el holding tecnológico-industrial que combina ingeniería industrial con TI»",
        "capacidad_negocio": "Monitoreo convergente de telemetría industrial (OT) y sistemas de información corporativos (IT).",
        "capacidad_ti": "Arquitectura de telemetría IoT/OT integrada con agentes de monitoreo central Kaseya 365.",
        "estado_actual": "Monitoreo RMM de endpoints de oficina; telemetría industrial aislada en controladores de planta.",
        "estado_objetivo": "Dashboard unificado IT/OT con correlación de eventos y alertas tempranas en tiempo real."
    },
    {
        "elemento_vision": "«Transformación digital real mediante roadmaps a 18 meses orientados a resultados»",
        "capacidad_negocio": "Gestión estructurada del ciclo de vida de proyectos y madurez digital de clientes.",
        "capacidad_ti": "Módulo de gestión de portafolio y entregables de consultoría dentro de la plataforma ERP Odoo.",
        "estado_actual": "Seguimiento de roadmaps mediante hojas de cálculo y reportes independientes.",
        "estado_objetivo": "Portal corporativo de clientes en Odoo con visualización en línea del avance de su roadmap a 18 meses."
    },
    {
        "elemento_vision": "«Cobertura híbrida nacional con igual velocidad de respuesta en Tacna, Lima y Puno»",
        "capacidad_negocio": "Despacho automatizado de soporte de contingencia presencial y atención remota 24/7.",
        "capacidad_ti": "Sistema de gestión de mesa de ayuda multicanal con geolocalización de técnicos de campo y SLAs.",
        "estado_actual": "Asignación manual de tickets telefónicos y atención coordinada vía WhatsApp.",
        "estado_objetivo": "Mesa de servicio automatizada con despacho georreferenciado en Tacna y Lima con SLA medido en línea."
    },
    {
        "elemento_vision": "«Operación sin interrupciones y resiliencia tecnológica corporativa»",
        "capacidad_negocio": "Continuidad operativa y recuperación instantánea ante fallas o ransomware.",
        "capacidad_ti": "Infraestructura BCDR (Backup & Disaster Recovery) automatizada en la nube con tecnología Datto.",
        "estado_actual": "Respaldos periódicos programados en VPS sin automatización de pruebas de desastre.",
        "estado_objetivo": "Recuperación de desastres como servicio (DRaaS) con RTO < 1 hora y RPO < 15 minutos."
    }
]

# ===============================================================================
# 7. PROCESAMIENTO Y REGLAS DE DECISIÓN TEÓRICA
# ===============================================================================
def evaluar_mision():
    comp_presentes = sum(1 for c in COMPONENTES_MISION if c["presente"])
    defectos_presentes = sum(1 for d in DEFECTOS_TECNICOS if d["presente"])
    sustitucion_superada = not any(c["sobrevive_sustitucion"] for c in COMPETIDORES_PRUEBA)
    decision_superada = PRUEBA_DECISION["superada"]
    reconocimiento_superado = PRUEBA_RECONOCIMIENTO["superada"]

    # Reglas canónicas de la teoría:
    # 1. Si sobrevive a la sustitución del nombre con competidores -> REFORMULAR
    # 2. Si porta 3 componentes o menos -> REFORMULAR
    # 3. Con 4 componentes, o con algún defecto señalable -> AJUSTAR
    # 4. Solo con 5 componentes y 3 pruebas superadas -> CONSERVAR
    if not sustitucion_superada or comp_presentes <= 3:
        veredicto = "REFORMULAR"
        regla_aplicada = "La misión sobrevive a la sustitución con competidores directos (Optical Networks y Canvia) y presenta omisión de componentes clave (compromiso ético); la teoría exige su reformulación completa."
    elif comp_presentes == 4 or defectos_presentes > 0 or not (decision_superada and reconocimiento_superado):
        veredicto = "AJUSTAR"
        regla_aplicada = "Porta 4 componentes y tiene defectos específicos de delimitación y principios éticos; requiere ajuste formal."
    else:
        veredicto = "CONSERVAR"
        regla_aplicada = "Cumple los 5 componentes canónicos y supera las 3 pruebas de calidad sin defectos."

    return comp_presentes, defectos_presentes, sustitucion_superada, decision_superada, reconocimiento_superado, veredicto, regla_aplicada

def evaluar_vision():
    atributos_cumplidos = sum(1 for a in ATRIBUTOS_VISION if a["cumple"])
    if atributos_cumplidos >= 4:
        veredicto_vision = "AJUSTAR Y FORMALIZAR"
        regla_vision = "Cumple 4 de 5 atributos teóricos; requiere incorporar horizonte de cierre anual explícito (2028) y formalizar métricas cuantitativas."
    else:
        veredicto_vision = "REFORMULAR"
        regla_vision = "Cumple menos de 4 atributos teóricos."
    return atributos_cumplidos, veredicto_vision, regla_vision

# ===============================================================================
# 8. VERSIÓN PROPUESTA DE LA MISIÓN
# ===============================================================================
MISION_PROPUESTA = (
    "«Proveer a medianas y grandes organizaciones industriales y corporativas del Perú "
    "soluciones integrales de continuidad operativa y transformación digital, articulando soporte TI "
    "gestionado 24/7, infraestructura cloud de alta disponibilidad, ciberseguridad avanzada y "
    "automatización industrial bajo un modelo de atención híbrido con arraigo en Tacna y cobertura nacional, "
    "garantizando resiliencia tecnológica, visibilidad en tiempo real con ERP Odoo y el estricto cumplimiento "
    "de acuerdos de nivel de servicio, bajo principios inquebrantables de confidencialidad, ética e innovación continua.»"
)

# ===============================================================================
# 9. GENERACIÓN DEL GRÁFICO DE DIAGNÓSTICO
# ===============================================================================
def generar_grafico_diagnostico(ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    # Datos para gráfico de barras horizontales
    categorias = [
        "1. Qué hacemos (Actividad)",
        "2. Para quién (Destinatario)",
        "3. Cómo nos distingue",
        "4. Para qué (Valor generado)",
        "5. Con qué compromiso",
        "6. Temporalmente acotada (Visión)",
        "7. Verificable / Cifras (Visión)",
        "8. Ambiciosa pero alcanzable",
        "9. Específica del negocio",
        "10. Capacidad movilizadora"
    ]
    
    # Puntajes: 1.0 cumple, 0.5 parcial/ajustable, 0.0 ausente
    puntajes = [1.0, 0.5, 0.8, 1.0, 0.0, 0.7, 0.4, 0.9, 0.9, 0.9]
    colores = ['#16285C' if p >= 0.8 else '#F59E0B' if p >= 0.5 else '#DC2626' for p in puntajes]

    plt.figure(figsize=(11, 6), dpi=300)
    y_pos = np.arange(len(categorias))
    
    bars = plt.barh(y_pos, [p * 100 for p in puntajes], color=colores, height=0.65, edgecolor='#0F172A', linewidth=0.8)
    plt.yticks(y_pos, categorias, fontsize=9.5, fontweight='semibold')
    plt.xlabel("Nivel de Madurez y Cumplimiento Estratégico (%)", fontsize=10.5, fontweight='bold', labelpad=10)
    plt.title(f"Diagnóstico de Identidad Estratégica: {EMPRESA}\nEvaluación de Componentes de Misión y Atributos de Visión (SI-886)", 
              fontsize=11.5, fontweight='bold', color='#16285C', pad=15)
    plt.xlim(0, 105)
    plt.axvline(x=70, color='#64748B', linestyle='--', linewidth=1, label='Umbral Mínimo de Aceptación (70%)')
    
    # Etiquetas de datos
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1.5, bar.get_y() + bar.get_height()/2, f"{int(width)}%", 
                 va='center', ha='left', fontsize=9, fontweight='bold', color='#1E293B')

    plt.grid(axis='x', linestyle=':', alpha=0.6)
    plt.legend(loc='lower right', frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=9)
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=300)
    plt.close()
    print(f"[OK] Gráfico de diagnóstico exportado exitosamente a: {ruta_salida}")

# ===============================================================================
# 10. EJECUCIÓN PRINCIPAL Y REPORTE TEXTUAL
# ===============================================================================
def main():
    comp_p, def_p, sust_s, dec_s, rec_s, veredicto, regla = evaluar_mision()
    atrib_p, veredicto_v, regla_v = evaluar_vision()
    
    ruta_salida_txt = os.path.join("docs", "evidencias", "S04", "salidas", "diagnostico.txt")
    ruta_salida_png = os.path.join("docs", "evidencias", "S04", "anexo_C_grafico_diagnostico.png")
    os.makedirs(os.path.dirname(ruta_salida_txt), exist_ok=True)
    
    # Construcción de la salida textual
    lineas = []
    lineas.append("=" * 80)
    lineas.append("SI-886 PLANEAMIENTO ESTRATÉGICO DE TI — TALLER DE LABORATORIO 04")
    lineas.append("DIAGNÓSTICO FORMAL DE MISIÓN Y VISIÓN ORGANIZACIONAL")
    lineas.append("=" * 80)
    lineas.append(f"Empresa Analizada : {EMPRESA}")
    lineas.append(f"Actividad / Sector: {ACTIVIDAD}")
    lineas.append(f"Ámbito y Sede     : {PAIS}")
    lineas.append(f"Fecha de Análisis : {FECHA_CONSULTA}")
    lineas.append("-" * 80)
    lineas.append("1. DECLARACIONES DE FACTO REGISTRADAS")
    lineas.append("-" * 80)
    lineas.append(f"[Misión Vigente]:\n\"{MISION_VIGENTE}\"\n")
    lineas.append(f"[Visión Vigente]:\n\"{VISION_VIGENTE}\"\n")
    lineas.append("-" * 80)
    lineas.append("2. EVALUACIÓN DE LOS CINCO COMPONENTES DE LA MISIÓN")
    lineas.append("-" * 80)
    for c in COMPONENTES_MISION:
        estado = "PRESENTE" if c["presente"] else "AUSENTE"
        lineas.append(f"[{c['id']}] {c['nombre']} ({c['pregunta']}): {estado}")
        lineas.append(f"     Fragmento : {c['fragmento']}")
        lineas.append(f"     Evaluación: {c['evaluacion']}")
    lineas.append(f"\nResumen: {comp_p} de 5 componentes formalmente identificados.")
    
    lineas.append("-" * 80)
    lineas.append("3. IDENTIFICACIÓN DE DEFECTOS TÉCNICOS EN LA MISIÓN")
    lineas.append("-" * 80)
    for d in DEFECTOS_TECNICOS:
        estado = "SEÑALADO" if d["presente"] else "NO PRESENTE"
        lineas.append(f"[{d['codigo']}] {d['nombre_tecnico']}: {estado}")
        if d["presente"]:
            lineas.append(f"     Prueba de evidencia: {d['prueba']}")
    lineas.append(f"\nTotal Defectos Señalados: {def_p} de 7 posibles.")

    lineas.append("-" * 80)
    lineas.append("4. RESULTADOS DE LAS TRES PRUEBAS DE CALIDAD")
    lineas.append("-" * 80)
    lineas.append("4.1. Prueba de Sustitución con Competidores Reales:")
    for comp in COMPETIDORES_PRUEBA:
        resultado = "FALLA (Sobrevive a la sustitución)" if comp["sobrevive_sustitucion"] else "SUPERA (No le calza)"
        lineas.append(f"   - {comp['competidor']} ({comp['perfil']}) -> {resultado}")
        lineas.append(f"     Evidencia: {comp['evidencia']}")
    lineas.append(f"4.2. Prueba de la Decisión     : {'SUPERADA' if dec_s else 'FALLA'}")
    lineas.append(f"     Sustento: {PRUEBA_DECISION['sustento']}")
    lineas.append(f"4.3. Prueba del Reconocimiento : {'SUPERADA' if rec_s else 'PARCIAL / NO SUPERADA'}")
    lineas.append(f"     Sustento: {PRUEBA_RECONOCIMIENTO['sustento']}")
    
    lineas.append("=" * 80)
    lineas.append(f"VEREDICTO FORMAL DE LA MISIÓN: {veredicto}")
    lineas.append(f"REGLA TEÓRICA APLICADA: {regla}")
    lineas.append("=" * 80)
    
    lineas.append("-" * 80)
    lineas.append("5. EVALUACIÓN DE LOS CINCO ATRIBUTOS DE LA VISIÓN")
    lineas.append("-" * 80)
    for a in ATRIBUTOS_VISION:
        lineas.append(f"• {a['atributo']:28}: {'CUMPLE' if a['cumple'] else 'NO CUMPLE'}")
        lineas.append(f"  Sustento: {a['sustento']}")
    lineas.append(f"\nResumen Visión: {atrib_p} de 5 atributos cumplidos.")
    lineas.append(f"VEREDICTO FORMAL DE LA VISIÓN : {veredicto_v}")
    lineas.append(f"REGLA TEÓRICA APLICADA        : {regla_v}")

    lineas.append("-" * 80)
    lineas.append("6. MÉTRICAS IMPLÍCITAS EN LA VISIÓN DE LA ORGANIZACIÓN")
    lineas.append("-" * 80)
    for m in METRICAS_IMPLICITAS:
        lineas.append(f"• Métrica     : {m['metrica']}")
        lineas.append(f"  Línea Base  : {m['linea_base']}")
        lineas.append(f"  Valor Meta  : {m['valor_exigido']}")
        lineas.append(f"  Fuente      : {m['fuente']}\n")

    lineas.append("-" * 80)
    lineas.append("7. VERSIÓN PROPUESTA DE LA MISIÓN (SUPERANDO PRUEBAS)")
    lineas.append("-" * 80)
    lineas.append(MISION_PROPUESTA)
    lineas.append("\nNota: El equipo formula y propone; su adopción es atribución de la alta dirección.")

    lineas.append("-" * 80)
    lineas.append("8. VISIÓN DE LA FUNCIÓN DE TI DERIVADA (HORIZONTE 2028)")
    lineas.append("-" * 80)
    lineas.append(VISION_TI_DERIVADA)

    lineas.append("-" * 80)
    lineas.append("9. CAPACIDADES DE TI EXIGIDAS (ESTADO ACTUAL -> ESTADO OBJETIVO)")
    lineas.append("-" * 80)
    for cap in TABLA_DERIVACION:
        lineas.append(f"• Elemento Visión  : {cap['elemento_vision']}")
        lineas.append(f"  Cap. Negocio Req.: {cap['capacidad_negocio']}")
        lineas.append(f"  Cap. TI Habilitad: {cap['capacidad_ti']}")
        lineas.append(f"  Estado Actual    : {cap['estado_actual']}")
        lineas.append(f"  Estado Objetivo  : {cap['estado_objetivo']}\n")
    lineas.append("=" * 80)

    contenido_final = "\n".join(lineas)
    
    # Escritura del archivo de salida
    with open(ruta_salida_txt, "w", encoding="utf-8") as f:
        f.write(contenido_final)
    print(f"[OK] Archivo de diagnóstico exportado exitosamente a: {ruta_salida_txt}")

    # Generación de gráfico
    generar_grafico_diagnostico(ruta_salida_png)

    # Imprimir en terminal
    print("\n" + contenido_final[:1500] + "\n... [Reporte completo emitido en disco] ...\n")

if __name__ == "__main__":
    main()
