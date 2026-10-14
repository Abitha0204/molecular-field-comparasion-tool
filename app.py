import streamlit as st
from molecule import create_molecule, generate_3d
from field import (
    calculate_electrostatic_field,
    calculate_hydrophobic_field,
    calculate_steric_field
)
from comparison import field_similarity

st.set_page_config(
    page_title="Molecular Field Comparison Tool",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>

    /* Main page */
    .stApp {
        background: #f4f8fc;
    }

    .main {
        padding-top: 2rem;
    }

    /* Header */
    .header {
        background: linear-gradient(135deg, #0b5ed7, #2563eb);
        padding: 30px;
        border-radius: 18px;
        margin-bottom: 28px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.15);
    }

    .header h1 {
        font-size: 34px;
        margin-bottom: 8px;
    }

    .header p {
        font-size: 16px;
        margin: 0;
        opacity: 0.9;
    }

    /* Section title */
    .section-title {
        color: #17365d;
        font-size: 22px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    /* Molecule cards */
    .molecule-card {
        background: white;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #dbe7f3;
        box-shadow: 0 4px 12px rgba(30, 70, 110, 0.06);
        margin-bottom: 15px;
    }

    .molecule-title {
        color: #0b5ed7;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .molecule-description {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 10px;
    }

    /* Compare button */
    div.stButton > button {
        width: 100%;
        background: #0b5ed7;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background: #084db2;
        color: white;
    }

    /* Result cards */
    .result-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #dbe7f3;
        box-shadow: 0 4px 12px rgba(30, 70, 110, 0.06);
    }

    .result-title {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .result-value {
        color: #0b5ed7;
        font-size: 28px;
        font-weight: 700;
    }

    /* Overall result */
    .overall-card {
        background: linear-gradient(135deg, #e8f1ff, #f5f9ff);
        border: 2px solid #9ec5fe;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
    }

    .overall-title {
        color: #17365d;
        font-size: 17px;
        font-weight: 600;
    }

    .overall-value {
        color: #0b5ed7;
        font-size: 42px;
        font-weight: 800;
    }

    /* Info box */
    .info-box {
        background: #eef6ff;
        border-left: 5px solid #0b5ed7;
        padding: 15px;
        border-radius: 8px;
        color: #334155;
        font-size: 14px;
        margin-top: 20px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="header">
    <h1>🧬 Molecular Field Comparison Tool</h1>
    <p>Compare electrostatic, hydrophobic and steric field characteristics of two molecules</p>
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT SECTION ----------------

st.markdown(
    '<div class="section-title">Molecule Input</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="molecule-card">
        <div class="molecule-title">Molecule 1</div>
        <div class="molecule-description">
            Enter the SMILES representation
        </div>
    </div>
    """, unsafe_allow_html=True)

    smiles1 = st.text_input(
        "Molecule 1 SMILES",
        "CCO",
        label_visibility="collapsed"
    )


with col2:

    st.markdown("""
    <div class="molecule-card">
        <div class="molecule-title">Molecule 2</div>
        <div class="molecule-description">
            Enter the SMILES representation
        </div>
    </div>
    """, unsafe_allow_html=True)

    smiles2 = st.text_input(
        "Molecule 2 SMILES",
        "CCCO",
        label_visibility="collapsed"
    )


st.write("")

if st.button("Compare Molecular Fields"):

    mol1 = create_molecule(smiles1)
    mol2 = create_molecule(smiles2)

    if mol1 is None or mol2 is None:

        st.error("Invalid SMILES. Please enter valid molecule structures.")

    else:

        mol1_3d = generate_3d(mol1)
        mol2_3d = generate_3d(mol2)

        # Field calculations

        electrostatic1 = calculate_electrostatic_field(mol1_3d)
        electrostatic2 = calculate_electrostatic_field(mol2_3d)

        hydrophobic1 = calculate_hydrophobic_field(mol1_3d)
        hydrophobic2 = calculate_hydrophobic_field(mol2_3d)

        steric1 = calculate_steric_field(mol1_3d)
        steric2 = calculate_steric_field(mol2_3d)

        # Similarity scores

        electrostatic_score = field_similarity(
            electrostatic1,
            electrostatic2
        )

        hydrophobic_score = field_similarity(
            hydrophobic1,
            hydrophobic2
        )

        steric_score = field_similarity(
            steric1,
            steric2
        )

        overall_score = (
            electrostatic_score
            + hydrophobic_score
            + steric_score
        ) / 3


        # ---------------- MOLECULE INFO ----------------

        st.markdown(
            '<div class="section-title">Molecule Information</div>',
            unsafe_allow_html=True
        )

        info1, info2 = st.columns(2)

        with info1:
            st.info(
                f"Molecule 1: {smiles1}\n\n"
                f"Atoms: {mol1_3d.GetNumAtoms()}"
            )

        with info2:
            st.info(
                f"Molecule 2: {smiles2}\n\n"
                f"Atoms: {mol2_3d.GetNumAtoms()}"
            )


        # ---------------- RESULTS ----------------

        st.markdown(
            '<div class="section-title">Field Similarity Results</div>',
            unsafe_allow_html=True
        )

        r1, r2, r3 = st.columns(3)

        with r1:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-title">Electrostatic Similarity</div>
                <div class="result-value">{electrostatic_score:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-title">Hydrophobic Similarity</div>
                <div class="result-value">{hydrophobic_score:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)

        with r3:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-title">Steric Similarity</div>
                <div class="result-value">{steric_score:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)


        # ---------------- OVERALL ----------------

        st.markdown(f"""
        <div class="overall-card">
            <div class="overall-title">
                Overall Molecular Field Similarity
            </div>
            <div class="overall-value">
                {overall_score:.2f}%
            </div>
        </div>
        """, unsafe_allow_html=True)


        # ---------------- NOTE ----------------

        st.markdown("""
        <div class="info-box">
            <b>Note:</b> The similarity percentage represents a
            computational comparison of molecular field characteristics.
            It is not a prediction of biological activity or drug effectiveness.
        </div>
        """, unsafe_allow_html=True)
