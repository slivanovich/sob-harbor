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
Phenyl-2-nitropropene: Phenyl-2-nitropropene is a chemical compound with the chemical formula is CHNO.  It can be produced by the reaction of benzaldehyde and nitroethane in the presence of a basic catalyst.  In this reaction, the base deprotonates nitroethane to form a resonance stabilized anion.  This anion nucleophilically adds to the aldehyde forming a beta nitro alcohol, which is subsequently dehydrated to yield the nitroalkene.  This reaction is known as a nitroaldol reaction.  Phenyl-2-nitropropene is used to make pharmaceuticals.  It is used in pharmaceutical industry to manufacture drug Adderall, an amphetamine mixture, which is used to treat ADHD and narcolepsy.

Sodium ferrocyanide: Sodium ferrocyanide is the sodium salt of the coordination compound of formula [Fe(CN)].  In its hydrous form, NaFe(CN)·10HO (sodium ferrocyanide decahydrate), it is sometimes known as yellow prussiate of soda.  It is a yellow crystalline solid that is soluble in water and insoluble in alcohol.  The yellow color is the color of ferrocyanide anion.  Despite the presence of the cyanide ligands, sodium ferrocyanide has low toxicity (acceptable daily intake 0–0.025 mg/kg body weight).  The ferrocyanides are less toxic than many salts of cyanide, because they tend not to release free cyanide.  However, like all ferrocyanide salt solutions, addition of an acid can result in the production of hydrogen cyanide gas, which is toxic.

Potassium ferrocyanide: Potassium ferrocyanide is the inorganic compound with formula K[Fe(CN)] · 3HO.  It is the potassium salt of the coordination complex [Fe(CN)].  This salt forms lemon-yellow monoclinic crystals.

Hexafluorophosphate: Hexafluorophosphate is an anion with chemical formula of PF6- .  This octahedral species is isoelectronic with sulfur hexafluoride, SF, and the hexafluorosilicate dianion, SiF, and is valence isoelectronic with the highly stable superacid anion fluoroantimonate SbF6- .  As a non-coordinating anion, it is a poor nucleophile.  It is prone to decomposition with the release of hydrogen fluoride in ionic liquids but is generally extremely stable in solution.  Hydrolysis to the phosphate ion is very slow even in concentrated acid with warming, and even slower under basic conditions.

Fluoride: Fluoride , is an inorganic, monatomic anion of fluorine with the chemical formula F− .  Fluoride is the simplest anion of fluorine.  Its salts and minerals are important chemical reagents and industrial chemicals, mainly used in the production of hydrogen fluoride for fluorocarbons.  In terms of charge and size, the fluoride ion resembles the hydroxide ion.  Fluoride ions occur on earth in several minerals, particularly fluorite, but are only present in trace quantities in water.  Fluoride contributes a distinctive bitter taste.  It contributes no color to fluoride salts.

Superoxide: A superoxide, also known as hyperoxide, is a compound that contains the superoxide anion with the chemical formula O2- .  The systematic name of the anion is dioxide(1−).  The reactive oxygen anion superoxide is particularly important as the product of the one-electron reduction of dioxygen O, which occurs widely in nature.  Whereas molecular oxygen (dioxygen) is a diradical containing two unpaired electrons, the addition of a second electron fills one of its two degenerate molecular orbitals, leaving a charged ionic species with single unpaired electron and a net negative charge of −1.  Both dioxygen and the superoxide anion are free radicals that exhibit paramagnetism.

Ferrocyanide: Ferrocyanide is the name of the anion [Fe(CN)].  Salts of this coordination complex give yellow solutions.  It is usually available as the salt potassium ferrocyanide, which has the formula KFe(CN).  [Fe(CN)] is a diamagnetic species, featuring low-spin iron(II) center in an octahedral ligand environment.  Although many salts of cyanide are highly toxic, ferro- and ferricyanides are less toxic because they tend not to release free cyanide.  It is of commercial interest as a precursor to the pigment Prussian blue and, as its potassium salt, an anticaking agent.

Chrysotile: Chrysotile or white asbestos is the most commonly encountered form of asbestos, accounting for approximately 95% of the asbestos in the United States and a similar proportion in other countries.  It is a soft, fibrous silicate mineral in the serpentine subgroup of phyllosilicates; as such, it is distinct from other asbestiform minerals in the amphibole group.  Its idealized chemical formula is Mg (Si O )(OH) .  The material has physical properties which make it desirable for inclusion in building materials, but poses serious health risks when dispersed into air and inhaled.

Prussian blue: Prussian blue is a dark blue pigment with the idealized chemical formula Fe7(CN)18 .  To better understand the binding situation in this complex compound the formula can also be written as Fe4[Fe(CN)6]3 · "x"H2O .  Another name for the color is Berlin blue or, in painting, Parisian or Paris blue.  Turnbull's blue is the same substance, but is made from different reagents, and its slightly different color stems from different impurities.

Tetrakis(3,5-bis(trifluoromethyl)phenyl)borate: Tetrakis[3,5-bis(trifluoromethyl)phenyl]borate is an anion with chemical formula [{3,5-(CF)CH}B], which is commonly abbreviated as [BAr] as the boron atom (B) is surrounded by four fluorinated aryl (Ar) groups.  It is sometimes referred to as "Kobayashi's anion" in honour of Hiroshi Kobayashi who led the team that first synthesised it, but more commonly it is affectionately nicknamed "BARF."  BARF has a tetrahedral geometry around the central boron atom but each of the four surrounding aryl groups is aromatic and planar.  The motivation for its preparation was the search for an anion which coordinates more weakly than the then-available ions hexafluorophosphate, tetrafluoroborate, or perchlorate.  Salts of this anion are known as solids and in both aqueous and non-aqueous solutions.  BARF can be used in catalytic systems where the active site requires an anion which will not coordinate to the metal centre and interfere with the catalytic cycle, such as in the preparation of polyketones.

Question: Ferrocyanide is the name of the anion [Fe(CN)], it is the commercial interest as a precursor to the pigment with what idealized chemical formula?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "anion_name": {
      "type": "string",
      "description": "The name of the anion."
    },
    "anion_formula": {
      "type": "string",
      "description": "The chemical formula of the anion."
    },
    "precursor_to_pigment_name": {
      "type": "string",
      "description": "The name of the pigment that the anion is a precursor to."
    },
    "pigment_idealized_chemical_formula": {
      "type": "string",
      "description": "The idealized chemical formula of the pigment."
    }
  },
  "required": [
    "anion_name",
    "anion_formula",
    "precursor_to_pigment_name",
    "pigment_idealized_chemical_formula"
  ],
  "additionalProperties": false
}
