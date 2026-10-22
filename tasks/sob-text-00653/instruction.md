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
Moringa oleifera: Moringa oleifera is the most widely cultivated species of the genus "Moringa", which is the only genus in the family Moringaceae.  English common names include: moringa, drumstick tree (from the appearance of the long, slender, triangular seed-pods), horseradish tree (from the taste of the roots, which resembles horseradish), ben oil tree, or benzoil tree (from the oil which is derived from the seeds).  It is a fast-growing, drought-resistant tree, native to the southern foothills of the Himalayas in northwestern India, and widely cultivated in tropical and subtropical areas where its young seed pods and leaves are used as vegetables.  It can also be used for water purification and hand washing, and is sometimes used in herbal medicine.

Nautilocalyx: Nautilocalyx is a genus of plant in family Gesneriaceae.

Psaronius: Psaronius was a Marattialean tree fern which grew to 10m in height, and is associated with leaves of the organ genus "Pecopteris" and other extinct tree ferns.  Originally, "Psaronius" was a name for the petrified stems, but today the genus is used for the entire tree fern.  "Psaronius" tree fern fossils are found from the Carboniferous through the Permian.

Gymnocladus: Gymnocladus (Neo-Latin, from Greek γυμνὀς, "gymnos", naked + κλάδος, "klados", branch) is a small genus of leguminous trees.  The common name coffeetree is used for this genus.

Australian green tree frog: The Australian green tree frog, simply green tree frog in Australia, White's tree frog, or dumpy tree frog ("Litoria caerulea") is a species of tree frog native to Australia and New Guinea, with introduced populations in the United States and New Zealand, though the latter is believed to have died out.  The species belongs to the genus "Litoria".  It is morphologically similar to some other members of the genus, particularly the magnificent tree frog ("L. splendida") and the white-lipped tree frog ("L. infrafrenata").

Tree fern: The tree ferns are the ferns that grow with a trunk elevating the fronds above ground level.  Most tree ferns are members of the "core tree ferns", belonging to the families Dicksoniaceae, Metaxyaceae, and Cibotiaceae in the order Cyatheales.  In addition to those families, many ferns in other groups may be considered tree ferns, such as several ferns in the family Osmundaceae, which can achieve short trunks under a metre tall, and particularly ferns in the genus "Cibotium", which can grow ten metres tall.  Fern species with short trunks in the genera "Blechnum, Calochleana, Cnemedaria, Culcita" (Europe's only tree fern), "Cystodium, Leptopteris, Lophosoria, Sadleria, Thyrsopteris" and "Todea" could also be considered tree ferns in a liberal interpretation of the term.

Gymnocladus chinensis: Gymnocladus chinensis, the soap tree or Chinese coffeetree, is a tree in the subfamily Caesalpinioideae of the pea family Fabaceae, native to central China.  It grows slowly and is apparently extremely rare.  The leaves have huge bipinnate leaves starting purple then shading to green.

Cajeput tree: Cajeput tree is a common name used for certain classification of tree that has a white spongy bark that is flexible and can easily flake off the trunk.  The Cajeput tree is of the genus "Melaleuca", native to Australia and is commonly known in North America as the Tea Tree.  The name "Cajeput tree" is primarily used for the species "M. cajuputi", "M. leucadendra", "M. linariifolia", "M. viridiflora" and "M. quinquenervia".  Other names for these trees are the paperbark tree, punk tree, or the white bottle brush tree.  Similar subtropical trees from the eucalyptus family are evergreens with pointed leaves and white, red or green flowers.  Aborigines of Australia often used the cajeput tree bark for shields, canoes, roofing material and timber.

Kentucky coffeetree: The Kentucky coffeetree, Gymnocladus dioicus, is a tree in the subfamily Caesalpinioideae of the pea family Fabaceae, native to the Midwest and Upper South of North America.  The seed may be roasted and used as a substitute for coffee beans; however, unroasted pods and seeds are toxic.  The wood from the tree is used by cabinetmakers and carpenters.

Cyclorana: Cyclorana is a genus of frogs in the family Hylidae (tree frogs), whose members are found in most of Australia.  It was formerly considered a separate genus, but reclassified following a major revision by Frost et al. in 2006.  Although classified as tree frogs, this genus is entirely terrestrial and lacks toe pads which their arboreal relatives use for climbing.  They are classified as tree frogs because of their similarity with the other members of the genus "Litoria" in terms of skeletal structure and physical resemblance of the tadpoles.

Question: Which is a genus of tree, Gymnocladus or Nautilocalyx?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_genus_options": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genera presented in the question for comparison."
    },
    "identified_tree_genus": {
      "type": "string",
      "description": "The genus identified as a tree."
    },
    "identified_tree_genus_description": {
      "type": "string",
      "description": "A description of the identified tree genus from the context."
    },
    "other_genus_name": {
      "type": "string",
      "description": "The name of the other genus mentioned in the question."
    },
    "other_genus_description": {
      "type": "string",
      "description": "A description of the other genus from the context, indicating it is not a tree."
    }
  },
  "required": [
    "question_genus_options",
    "identified_tree_genus",
    "identified_tree_genus_description",
    "other_genus_name",
    "other_genus_description"
  ],
  "additionalProperties": false
}
