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
Morphic (band): Morphic was an American heavy metal band formed in Royal Oak, Michigan, in 2000.  The band's final lineup consisted of John Webb (lead vocals), Josh DeVries (guitar), Wes Alfonsi (bass guitar), Andrew Hale (lead guitar) and Matt Morrocco (drums, percussion).  Previously, the group also featured guitarist Tomo Miličević.

Rio Bonito Formation: The Rio Bonito Formation is a geological formation of the Paraná Basin of Permian age.  It is represented by a succession of cyclic sedimentary packages of sandstones, siltstones and shales which bear extensive deposits of coal that has been extracted since the 19th century.  The Rio Bonito Formation was deposited in a coastal environment, formed by rivers, deltas, bays and estuaries with tidal plains, barrier islands and shallow marine platform, at a time when the Paraná Basin was a large gulf of the ancient supercontinent Gondwana.  This gulf was open to the southwest, to the old ocean Panthalassa.  The Rio Bonito Formation outcrops occur mainly in the eastern border of the Paraná Basin, in a narrow band in the states of São Paulo, Paraná, Santa Catarina, Rio Grande do Sul and Uruguay.  The Rio Bonito Formation belongs to the second-order stratigraphic supersequence called Gondwana I.

The Palace of Auburn Hills: The Palace of Auburn Hills (commonly referred to as The Palace) is a defunct multi-purpose arena located in Auburn Hills, Michigan, a suburb of Detroit.  It served as the home of the Detroit Pistons of the National Basketball Association (NBA), the Detroit Shock of the Women's National Basketball Association (WNBA), the Detroit Vipers of the International Hockey League, the Detroit Safari of the Continental Indoor Soccer League, and the Detroit Fury of the Arena Football League.

Tomo Miličević: Tomislav "Tomo" Miličević (] ; born September 3, 1979) is an American musician and record producer best known as the lead guitarist of rock band Thirty Seconds to Mars.  Born in Sarajevo but raised in the United States, Miličević moved to Troy, Michigan in the early 1980s, where he became active in the local heavy metal scene and played in a number of bands, co-founding Morphic.  In 2003, he joined Thirty Seconds to Mars, with whom he achieved worldwide recognition in the mid-2000s after recording the band's second album "A Beautiful Lie" (2005).  Its full-length follow-ups, "This Is War" (2009) and "Love, Lust, Faith and Dreams" (2013), received further critical and commercial success.

Farellones Formation: Farellones Formation (Spanish: "Formación Farellones" ) is a geological formation of Miocene age in the Andes of Central Chile up almost entirely of volcanic and volcaniclastic rocks.  At some location reaches thicknesses in excess of 3000 m .  It overlies the Oligo–Miocene Abanico Formation across a diachronous unconformity.  The best exposure of the formation is said to be at the ski resort of Farellones east of Santiago.  From the latitude of Santiago to Rancagua the base of the formation becomes progressively younger and outcrops more scarce.  In the mentioned latitudes the formation has been deformed by a diachronous tectonic inversion that produced reverse faults and destroyed the extensional sedimentary basin were the rocks deposited and contributed to the uplift of the Andes in the Late Miocene.

Janet M. Anderson: Janet Anderson (1949–1996) was a successful Detroit commercial artist.  Born in Royal Oak, Michigan and raised in nearby St. Clair Shores, Anderson honed her artistic talents by studying drawing, illustration, and printmaking at the Cranbrook Academy of Arts, University of Michigan, College for Creative Studies in Detroit, and Pratt Institute, Brooklyn.  Though Anderson would cycle between Detroit and New York City during the mid-1970s and early 1980s, Detroit was her true artistic home.  Residing in the western suburb of Livonia for much of her adult life, Anderson gained renown for the clarity and animation of her ink drawings, watercolors, murals, and prints.  Anderson’s commercial work features depictions of famous Detroit landmarks and life along the Detroit River and Lake St. Clair.  (Her grandfather was a captain of the SS Ste. Clair).

Prima Porta: Prima Porta is a suburb of Rome located 12 kilometres north of its center along the Via Flaminia and just a kilometre outside of the Grande Raccordo Anulare highway.  It is located on the right bank of the Tiber where the Via Tiberina leads away from the Via Flaminia and another road led off along the Cremera to Veii (Latitude: 42.000992° - Longitude: 12.493380° ).  The location was strategically important due to the iron-rich cliffs of red tuff that approach the river at this point, the confluence of several roads, and its function as the north entry point to Rome.  Parrocchia Santi Urbano e Lorenzo a Prima Porta, is the name of the Catholic Parish.  It is looked after, the location of and serves as a House of formation for the Pauline Fathers. 

Royal Oak, Michigan: Royal Oak is a city in Oakland County of the U.S. state of Michigan.  It is a suburb of Detroit.  As of the 2010 census, the city had a population of 57,236.  It is the 8th-largest municipality in Oakland County and the 27th-largest municipality in Michigan by population.

Bishop Borgess High School: Bishop Borgess High School was a Catholic secondary school in the Detroit suburb of Redford, Michigan.  Named after Caspar Henry Borgess, the second Roman Catholic bishop of Detroit, it was founded by the parishes of St. Suzanne (in Detroit), Our Lady of Grace (Dearborn Heights), and St. Hilary (Redford).  Later contributing parishes included St. Monica (Detroit), St. Robert Bellarmine (Redford),St. Gemma(Detroit). St, Valentine(Redford), Christ the King(Detroit), St. Scholastica(Detroit),St. Thomas Aquinas(Detroit) and St. Gerard (Detroit).

The Second City Detroit: The Second City Detroit was a comedy theatre and training center located in the Detroit suburb Novi, Michigan.  It was the Second City's third mainstage theatre in North America following the Second City Chicago and Toronto.  Originally established in September 1993 in downtown Detroit, Michigan,the theatre relocated to a strip mall in Novi in 2005, where it remained until it was disbanded in 2009.  The original downtown Detroit theater, within the Hockeytown Cafe complex, is now named the City Theater (Detroit), and the Novi location is now named the Andiamo Novi Theatre.

Question: Which suburb of Detroit was the location of the formation of the band Morphic?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "formation_details": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the band was formed."
        },
        "state": {
          "type": "string",
          "description": "The state where the band was formed."
        },
        "is_detroit_suburb": {
          "type": "boolean",
          "description": "Indicates if the formation city is a suburb of Detroit."
        }
      },
      "required": [
        "city",
        "state",
        "is_detroit_suburb"
      ],
      "additionalProperties": false
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    }
  },
  "required": [
    "band_name",
    "formation_details",
    "formation_year"
  ],
  "additionalProperties": false
}
