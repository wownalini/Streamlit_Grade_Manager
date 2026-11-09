import streamlit as st

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

if "students" not in st.session_state:
    st.session_state.students = []

# Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #1e3a5f;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        text-align: center;
        color: #64748b;
        margin-bottom: 2rem;
        font-size: 1.05rem;
    }
    .metric-card {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    .metric-card h3 {
        margin: 0;
        font-size: 0.95rem;
        color: #475569;
    }
    .metric-card p {
        margin: 0.3rem 0 0 0;
        font-size: 1.8rem;
        font-weight: 700;
        color: #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">🎓 Student Grade Manager</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Add students, view results and get class performance overview.</div>', unsafe_allow_html=True)

# Add Student
st.subheader("➕ Add Student Record")
st.caption("Add a student and their mark to the class.")

with st.form("add_student", clear_on_submit=True):
    col1, col2, col3 = st.columns([2, 1.5, 1])
    with col1:
        name = st.text_input("Student Name", placeholder="Enter student name")
    with col2:
        mark = st.number_input("Mark (out of 100)", min_value=0, max_value=100, value=0)
    with col3:
        st.write("")
        st.write("")
        submitted = st.form_submit_button("➕ Add Record", use_container_width=True)

    if submitted:
        if not name.strip():
            st.error("Please enter a student name.")
        else:
            grade = get_grade(mark)
            st.session_state.students.append({
                "Name": name.strip(),
                "Mark": int(mark),
                "Grade": grade
            })
            st.success(f"Added {name.strip()} — Grade {grade}")

# Results
if st.session_state.students:
    st.subheader("📊 Class Results")
    table_data = []
    for i, s in enumerate(st.session_state.students, 1):
        table_data.append({
            "#": i,
            "Student Name": s["Name"],
            "Mark": s["Mark"],
            "Grade": s["Grade"]
        })
    st.dataframe(table_data, use_container_width=True, hide_index=True)

    # Overview with colored cards
    marks = [s["Mark"] for s in st.session_state.students]
    total = len(marks)
    average = sum(marks) / total
    highest = max(marks)
    lowest = min(marks)

    st.subheader("📈 Overview")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f'''
        <div class="metric-card" style="background:#eff6ff;">
            <h3>Total Students</h3>
            <p>{total}</p>
        </div>
        ''', unsafe_allow_html=True)

    with c2:
        st.markdown(f'''
        <div class="metric-card" style="background:#ecfdf5;">
            <h3>Class Average</h3>
            <p>{average:.1f}</p>
        </div>
        ''', unsafe_allow_html=True)

    with c3:
        st.markdown(f'''
        <div class="metric-card" style="background:#fffbeb;">
            <h3>Highest Mark</h3>
            <p>{highest}</p>
        </div>
        ''', unsafe_allow_html=True)

    with c4:
        st.markdown(f'''
        <div class="metric-card" style="background:#fef2f2;">
            <h3>Lowest Mark</h3>
            <p>{lowest}</p>
        </div>
        ''', unsafe_allow_html=True)

else:
    st.info("No students added yet. Use the form above to add one.")