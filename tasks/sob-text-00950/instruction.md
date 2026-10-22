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
Sporisorium sorghi: Sporisorium sorghi is a species of fungus in the Ustilaginaceae family.  It is a plant pathogen, causing covered smut of "sorghum" spp.  such as "Sorghum bicolor" ("S. vulgare") (sorghum), "S. sudanense" (Sudan grass), "S. halepense" (Johnson grass) and "Sorghum" "vulgare" var.  "technichum" (broomcorn).

Nepalese sorghum: Sorghum (Sorghum bicolor) comes from the Latin name “Syrucum (granum)” which means “grain of Syria” however it originated in eastern Africa.  Sorghum is an important species of the grass family, Paceae, and is considered the world’s fifth most important cereal crop.  There are many diverse and wild types of Sorghum, however there are seven basic races, the most common in Asia are Durra and Sballu.  Sorghum is an important staple crop for more than 500 million people in sub-Saharan Africa and South Asia, including many people in Nepal.  Sorghum is grown on more than 48 ha area around the world.  In statistics collected from 1992-1994 about general millet, Nepal had an area of 0.21 million ha, with a yield rate of 1.14 (t/ha), and produced around 0.24 million tons of Sorghum.  The entirety of the crop is highly valued, both the grain and the stem are very useful.  Sorghum can be cooked in many different ways for food with a high nutritional content, among many other uses.  Overall Sorghum is a very important crop worldwide.

Phaseolus vulgaris: Phaseolus vulgaris, the common bean (also known as the string bean, field bean, flageolet bean, French bean, garden bean, green bean, haricot bean, pop bean, snap bean, or snap), is a herbaceous annual plant grown worldwide for its edible dry seed (known as just "beans") or unripe fruit (green beans).  The main categories of common beans, on the basis of uses, are dry beans (seeds harvested at complete maturity), snap beans (tender pods with reduced fibre harvested before the seed development phase) and shell beans (seeds harvested at physiological maturity).  Its leaf is also occasionally used as a vegetable and the straw as fodder.  Its botanical classification, along with other "Phaseolus" species, is as a member of the legume family "Fabaceae", most of whose members acquire the nitrogen they require through an association with rhizobia, a species of nitrogen-fixing bacteria.

Banana: The banana is an edible fruit – botanically a berry – produced by several kinds of large herbaceous flowering plants in the genus "Musa".  In some countries, bananas used for cooking may be called plantains, in contrast to dessert bananas.  The fruit is variable in size, color and firmness, but is usually elongated and curved, with soft flesh rich in starch covered with a rind which may be green, yellow, red, purple, or brown when ripe.  The fruits grow in clusters hanging from the top of the plant.  Almost all modern edible parthenocarpic (seedless) bananas come from two wild species – "Musa acuminata" and "Musa balbisiana".  The scientific names of most cultivated bananas are "Musa acuminata", "Musa balbisiana", and "Musa" × "paradisiaca" for the hybrid "Musa acuminata" × "M. balbisiana", depending on their genomic constitution.  The old scientific name "Musa sapientum" is no longer used.

List of Durio species: Among the thirty known species of "Durio", so far nine species have been identified to produce edible fruits.  However, there are many species for which the fruit has never been collected or properly described and it is likely that other species with edible fruit exist.  The currently known nine species of edible durians are:

Cereal: A cereal is any grass cultivated for the edible components of its grain (botanically, a type of fruit called a caryopsis), composed of the endosperm, germ, and bran.  Cereal grains are grown in greater quantities and provide more food energy worldwide than any other type of crop and are therefore staple crops.  Edible grains from other plant families, such as buckwheat (Polygonaceae), quinoa (Amaranthaceae) and chia (Lamiaceae), are referred to as pseudocereals.

Pyrus × bretschneideri: Pyrus" × "bretschneideri (or "Pyrus" ×"bretschneideri"), the ya pear or pearple or Chinese white pear (), is an interspecific hybrid species of pear native to North China, where it is widely grown for its edible fruit.

Sorghum bicolor: Sorghum bicolor, commonly called sorghum ( ) and also known as great millet, durra, jowari, or milo, is a grass species cultivated for its grain, which is used for food, both for animals and humans, and for ethanol production.  Sorghum originated in northern Africa, and is now cultivated widely in tropical and subtropical regions.  Sorghum is the world's fifth most important cereal crop after rice, wheat, maize and barley.  "S. bicolor" is typically an annual, but some cultivars are perennial.  It grows in clumps that may reach over 4 m high.  The grain is small, ranging from 2 to 4 mm in diameter.  Sweet sorghums are sorghum cultivars that are primarily grown for foliage, syrup production, and ethanol; they are taller than those grown for grain.

Sweet sorghum: Sweet sorghum is any of the many varieties of the sorghum grass whose stalks have a high sugar content.  Sweet sorghum thrives better under drier and warmer conditions than many other crops and is grown primarily for forage, silage, and syrup production.  Although, in most of the United States the term "molasses" refers to a sweet syrup, made as a byproduct of sugarcane or sugar beet sugar extraction, sweet sorghum syrup is known as "sorghum molasses" in some regions of the U.S

Sorghum × drummondii: Sorghum" × "drummondii (Sudangrass), is a hybrid-derived species of grass raised for forage and grain, native to tropical and subtropical regions of Eastern Africa.  The plant is cultivated in Southern Europe, South America, Central America, North America and Southern Asia, for forage or as a cover crop.

Question: Sorghum × drummondii is a type of grass harvested for what type of edible fruit?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plant_name": {
      "type": "string",
      "description": "The scientific name of the plant."
    },
    "plant_type": {
      "type": "string",
      "description": "The general type of plant."
    },
    "harvested_for_purpose": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The primary purposes for which the plant is harvested."
    },
    "edible_fruit_type": {
      "type": "string",
      "description": "The botanical name for the edible fruit of the plant's grain."
    }
  },
  "required": [
    "plant_name",
    "plant_type",
    "harvested_for_purpose",
    "edible_fruit_type"
  ],
  "additionalProperties": false
}
