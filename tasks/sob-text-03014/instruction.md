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
Aerangis gracillima: Aerangis gracillima is a species of plant in the Orchidaceae family.  It is found in Cameroon and Gabon.  Its natural habitat is subtropical or tropical dry forests.

Gillenia trifoliata: Gillenia trifoliata (common names Bowman's root and Indian physic) is a species of flowering plant in the Rosaceae family, native to eastern North America from Ontario to Georgia.  It is an erect herbaceous perennial growing to 100 cm tall by 60 cm wide, with 3-palmate leaves and pale pink flowers with narrow petals and reddish calyces above red coloured stems in spring and summer.

Gillenia: Gillenia (syn.  "Porteranthus") is a genus of two species of perennial herbs in the Rosaceae family.  Common names for plants in this genus include: Bowman's root, Indian-physic, American ipecac.  This genus is endemic to dry open woods with acidic soils in eastern North America.  Both plants are subshrubs with exposed semi-woody branches and serrated leaves; the larger lower leaves are divided into palmately arranged leaflets.  Plants bloom in May, June, or July; blooms are composed of five slender white petals which are loosely arranged and typically appear slightly twisted and limp as if they were wilted.  The flowers mature into small capsules.  These plants are often planted as ornamentals and used in herbal medicine.

Aerangis: Aerangis, abbreviated as Aergs in horticultural trade, is a genus of the Orchid family (Orchidaceae).  The name of this genus has been derived from the Greek words 'aer' (air) and 'angos' (urn), referring to the form of the lip.  It is the type genus of the subtribe Aerangidinae.  Approximately 50 species in this genus are known mostly from tropical Africa, but also from the Comoro Islands, Madagascar and Sri Lanka.

Question: What plant has more species, Aerangis or Gillenia?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genus_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "species_count": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "species_count"
      ],
      "additionalProperties": false
    },
    "genus_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "species_count": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "species_count"
      ],
      "additionalProperties": false
    },
    "genus_with_more_species": {
      "type": "string"
    },
    "comparison_summary": {
      "type": "string"
    }
  },
  "required": [
    "genus_a",
    "genus_b",
    "genus_with_more_species",
    "comparison_summary"
  ],
  "additionalProperties": false
}
