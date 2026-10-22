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
Celia (given name): Celia is a given name for females of Latin origin, as well as a nickname for Cecilia, Celeste, or Celestina.  The name is often derived from the Roman family name "Caelius", thought to originate in the Latin "caelum" ("heaven").  Celia was popular in British pastoral literature in the seventeenth and eighteenth centuries, stemming from Shakespeare's use in the play "As You Like It".  Celia is also the name of the main character in the series Celia's Journey, by Melissa Gunther.

Great skua: The great skua ("Stercorarius skua") is a large seabird in the skua family Stercorariidae.  The English name and species name "skua" is believed to originate from the Faroese "skúvur" or "skúgvur" ] and is the only known bird name to originate from the Faroes that has come into regular use elsewhere.  In Britain, it is sometimes known by the name bonxie, a Shetland name of Norse origin.  The genus name "Stercorarius" is Latin and means "of dung"; the food disgorged by other birds when pursued by skuas was once thought to be excrement.

Kumhausen: Kumhausen is a municipality in the district of Landshut in Bavaria in Germany.  There was a sausage baked that was 5.88 km and 1.7 tons made there.  It broke the record on June 27, 1999.  It was made by 15 butchers, leading was Bernhard Ossner.  To go with it, there was a 1.37 km long loaf of bread.  Also said to set a record.  Spectators had a chance to buy the sausage at the price of five German marks (US$2.65) per meter, with proceeds going to a charity for Romanian children.

Hog's pudding: Hog's pudding is a type of sausage produced in Cornwall and parts of Devon.  Some versions of the recipe comprise pork meat and fat, suet, bread, and oatmeal or pearl barley formed into the shape of a large sausage - also known as 'Groats pudding' and are very similar to a white pudding, whereas others versions of the recipe contain a high percentage of offal such as lung and liver and can more accurately be described as a sort of West Country haggis.  It is much spicier than white pudding as it contains black pepper, cumin, basil and garlic.  The sausage is usually around two inches in diameter.

Azaruja sausage: Azaruja sausage is a type of sausage from Azaruja, Évora, Alentejo, Portugal.  It is listed on the Ark of Taste.  They are produced seasonally during the pig harvest season from December until February.  Alentejo black pig (more widely known as Iberian black pig).  Other ingredients include spices and bread.  The family recipes go back at least 150 years and the sausages are made in traditional home kitchens using Alentejan fireplaces.

Gaudeamus igitur: "De Brevitate Vitae" (Latin: "On the Shortness of Life"), more commonly known as "Gaudeamus Igitur" ("So Let Us Rejoice") or just "Gaudeamus", is a popular academic commercium song in many Western countries, mainly sung or performed at university graduation ceremonies.  Despite its use as a formal graduation hymn, it is a jocular, light-hearted composition that pokes fun at university life.  The song is thought to originate in a Latin manuscript from 1287.  It is in the tradition of "carpe diem" ("seize the day") with its exhortations to enjoy life.  It was known as a beer-drinking song in many early universities and is the official song of many schools, colleges, universities, institutions, student societies and is the official anthem of the International University Sports Federation.

Chorizo ​​de Pamplona: Chorizo de Pamplona is a sausage that is typical in the cuisine of the Navarre region of Spain It is prepared with equal parts of finely-chopped beef and pork and significant amounts of paprika, with a natural or plastic casing which is designated to have a minimum size of forty millimeters in diameter.  The red-orange coloration is due to the addition of paprika, which is abundant in Navarre.  Despite its local name, it is a very common type of sausage in delicatessens around the Spanish territory.  It is also produced and sold in Pamplona, Spain.

Saveloy: A saveloy is a type of highly seasoned sausage, usually bright red, normally boiled and frequently available in British fish and chips shops, occasionally also available fried in batter.  The word is believed to originate from the Swiss-French "cervelas" or "servelat", ultimately from the Latin "cerebrus"; originally a pig brain sausage particularly associated with Switzerland.

Cervelat: Cervelat, also cervelas, servelat or zervelat, is a sausage produced in Switzerland, France (especially Alsace and Lyon) and parts of Germany.  The recipe and preparation of the sausage vary regionally.

List of rivers of Ponce, Puerto Rico: This list of rivers of Ponce consists of the 14 rivers in the municipality of Ponce, Puerto Rico.  Rivers that either originate in the municipality or that run the bulk of their course through said municipality are listed.  Except for two rivers, Río Portugués and Río Jacaguas, all other rivers originate and terminate within the boundaries of the municipality of Ponce.  This list does not include "quebradas" (English: brooks).  Only streams recognized as "rivers" by the United States Geological Survey and the Puerto Rico Department of Natural and Environmental Resources are included here.

Question: Saveloy is said to originate from the Latin "cerebrus" which is a sausage produced where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sausage_name": {
      "type": "string",
      "description": "The name of the sausage whose origin is being discussed."
    },
    "latin_origin": {
      "type": "string",
      "description": "The Latin word from which the sausage name is believed to originate."
    },
    "production_locations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of countries where the sausage is produced."
    },
    "specific_regions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of specific regions or cities within the production countries where the sausage is made."
    }
  },
  "required": [
    "sausage_name",
    "latin_origin",
    "production_locations"
  ],
  "additionalProperties": false
}
