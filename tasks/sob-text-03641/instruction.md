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
Victor Urbancic: Dr. Victor Urbancic or Viktor Ernest Johann von Urbantschitsch (9 August 1903 – 4 April 1958) was an Austrian composer, conductor, teacher and music scholar from Vienna.  He emigrated to Iceland in 1938.  His wife, Melitta, came from a Jewish family.  Urbancic stayed for the second half of his life in Iceland and had a big influence on the music development in the country at the time.

Vienna: Vienna ( ; German: "Wien" , ] ) is the capital and largest city of Austria and one of the nine states of Austria.  Vienna is Austria's primary city, with a population of about 1.8 million (2.6 million within the metropolitan area, nearly one third of Austria's population), and its cultural, economic, and political centre.  It is the 7th-largest city by population within city limits in the European Union.  Until the beginning of the 20th century, it was the largest German-speaking city in the world, and before the splitting of the Austro-Hungarian Empire in World War I, the city had 2 million inhabitants.  Today, it has the second largest number of German speakers after Berlin.  Vienna is host to many major international organizations, including the United Nations and OPEC.  The city is located in the eastern part of Austria and is close to the borders of the Czech Republic, Slovakia, and Hungary.  These regions work together in a European Centrope border region.  Along with nearby Bratislava, Vienna forms a metropolitan region with 3 million inhabitants.  In 2001, the city centre was designated a UNESCO World Heritage Site.  In July 2017 it was moved to the list of World Heritage in Danger.

Vienna Symphonic Library: Vienna Symphonic Library GmbH (VSL) is one of the leading developers of sample libraries and music production software for classical orchestral music.  The company is located in a landmark protected building, called Synchron Stage Vienna based in the Austrian capital's 23rd district.

Synchron Stage Vienna: Synchron Stage Vienna is a recording facility specializing in recording large orchestras and film music.  The landmark protected building, formerly "Synchronhalle" ("Hall 6") of the historic film lot "Film City Vienna" in the Austrian capital's 23rd district is operated by Vienna Symphonic Library.

Wiener Derby: The Wiener derby, or Vienna derby is an association football local derby match between city rivals FK Austria Wien and SK Rapid Wien from the Austrian capital city of Vienna (Wien).  The two sides are the most successful in the country winning more national titles and cups than any other teams.  They are also two of the most popular clubs in Austria with fans across the country.

Federal Ministry of Finance (Austria): The Federal Ministry of Finance (German: "Bundesministerium für Finanzen" , abbreviated BMF or "Finanzministerium") is the cabinet-level finance ministry of the Austrian Federal Government.  Its seat is at the former city palace of Prince Eugene of Savoy in the Austrian capital Vienna.  The current Federal Minister of Finance is Hans Jörg Schelling (ÖVP).

List of fountains in Bratislava: This is a list of fountains, drinking fountains and water wells in Bratislava, the capital of Slovakia.  Approximately half of the over 140 fountains found in the city form part of the picturesque landscape of the medieval Old Town of Bratislava (the city was known in the past under many names) and serve as tourist attractions while many of the newer fountains are fine examples of socialist era building of modern panelák city suburbs.  The number of fountains in Bratislava is comparable to the four times larger neighboring Austrian capital Vienna.

Johann Hattey: Johann Evangelist Hattey (1859–1904) was an Austrian architect born in Vienna.  His father, born in Klášter, Pilsnerkreis, Bohemia, was called Josef (1818–1879) and owned some land and building plots in the city.  His mother's name was Anna Maria Borik, born in Žinkovy in 1815 and buried at the Vienna Central Cemetery on 16 January 1894.  Most of the buildings Johann built were, and still are, in the 18th area of the Austrian capital called 18. Wiener Gemeindebezirk or achtzehnten Bezirk.  According to University site, this is the list of buildings built in Vienna under his direction:

Wiener Moderne: The Wiener Moderne (] ) or "Viennese Modern Age" is a term describing the culture of Vienna in the period between approximately 1890 and 1910.  It refers especially to the development of modernism in the Austrian capital and its effect on the spheres of philosophy, literature, music, art, design and architecture.

Břeclav: Břeclav (] ; German: "Lundenburg" ; Hungarian: "Leventevár" ) is a town in the Moravia, South Moravian Region, Czech Republic, approximately 55 km southeast of Brno.  It is located at the border with Lower Austria on the Dyje River.  The nearest town on Austrian territory is Bernhardsthal.  Břeclav also lies 10 km northwest of the Slovak border at Kúty and 100 km north of the Austrian capital city Vienna.

Question: Victor Urbancic was a music scholar from the Austrian capital city that has a popualation of how many?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the Austrian capital city."
    },
    "country": {
      "type": "string",
      "description": "The country where the city is located."
    },
    "population_details": {
      "type": "object",
      "properties": {
        "city_population": {
          "type": "number",
          "description": "The population within the city limits."
        },
        "metropolitan_population": {
          "type": "number",
          "description": "The population within the metropolitan area."
        },
        "population_description": {
          "type": "string",
          "description": "A description of the city's population relative to the country."
        }
      },
      "required": [
        "city_population"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "city_name",
    "country",
    "population_details"
  ],
  "additionalProperties": false
}
