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
Solvent: A solvent (from the Latin "solvō", "loosen, untie, solve") is a substance that dissolves a solute (a chemically distinct liquid, solid or gas), resulting in a solution.  A solvent is usually a liquid but can also be a solid, a gas, or a supercritical fluid.  The quantity of solute that can dissolve in a specific volume of solvent varies with temperature.  Common uses for organic solvents are in dry cleaning (e.g. tetrachloroethylene), as paint thinners (e.g. toluene, turpentine), as nail polish removers and glue solvents (acetone, methyl acetate, ethyl acetate), in spot removers (e.g. hexane, petrol ether), in detergents (citrus terpenes) and in perfumes (ethanol).  Water is a solvent for polar molecules and the most common solvent used by living things; all the ions and proteins in a cell are dissolved in water within a cell.  Solvents find various applications in chemical, pharmaceutical, oil, and gas industries, including in chemical syntheses and purification processes.

Methanol fuel: Methanol is an alternative fuel for internal combustion and other engines, either in combination with gasoline or directly ("neat").  It is used in racing cars in many countries.  In the U.S., methanol fuel has received less attention than ethanol fuel as an alternative to petroleum-based fuels.  In general, ethanol is less toxic and has higher energy density, although methanol is less expensive to produce sustainably and is a less expensive way to reduce the carbon footprint.  However, for optimizing engine performance, fuel availability, toxicity and political advantage, a blend of ethanol, methanol and petroleum is likely to be preferable to using any of these individual substances alone .  Methanol may be made from hydrocarbon or renewable resources, in particular natural gas and biomass respectively.  It can also be synthesized from CO (carbon dioxide) and hydrogen.

Svensk Etanolkemi: The company Svensk Etanolkemi AB, or Sekab is a major Nordic producer of ethanol, ethanol derivatives such as acetic acid and ethyl acetate, and ethanol fuels such as E85.  They are located in Örnsköldsvik in middle Sweden, and are owned by NEAB, a regional private consortium.

Isochrysis galbana: Isochrysis galbana is a species of haptophytes.  It is the type species of the genus "Isochrysis".  It is an outstanding food for various bivalve larvae.  and is now widely cultured for use in the bivalve aquaculture industry.  This unicellular is investigated for its high amount of Fucoxanthin (18.23 mg/g dried sample).  The "Isochrysis galbana" extract is said to have certain cosmetic and hair-growth properties when using hexane, ethyl acetate, ethanol, water, methanol, or isopropanol as extractants.

Methyl acetate: Methyl acetate, also known as MeOAc, acetic acid methyl ester or methyl ethanoate, is a carboxylate ester with the formula CHCOOCH.  It is a flammable liquid with a characteristically pleasant smell reminiscent of some glues and nail polish removers.  Methyl acetate is occasionally used as a solvent, being weakly polar and lipophilic, but its close relative ethyl acetate is a more common solvent being less toxic and less soluble in water.  Methyl acetate has a solubility of 25% in water at room temperature.  At elevated temperature its solubility in water is much higher.  Methyl acetate is not stable in the presence of strong aqueous bases or aqueous acids. Methyl acetate is not considered as a VOC.

2-Ethoxyethanol: 2-Ethoxyethanol, also known by the trademark Cellosolve or ethyl cellosolve, is a solvent used widely in commercial and industrial applications.  It is a clear, colorless, nearly odorless liquid that is miscible with water, ethanol, diethyl ether, acetone, and ethyl acetate.

Ethyl acetate: Ethyl acetate (systematically ethyl ethanoate, commonly abbreviated EtOAc or EA) is the organic compound with the formula CH−COO−CH−CH, simplified to CHO.  This colorless liquid has a characteristic sweet smell (similar to pear drops) and is used in glues, nail polish removers, decaffeinating tea and coffee, and cigarettes (see list of additives in cigarettes).  Ethyl acetate is the ester of ethanol and acetic acid; it is manufactured on a large scale for use as a solvent.  The combined annual production in 1985 of Japan, North America, and Europe was about 400,000 tonnes.  In 2004, an estimated 1.3 million tonnes were produced worldwide.

Swedish ethyl acetate method: The Swedish ethyl acetate method (SweEt) is a method for chemical analysis of pesticide residues in food using ethyl acetate as an extraction medium followed by analysis with liquid chromatography-tandem mass spectrometry (LC-MS/MS) and gas chromatography-tandem mass spectrometry (GC-MS/MS).  It was developed by the Swedish National Food Agency (National Reference Laboratory for pesticide analysis) for quantitative analysis of over 500 pesticides in fruits, vegetables, cereals and products of animal origin.

Isopropyl alcohol: Isopropyl alcohol (IUPAC name propan-2-ol), also called dimethyl carbinol or, incorrectly, isopropanol, is a compound with the chemical formula CHO or CHOH or CHCHOHCH (sometimes represented as "i"-PrOH).  It is a colorless, flammable chemical compound with a strong odor.  As a propyl group linked to a hydroxyl group, it is the simplest example of a secondary alcohol, where the alcohol carbon atom is attached to two other carbon atoms, sometimes shown as (CH)CHOH.  It is a structural isomer of 1-propanol.  It has a wide variety of industrial and household uses, and is a common ingredient in chemicals such as antiseptics, disinfectants and detergents.

Nonactin: Nonactin is a member of a family of naturally occurring cyclic ionophores known as the macrotetrolide antibiotics.  The other members of this homologous family are monactin, dinactin, trinactin and tetranactin which are all neutral ionophoric substances and higher homologs of nonactin.  Collectively, this class is known as the nactins. Nonactin is soluble in methanol, dichloromethane, ethyl acetate and DMSO, but insoluble in water.

Question: What extract is said to have certain cosmetic and hair-growth properties when using hexane, ethyl acetate, ethanol, water, methanol, or dimethyl carbinol as extractants?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "extract_name": {
      "type": "string",
      "description": "The name of the extract that possesses the specified properties."
    },
    "attributed_properties": {
      "type": "array",
      "description": "A list of properties attributed to the extract.",
      "items": {
        "type": "string"
      }
    },
    "extractants_used": {
      "type": "array",
      "description": "A list of substances used as extractants to obtain these properties.",
      "items": {
        "type": "string"
      }
    },
    "extractant_aliases_mentioned": {
      "type": "array",
      "description": "A list of aliases for extractants mentioned in the question, mapping to their primary name used in the context.",
      "items": {
        "type": "object",
        "properties": {
          "alias": {
            "type": "string",
            "description": "The alias name used in the question."
          },
          "primary_name": {
            "type": "string",
            "description": "The primary name of the substance as found in the context."
          }
        },
        "required": [
          "alias",
          "primary_name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "extract_name",
    "attributed_properties",
    "extractants_used",
    "extractant_aliases_mentioned"
  ],
  "additionalProperties": false
}
