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
Otto Heinrich Fugger, Count of Kirchberg: Otto Heinrich Fugger, Count of Kirchberg and Weissenhorn (1592–1644) was promoted to be a Knight of the Order of the Golden Fleece in 1628.  He was the son of Christoph Fugger von Glött, deceased 1615, the grandson of Johann Fugger, deceased 1598, the great grandson of very wealthy Augsburg city International businessman and banker Anton Fugger (1493–1560).  The 16th century Fugger's, descendents of a German businessmen family tracked down to the 14th century, were the Imperial bankers with King Charles I of Imperial Spain, also Holy Roman Emperor as Charles V (1500–1558), and his brother, also Holy Roman Emperor, Ferdinand I of Habsburg (1503–1564), king of Hungary and Bohemia from 1526, emperor from 1556 by abdication of his brother Charles.

Eustathios Argyros (general under Leo VI): Eustathios Argyros (Greek: Εὐστάθιος Ἀργυρός ; died ca. 910) was a Byzantine aristocrat and one of the most prominent generals under Emperor Leo VI the Wise (r. 886–912).  The first member of the Argyros family to rise to high posts, he fought with distinction against the Arabs in the east, before being disgraced ca. 907, possibly in connection with the flight of Andronikos Doukas to the Arabs.  Rehabilitated soon after, he was appointed as "strategos" of Charsianon, from which post he oversaw the settlement of Armenian lords as march-wardens along the Empire's eastern frontier.  Promoted to commander of the imperial bodyguard in late 908, he again fell into disgrace shortly after and died of poison (apparently a suicide) on his way to his estates.

Charles O'Gara: Charles O'Gara (b. 1699 in Saint-Germain, d. 1777) was a French-born courtier of Irish parentage who rose to prominence in the service of Leopold, Duke of Lorraine and later his son Francis I, Holy Roman Emperor.  Like the rest of his family he was a Jacobite who supported the return of Stuart rule to the British and Irish kingdoms.

Maria Caroline Charlotte von Ingenheim: Maria Caroline Charlotte von Ingenheim (1704-1749), was a German courtier.  She was the royal mistress of Charles VII, Holy Roman Emperor, i 1719-1723, and the ancestral mother of the "Grafen von Holnstein aus Bayern" line.

St. Uroš Cathedral, Ferizaj: The Church of the Holy Emperor Uroš (Serbian: црква Светог Цара Уроша ) is a Serbian Orthodox church located in the center of Ferizaj (Uroševac) in Kosovo.  It belongs to the Eparchy of Raška and Prizren.

Milo of Verona: Milo (Italian: "Milone" ) was the Count (later Margrave) of Verona from 931 until 955.  He was a vassal of four successive kings of Italy from 910.  Under Berengar I he became a courtier ("familiaris") and by 924 head of the bodyguard.  By 927 he had expanded his landholdings to have vassals of his own.  Under Hugh, he revolted twice but kept his position in Verona.  Under Berengar II, he was raised to the rank of margrave ("marchio") in 953.

Hieronymus Lauweryn van Watervliet: Count Hieronymus Lauweryn or Jerome Laurinus of Watervliet was a courtier at the courts of Philip the Handsome, to whom he was treasurer, Maximilian I, Holy Roman Emperor, and Margaret of Austria.  Of common origins, the lordship of Watervliet was awarded to Hieronymus by Philip in 1507 He married twice His son Matthias Lauweryn, or Matthias Laurinus (d.1540), the second lord of Watervliet, was well known to Erasmus.  He was responsible for the construction of the Church of Our Lady's Ascension in Watervliet.

German Emperor: The German Emperor (German: Deutscher Kaiser) was the official title of the head of state and hereditary ruler of the German Empire.  A specifically chosen term, it was used between the 18 January 1871 proclamation of King of Prussia and President of the North German Confederation Wilhelm I as ""Deutscher Kaiser"" and the official abdication of Wilhelm II on 28 November 1918.  The Holy Roman Emperor is sometimes also called "German Emperor" when the historical context is clear, as derived from the Holy Roman Empire's official post-1512 title of "Holy Roman Empire of the German Nation."

Karl Anselm, 4th Prince of Thurn and Taxis: Karl Anselm, 4th Prince of Thurn and Taxis, full German name: "Karl Anselm Fürst von Thurn und Taxis" (2 June 1733, Frankfurt am Main, Free Imperial City of Frankfurt, Holy Roman Empire – 13 November 1805, Winzer bei Regensburg, Electorate of Bavaria, Holy Roman Empire) was the fourth Prince of Thurn and Taxis, Postmaster General of the Imperial Reichspost, and Head of the Princely House of Thurn and Taxis from 17 March 1773 until his death on 13 November 1805.  Karl Anselm served as "Prinzipalkommissar" at the Perpetual Imperial Diet in Regensburg for Joseph II, Holy Roman Emperor and Francis II, Holy Roman Emperor from 1773 to 1797.

Berengar I of Italy: Berengar I (Latin: "Berengarius, Perngarius" ; Italian: "Berengario" ; 845 – 7 April 924) was the King of Italy from 887, and Holy Roman Emperor after 915, until his death.  He is usually known as Berengar of Friuli, since he ruled the March of Friuli from 874 until at least 890, but he had lost control of the region by 896.

Question: What year was The Holy Emperor of Romes courtier promoted to head of the bodyguard?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the courtier."
    },
    "emperor_served": {
      "type": "string",
      "description": "The name of the Holy Roman Emperor the courtier served."
    },
    "promotion_role": {
      "type": "string",
      "description": "The role the courtier was promoted to."
    },
    "promotion_year": {
      "type": "integer",
      "description": "The year of the promotion."
    }
  },
  "required": [
    "person_name",
    "emperor_served",
    "promotion_role",
    "promotion_year"
  ],
  "additionalProperties": false
}
