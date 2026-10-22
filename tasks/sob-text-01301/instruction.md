Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Protein structure: Protein structure is the three-dimensional arrangement of atoms in a protein molecule.  Proteins are polymers — specifically polypeptides — formed from sequences of amino acids, the monomers of the polymer.  A single amino acid monomer may also be called a residue indicating a repeating unit of a polymer.  Proteins form by amino acids undergoing condensation reactions, in which the amino acids lose one water molecule per reaction in order to attach to one another with a peptide bond.  By convention, a chain under 30 amino acids is often identified as a peptide, rather than a protein.  To be able to perform their biological function, proteins fold into one or more specific spatial conformations driven by a number of non-covalent interactions such as hydrogen bonding, ionic interactions, Van der Waals forces, and hydrophobic packing.  To understand the functions of proteins at a molecular level, it is often necessary to determine their three-dimensional structure.  This is the topic of the scientific field of structural biology, which employs techniques such as X-ray crystallography, NMR spectroscopy, and dual polarisation interferometry to determine the structure of proteins.

Edotreotide: Edotreotide (USAN, codenamed SMT487, also known as (DOTA-Phe-Tyr)octreotide, or DOTATOC) is a substance which, when bound to various radionuclides, is used in the treatment and diagnosis of certain types of cancer.

Aspartic acid: Aspartic acid (abbreviated as Asp or D; encoded by the codons [GAU and GAC]), also known as aspartate, is an α-amino acid that is used in the biosynthesis of proteins.  Similar to all other amino acids it contains an amino group and a carboxylic acid.  Its α-amino group is in the protonated –NH form under physiological conditions, while its α-carboxylic acid group is deprotonated −COO under physiological conditions.  Aspartic acid has an acidic side chain (CHCOOH) which reacts with other amino acids, enzymes and proteins in the body.  Under physiological conditions (pH 7.4) in proteins the side chain usually occurs as the negatively charged aspartate form, −COO .  It is a non-essential amino acid in humans, meaning the body can synthesize it as needed.

Amino acid: Amino acids are organic compounds containing amine (-NH) and carboxyl (-COOH) functional groups, along with a side chain (R group) specific to each amino acid.  The key elements of an amino acid are carbon, hydrogen, oxygen, and nitrogen, although other elements are found in the side chains of certain amino acids.  About 500 amino acids are known (though only 20 appear in the genetic code) and can be classified in many ways.  They can be classified according to the core structural functional groups' locations as alpha- (α-), beta- (β-), gamma- (γ-) or delta- (δ-) amino acids; other categories relate to polarity, pH level, and side chain group type (aliphatic, acyclic, aromatic, containing hydroxyl or sulfur, etc.).  In the form of proteins, amino acid residues form the second-largest component (water is the largest) of human muscles and other tissues.  Beyond their role as residues in proteins, amino acids participate in a number of processes such as neurotransmitter transport and biosynthesis.

BLOSUM: In bioinformatics, the BLOSUM (BLOcks SUbstitution Matrix) matrix is a substitution matrix used for sequence alignment of proteins. BLOSUM matrices are used to score alignments between evolutionarily divergent protein sequences.  They are based on local alignments.  BLOSUM matrices were first introduced in a paper by Steven Henikoff and Jorja Henikoff.  They scanned the BLOCKS database for very conserved regions of protein families (that do not have gaps in the sequence alignment) and then counted the relative frequencies of amino acids and their substitution probabilities.  Then, they calculated a log-odds score for each of the 210 possible substitution pairs of the 20 standard amino acids.  All BLOSUM matrices are based on observed alignments; they are not extrapolated from comparisons of closely related proteins like the PAM Matrices.

Amino acid synthesis: Amino acid synthesis is the set of biochemical processes (metabolic pathways) by which the various amino acids are produced from other compounds.  The substrates for these processes are various compounds in the organism's diet or growth media.  Not all organisms are able to synthesize all amino acids.  Humans are an excellent example of this, since humans can only synthesize 11 of the 20 standard amino acids (a.k.a. non-essential amino acid), and in time of accelerated growth, histidine, can be considered an essential amino acid.

Adaptor complexes medium subunit domain: In molecular biology, the adaptor complexes medium subunit domain is a protein domain found at the C-terminus of the mu subunit from various clathrin adaptor protein complexes (AP1, AP2, AP3, AP4 and AP5) and muniscins.  The C-terminal domain has an immunoglobulin-like beta-sandwich fold consisting of 9 strands in 2 sheets with a Greek key topology, similar to that found in cytochrome f and certain transcription factors.  The mu subunit regulates the coupling of clathrin lattices with particular membrane proteins by self-phosphorylation via a mechanism that is still unclear.  The mu subunit possesses a highly conserved N-terminal domain of around 230 amino acids, which may be the region of interaction with other AP proteins; a linker region of between 10 and 42 amino acids; and a less well-conserved C-terminal domain of around 190 amino acids, which may be the site of specific interaction with the protein being transported in the vesicle.

