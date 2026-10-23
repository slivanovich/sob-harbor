{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHardenbergia: Hardenbergia is a small genus of leguminous vines from Australia.\n\nChrysogonum: Chrysogonum is a genus of flowering plants in the daisy family.  The plants are terrestrial herbs with yellow flower heads containing both disc florets and ray florets.\n\nStyphnolobium: Styphnolobium is a small genus of three or four species of small trees and shrubs in the subfamily Faboideae of the pea family Fabaceae, formerly included within a broader interpretation of the genus \"Sophora\".  It was recently assigned to the unranked, monophyletic \"Cladrastis\" clade.  They differ from the genus \"Calia\" (mescalbeans) in having deciduous leaves and flowers in axillary, not terminal, racemes.  The leaves are pinnate, with 9–21 leaflets, and the flowers in pendulous racemes similar to those of the black locust.  Necklacepod is a common name for plants in this genus.\n\nAcacia cincinnata: Acacia cincinnata, also known as the Daintree wattle, is a species of leguminous trees of the plant family Fabaceae, found naturally in north eastern Queensland.\n\nGeoffroea: Geoffroea is a rather small genus of wild spiny shrubs or small trees of tropical and subtropical South America.  Although it gathers few species, they are highly extended geographically throughout the subcontinent.  Each species is well known in its local area, as seen from the varied (and mostly domestic) usage of these trees as food, timber, or fuel.  It was recently assigned to the informal monophyletic \"Pterocarpus\" clade within the Dalbergieae.\n\nClover: Clover or trefoil are common names for plants of the genus Trifolium (Latin, \"tres\" \"three\" + \"folium\" \"leaf\"), consisting of about 300 species of plants in the leguminous pea family Fabaceae.  The genus has a cosmopolitan distribution; the highest diversity is found in the temperate Northern Hemisphere, but many species also occur in South America and Africa, including at high altitudes on mountains in the tropics.  They are small annual, biennial, or short-lived perennial herbaceous plants.  Clover can be evergreen.  The leaves are trifoliate (rarely quatrefoiled (Four-leaf clover), cinquefoil, or septfoil), with stipules adnate to the leaf-stalk, and heads or dense spikes of small red, purple, white, or yellow flowers; the small, few-seeded pods are enclosed in the calyx.  Other closely related genera often called clovers include \"Melilotus\" (sweet clover) and \"Medicago\" (alfalfa or Calvary clover).\n\nGymnocladus: Gymnocladus (Neo-Latin, from Greek γυμνὀς, \"gymnos\", naked + κλάδος, \"klados\", branch) is a small genus of leguminous trees.  The common name coffeetree is used for this genus.\n\nCopaiba: Copaiba is a stimulant oleoresin obtained from the trunk of several pinnate-leaved South American leguminous trees (genus \"Copaifera\").  The thick, transparent exudate varies in color from light gold to dark brown, depending on the ratio of resin to essential oil.  Copaiba is used in making varnishes and lacquers.\n\nMesquite: Mesquite is the common name for the genus \"Prosopis\", containing over 40 species of small leguminous trees.  They are native to the southwestern United States and Mexico (even the creeping mesquite, which is invasive in southern California).\n\nBauhinia monandra: Bauhinia monandra is a species of leguminous trees, of the Fabaceae family.  Common names include pink bauhinia, orchid tree, and Napoleon’s plume.  Naturally they grow in Madagascar, but have naturalised in Burma, Australia, Christmas Island, the Caribbean, southern USA and the Pacific Islands.\n\nQuestion: While  Gymnocladus is a small genus of leguminous trees, what genus is Chrysogonum?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"plant_genus_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the plant genus.\"\n    },\n    \"plant_type_description\": {\n      \"type\": \"string\",\n      \"description\": \"A general description of the plant type for the genus.\"\n    },\n    \"family\": {\n      \"type\": \"string\",\n      \"description\": \"The plant family to which the genus belongs.\"\n    }\n  },\n  \"required\": [\n    \"plant_genus_name\",\n    \"plant_type_description\",\n    \"family\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "plant_genus_name": {
        "type": "string",
        "description": "The name of the plant genus."
      },
      "plant_type_description": {
        "type": "string",
        "description": "A general description of the plant type for the genus."
      },
      "family": {
        "type": "string",
        "description": "The plant family to which the genus belongs."
      }
    },
    "required": [
      "plant_genus_name",
      "plant_type_description",
      "family"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
