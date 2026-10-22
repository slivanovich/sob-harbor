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
Treaty of The Hague (1698): The Treaty of Den Haag (also known as the Treaty of The Hague or the First Partition Treaty) was signed on October 11, 1698 between England and France.  The accord attempted to resolve who would inherit the Spanish throne, proposing that Joseph Ferdinand of Bavaria be the heir.  Moreover, the agreement proposed that Louis, "le Grand Dauphin", would receive Naples, Sicily, Finale, and the ports in Tuscany while Archduke Charles, the younger son of Holy Roman Emperor Leopold I would receive the Spanish Netherlands.  Leopold, Duke of Lorraine, would take Milan, which in turn ceded Lorraine and Bar to the Dauphin.

List of Holy Roman Empresses: Holy Roman Empress or Empress of the Holy Roman Empire is the title given to the consort (wife) or regent of the Holy Roman Emperor.  The elective dignity of Holy Roman Emperor was restricted to males only, therefore there was never a Holy Roman Empress regnant, though women such as Theophanu or Maria Theresa of Austria, who controlled the power of rule, served as de facto Empresses regnant.

Wolfgang Ebner: Wolfgang Ebner (16121665) was a German baroque composer.  He was a Viennese court organist in the latter years of the reign of Ferdinand III, Holy Roman Emperor, and then of Leopold I, Holy Roman Emperor.

Joseph Ferdinand of Bavaria: Joseph Ferdinand Leopold of Bavaria (28 October 1692 – 6 February 1699) was the son of Maximilian II Emanuel, Elector of Bavaria (1679–1705, 1714–1726) and his first wife, Maria Antonia of Austria, daughter of Leopold I, Holy Roman Emperor, maternal granddaughter of King Felipe IV of Spain.

Archduke Alexander Leopold of Austria: Archduke Alexander Leopold of Austria (Alexander Leopold Johann Joseph; Hungarian: "Sándor Lipót" ; 14 August 1772 – 12 July 1795) was Palatine of Hungary, appointed during the reign of his father, Holy Roman Emperor Leopold II, and serving into the reign of his elder brother, Holy Roman Emperor Francis II.

Maria Josepha of Bavaria: Maria Josepha of Bavaria (Marie Josephe Antonie Walburga Felicitas Regula, 20 March 173928 May 1767) was Holy Roman Empress, Queen of the Romans, Archduchess of Austria, Grand Duchess of Tuscany, etc. by her marriage to Joseph II, Holy Roman Emperor.  By birth, she was a Princess and Duchess of Bavaria as the daughter of Charles VII, Holy Roman Emperor, Elector of Bavaria, and Archduchess Maria Amalia of Austria.

Leopold I, Holy Roman Emperor: Leopold I (name in full: "Leopold Ignaz Joseph Balthasar Felician"; Hungarian: "I. Lipót" ; 9 June 1640 – 5 May 1705) was Holy Roman Emperor, King of Hungary, Croatia, and Bohemia.  The second son of Ferdinand III, Holy Roman Emperor, by his first wife, Maria Anna of Spain, Leopold became heir apparent in 1654 by the death of his elder brother Ferdinand IV.  Elected in 1658, Leopold ruled the Holy Roman Empire until his death in 1705.

Gerasim Zelić: Gerasim Zelić (Serbian: Герасим Зелић ; 1752–1828) was a renowned Serbian Orthodox Church archimandrite, traveller and writer (a contemporary and compatriot of Dositej Obradović).  His chief work is "Žitije" (Lives), in three volumes.  They are memoirs of his travels throughout western Europe, Russia and Asia Minor from the latter half of the 18th century to the first decade of the 19th century and the famous personalities (Napoleon, Prince Eugène, Viceroy of Naples, Joseph II, Holy Roman Emperor, Leopold II, Holy Roman Emperor, Francis II, Holy Roman Emperor, Semyon Zorich, Catherine the Great, Alexander I of Russia, Stanisław August Poniatowski, Dositej Obradović) he met.  He had valuable original notes on people, religions, manners, customs, trade, etc.

Maria Amalia of Austria: Maria Amalia of Austria (Maria Amalie Josefa Anna; 22 October 1701 – 11 December 1756) was Holy Roman Empress, Queen of the Germans, Queen of Bohemia, Electress and Duchess of Bavaria etc. as the spouse of Charles VII, Holy Roman Emperor.  By birth, she was an Archduchess of Austria as the daughter of Joseph I, Holy Roman Emperor and Wilhelmine Amalia of Brunswick-Lüneburg.

Karl Anselm, 4th Prince of Thurn and Taxis: Karl Anselm, 4th Prince of Thurn and Taxis, full German name: "Karl Anselm Fürst von Thurn und Taxis" (2 June 1733, Frankfurt am Main, Free Imperial City of Frankfurt, Holy Roman Empire – 13 November 1805, Winzer bei Regensburg, Electorate of Bavaria, Holy Roman Empire) was the fourth Prince of Thurn and Taxis, Postmaster General of the Imperial Reichspost, and Head of the Princely House of Thurn and Taxis from 17 March 1773 until his death on 13 November 1805.  Karl Anselm served as "Prinzipalkommissar" at the Perpetual Imperial Diet in Regensburg for Joseph II, Holy Roman Emperor and Francis II, Holy Roman Emperor from 1773 to 1797.

Question: how is Joseph Ferdinand of Bavaria and Leopold I, Holy Roman Emperor related?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first individual."
        },
        "relationship_to_person_2": {
          "type": "string",
          "description": "The relationship of the first individual to the second individual."
        }
      },
      "required": [
        "name",
        "relationship_to_person_2"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second individual."
        },
        "relationship_to_person_1": {
          "type": "string",
          "description": "The relationship of the second individual to the first individual."
        }
      },
      "required": [
        "name",
        "relationship_to_person_1"
      ],
      "additionalProperties": false
    },
    "relationship_summary": {
      "type": "string",
      "description": "A concise summary of the relationship between the two individuals, including the lineage path."
    }
  },
  "required": [
    "person_1",
    "person_2",
    "relationship_summary"
  ],
  "additionalProperties": false
}
