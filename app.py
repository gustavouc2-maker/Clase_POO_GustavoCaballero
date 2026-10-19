
import streamlit as st
from desarrollo_de_una_aplicacion import Estudiante

# Título del programa
st.title("Sistema de Gestión de Estudiantes")
st.write("Registro de estudiantes y calificaciones")

# Guardar estudiantes durante la sesión
if "estudiantes" not in st.session_state:
    st.session_state.estudiantes = {}

# Registrar un estudiante
st.subheader("Registrar estudiante")

nombre = st.text_input("Nombre del estudiante")
matricula = st.text_input("Matrícula")

if st.button("Registrar estudiante"):
    if nombre.strip() and matricula.strip():
        if matricula in st.session_state.estudiantes:
            st.warning("Esta matrícula ya existe")
        else:
            alumno = Estudiante(nombre, matricula)
            st.session_state.estudiantes[matricula] = alumno
            st.success("Estudiante registrado correctamente")
    else:
        st.warning("Completa los datos")

# Consultar estudiantes
st.subheader("Consultar estudiantes")

if st.session_state.estudiantes:
    matricula_elegida = st.selectbox(
        "Selecciona un estudiante",
        list(st.session_state.estudiantes.keys())
    )

    alumno = st.session_state.estudiantes[matricula_elegida]

    st.write("Nombre:", alumno.nombre)
    st.write("Matrícula:", alumno.matricula)

    # Agregar calificaciones
    nota = st.number_input(
        "Ingresa una calificación",
        min_value=0,
        max_value=100,
        value=90
    )

    if st.button("Agregar calificación"):
        alumno.agregar_calificacion(nota)
        st.success("Calificación agregada")

    st.write("Calificaciones:", alumno.calificaciones)
    st.write("Promedio:", alumno.calcular_promedio())

else:
    st.info("Todavía no hay estudiantes registrados")
