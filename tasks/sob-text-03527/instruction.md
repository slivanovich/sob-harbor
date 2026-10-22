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
Astilboides: Astilboides, a genus of the saxifrage family containing only one species, a herbaceous perennial once included in the genus Rodgersia.  It comes from China and differs from its former relatives mainly in its leaf shape.  It is grown for its huge bright green, circular leaves to 36 in (90 cm) across with the stem attached to the center, and large fluffy racemes of tiny white flowers produced in summer.

Callicarpa bodinieri: Callicarpa bodinieri (Bodinier's beautyberry) is a species of flowering plant in the genus "Callicarpa" of the family Lamiaceae, native to West and Central China.  Growing to 3 m tall by 2.5 m wide, it is an upright deciduous shrub with dark green leaves turning red in autumn (fall).  In midsummer, small lilac flowers are produced in the leaf axils.  But it is grown in gardens primarily for its small, decorative purple berries in tight clusters in autumn.  While the berries are not poisonous, they are very bitter.  Wildlife will not eat them until there are no other available food sources.  This species is more tolerant of cold than "C. americana" (American beautyberry).

Callicarpa tomentosa: Callicarpa tomentosa is a species of beautyberry plant in the Lamiaceae family.  It is found in Western Ghats of India and Sri Lanka.  It is a small tree with about 5m tall.  Leaves simple, opposite; elliptic to broadly elliptic; apex acute or acuminate.  Purplish flowers show branched axillary cymes.  Fruit is 3-4 seeded globose drupe.  Fruits provide food for wildlife.  They are sometimes used to make herbal medicine.  The leaves are also food for wildlife.

Callicarpa: Callicarpa (beautyberry) is a genus of shrubs and small trees in the family Lamiaceae.  They are native to east and southeast Asia (where the majority of the species occur), Australia, Madagascar, southeast North America and South America.

Idiophantis callicarpa: Idiophantis callicarpa is a moth of the Gelechiidae family.  It was described by Meyrick in 1927.  It is found on Samoa.

Callicarpa ampla: Callicarpa ampla, also called the capa rose, is a species of plant in the Lamiaceae family.  It is found in Puerto Rico in the Caribbean region.  It is threatened by habitat loss and is a critically endangered plant species.

Endoclita undulifer: Endoclita undulifer is a species of moth of the family Hepialidae.  It is known from India.  Food plants for this species include "Alnus", "Byttneria", "Callicarpa", "Cryptomeria", "Eucalyptus", and "Gmelina".

Callicarpa maingayi: Callicarpa maingayi is a species of beautyberry plant in the Lamiaceae family.  It is found in Malaysia and Singapore.

Question: Are Astilboides and Callicarpa in the same family?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plant_genus_1": {
      "type": "string",
      "description": "The name of the first plant genus."
    },
    "plant_genus_1_family": {
      "type": "string",
      "description": "The family of the first plant genus."
    },
    "plant_genus_2": {
      "type": "string",
      "description": "The name of the second plant genus."
    },
    "plant_genus_2_family": {
      "type": "string",
      "description": "The family of the second plant genus."
    },
    "are_in_same_family": {
      "type": "boolean",
      "description": "True if both plant genera belong to the same family, false otherwise."
    }
  },
  "required": [
    "plant_genus_1",
    "plant_genus_1_family",
    "plant_genus_2",
    "plant_genus_2_family",
    "are_in_same_family"
  ],
  "additionalProperties": false
}