Tyrosine: Tyrosine (Tyr or Y) or 4-hydroxyphenylalanine is one of the 20 standard amino acids that are used by cells to synthesize proteins.  It is a non-essential amino acid with a polar side group.  Its codons are UAC and UAU.  The word "tyrosine" is from the Greek "tyros", meaning "cheese", as it was first discovered in 1846 by German chemist Justus von Liebig in the protein casein from cheese.  It is called tyrosyl when referred to as a functional group or side chain.  Tyrosine is a hydrophilic amino acid and is significantly more soluble in water than its precursor, phenylalanine, due to the thermodynamic favorability of the hydrogen bonding between the hydroxyl group of one molecule of tyrosine and the carboxyl group of another.

Ion chromatography: Ion chromatography (or ion-exchange chromatography) is a chromatography process that separates ions and polar molecules based on their affinity to the ion exchanger.  It works on almost any kind of charged molecule—including large proteins, small nucleotides, and amino acids.  The two types of ion chromatography are anion-exchange and cation-exchange.  It is often used in protein purification, water analysis, and quality control.  The water-soluble and charged molecules such as proteins, amino acids, and peptides bind to moieties which are oppositely charged by forming ionic bonds to the insoluble stationary phase.  The equilibrated stationary phase consists of an ionizable functional group where the targeted molecules of a mixture to be separated and quantified can bind while passing through the column—a cationic stationary phase is used to separate anions and an anionic stationary phase is used to separate cations.  Cation exchange chromatography is used when the desired molecules to separate are cations and anion exchange chromatography is used to separate anions.  The bound molecules then can be eluted and collected using an eluant which contains anions and cations by running higher concentration of ions through the column or changing pH of the column.  One of the primary advantages for the use of ion chromatography is only one interaction involved during the separation as opposed to other separation techniques; therefore, ion chromatography may have higher matrix tolerance.  However, there are also disadvantages involved when performing ion-exchange chromatography, such as constant evolution with the technique which leads to the inconsistency from column to column.

Phosphomimetics: Phosphomimetics are amino acid substitutions that mimic a phosphorylated protein, thereby activating (or deactivating) the protein.  Within cells, proteins are commonly modified at serine, tyrosine and threonine amino acids by adding a phosphate group.  Phosphorylation is a common mode of activating or deactivating a protein as a form of regulation.  However some non-phosphorylated amino acids appear chemically similar to phosphorylated amino acids.  Therefore, by replacing an amino acid, the protein may maintain a higher level of activity.  For example, aspartic acid is chemically similar to phospho-serine.  Therefore, when an aspartic acid replaces a serine, it is a phosphomimetic of phospho-serine and can make the protein always in its phosphorylated form.

Question: What is the other name for a subastance , when bound to various radionuclides, is used in the treatment and diagnosis of certain types of cancer, and  is one of the 20 standard amino acids that are used by cells to synthesize proteins?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "substance_identified": {
      "type": "string",
      "description": "The primary name of the substance that fits the description."
    },
    "other_name_for_substance": {
      "type": "string",
      "description": "Another name or synonym for the identified substance."
    },
    "is_standard_amino_acid": {
      "type": "boolean",
      "description": "Indicates if the substance is one of the 20 standard amino acids used by cells to synthesize proteins."
    },
    "is_part_of_cancer_treatment_compound": {
      "type": "boolean",
      "description": "Indicates if the substance is a component of a larger compound used in cancer treatment and diagnosis."
    },
    "cancer_treatment_compound_details": {
      "type": "object",
      "properties": {
        "compound_name": {
          "type": "string",
          "description": "The name of the larger compound used in cancer treatment and diagnosis."
        },
        "compound_aliases": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other names or codenames for the cancer treatment compound."
        },
        "compound_use": {
          "type": "string",
          "description": "The specific use of the compound in cancer treatment/diagnosis when bound to radionuclides."
        }
      },
      "required": [
        "compound_name",
        "compound_aliases",
        "compound_use"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "substance_identified",
    "other_name_for_substance",
    "is_standard_amino_acid",
    "is_part_of_cancer_treatment_compound",
    "cancer_treatment_compound_details"
  ],
  "additionalProperties": false
}
