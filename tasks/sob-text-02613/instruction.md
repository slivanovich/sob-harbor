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
Margrethe II of Denmark: Margrethe II (Danish: "Margrethe 2."  , ] ; Faroese: "Margreta 2."  ; Greenlandic: "Margrethe II" ; full name: "Margrethe Alexandrine Þórhildur Ingrid"; born 16 April 1940) is the Queen of Denmark.  She is also the supreme authority of the Church of Denmark and Commander-in-Chief of the Danish Defence.  Born into the House of Glücksburg, a royal house with origins in Northern Germany, she was the eldest child of Frederick IX of Denmark and Ingrid of Sweden.  She succeeded her father upon his death on 14 January 1972, having had become heir presumptive to her father in 1953, when a constitutional amendment allowed women to inherit the throne.  On her accession, Margrethe became the first female monarch of Denmark since Margaret I, ruler of the Scandinavian kingdoms in 1375–1412 during the Kalmar Union.  In 1967, she married Henri de Laborde de Monpezat, with whom she has two sons: Crown Prince Frederik (born 1968) and Prince Joachim (born 1969).  She has been on the Danish throne for 45 years, becoming the second-longest-reigning Danish monarch after her ancestor Christian IV.

Denmark–Slovenia relations: Denmark–Slovenia relations refers to the current and historical relations between Denmark and Slovenia.  Denmark have an embassy in Ljubliana.  Slovenia have an embassy in Copenhagen.  Both countries are members of the European Union and NATO.  Diplomatic relations were established on 20 January 1992.  There have been few ties between Denmark and Slovenia before the independence of Slovenia.  In 2001, Queen Margrethe II visited Slovenia.  In 2002, Danish prime minister Anders Fogh Rasmussen visited Slovenia, to support Slovenia in the European Union.  There is a small Slovenian community in Denmark, With the accession of Slovenia in the European Union, more Slovenians moved to Denmark.

John, King of Denmark: John (Danish and Norwegian: "Hans" ; Swedish: "Johan" ; né "Johannes") (2 February 1455 – 20 February 1513) was a Scandinavian monarch under the Kalmar Union.  He was King of Denmark (1481–1513), Norway (1483–1513) and as John II (Swedish: "Johan II" ) Sweden (1497–1501).  From 1482 to 1513, he was concurrently Duke of Schleswig and Holstein in joint rule with his brother Frederick.  He currently remains the only King of Denmark since the mid-15th century to not be named Christian or Frederick, if one does not include the current Queen of Denmark, Margrethe II.

Descendants of James VI and I: James VI and I (19 June 1566 – 27 March 1625), the only child of Mary, Queen of Scots, was King of Scots from 1567 and King of England and Ireland from 1603, being the first monarch of the House of Stuart to rule all three countries.  His descendants include Elizabeth II of the United Kingdom, Philippe of Belgium, Felipe VI of Spain, Carl XVI Gustaf of Sweden, Margrethe II of Denmark, Harald V of Norway, Willem-Alexander of the Netherlands, and Henri, Grand Duke of Luxembourg.  This article deals with numerous descendants of James and his wife Anne of Denmark (Since he is not known to have had any illegitimate children).

Queen Margrethe II Land: Queen Margrethe II Land (Danish: "Dronning Margrethe II Land" ) is a peninsula in the northern limit of King Christian X Land, northeastern Greenland.  Administratively it belongs to the NE Greenland National Park area.

Ingrid of Sweden: Ingrid of Sweden (Ingrid Victoria Sofia Louise Margareta; 28 March 1910 – 7 November 2000) was Queen of Denmark from 1947 until 1972 as the wife of King Frederick IX.

Denmark–Portugal relations: Denmark–Portugal relations refers to the current and historical relations between Denmark and Portugal.  Denmark has an embassy in Lisbon.  Portugal has an embassy in Copenhagen.  Both countries are members of the European Union and NATO.  In 1984, Queen Margrethe II visited Portugal.  In 2008, Danish exports to Portugal amounted 2,5 billion DKK, and Portuguese exports to Denmark amounted 2,3 billion DKK.

Princess Josephine of Denmark: Princess Josephine of Denmark, Countess of Monpezat (Josephine Sophia Ivalo Mathilda; born 8 January 2011), is the fourth and youngest child of Crown Prince Frederik and Crown Princess Mary, and the seventh grandchild of Queen Margrethe II of Denmark and her husband, Henrik, Prince Consort of Denmark.  She is the twin sister of Prince Vincent of Denmark.

Princess Elisabeth of Denmark: Princess Elisabeth of Denmark, {'1': ", '2': ", '3': 'RE', '4': "} ("Elisabeth Caroline-Mathilde Alexandrine Helena Olga Thyra Feodora Estrid Margrethe Désirée"; born 8 May 1935 in Copenhagen) is the daughter of Hereditary Prince Knud and Hereditary Princess Caroline-Mathilde of Denmark, and is a first cousin of the present Danish monarch, Queen Margrethe II.

Princess Nathalie of Sayn-Wittgenstein-Berleburg: Princess Nathalie of Sayn-Wittgenstein-Berleburg (Nathalie Xenia Margrethe Benedikte; born 2 May 1975, in Copenhagen, Denmark) is the youngest daughter of Prince Richard of Sayn-Wittgenstein-Berleburg and Princess Benedikte of Denmark and niece of Queen Margrethe II of Denmark and Queen Anne-Marie of Greece.

Question: What years did Margrethe II of Denmark's mother rule as Queen of Denmark?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of Margrethe II's mother."
    },
    "relationship_to_margrethe_ii": {
      "type": "string",
      "description": "The relationship of this person to Margrethe II."
    },
    "title_held": {
      "type": "string",
      "description": "The title held by the person."
    },
    "reign_start_year": {
      "type": "integer",
      "description": "The year the person started their reign as Queen of Denmark."
    },
    "reign_end_year": {
      "type": "integer",
      "description": "The year the person ended their reign as Queen of Denmark."
    }
  },
  "required": [
    "person_name",
    "relationship_to_margrethe_ii",
    "title_held",
    "reign_start_year",
    "reign_end_year"
  ],
  "additionalProperties": false
}
