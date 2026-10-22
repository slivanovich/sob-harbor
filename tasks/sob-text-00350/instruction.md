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
2013 Columbia Lions football team: The 2013 Columbia Lions football team represented Columbia University in the 2013 NCAA Division I FCS football season.  They were led by second year head coach Pete Mangurian and played their home games at Robert K. Kraft Field at Lawrence A. Wien Stadium.  They were a member of the Ivy League.  They finished with a record of 0–10 overall, 0–7 in Ivy League play for a last place finish.  This was the sixth time in school history that the Columbia Lions went winless. </small>

2014 Columbia Lions football team: The 2014 Columbia Lions football team represented Columbia University in the 2014 NCAA Division I FCS football season.  They were led by third year head coach Pete Mangurian and played their home games at Robert K. Kraft Field at Lawrence A. Wien Stadium.  They were a member of the Ivy League.  They finished the season 0–10, 0–7 in Ivy League play to finish in last place.  This was the seventh time, and second consecutive year, the school ended the season winless.

2012 Columbia Lions football team: The 2012 Columbia Lions football team represented Columbia University in the 2012 NCAA Division I FCS football season.  They were led by first year head coach Pete Mangurian and played their home games at Robert K. Kraft Field at Lawrence A. Wien Stadium.  They are a member of the Ivy League.  They finished the season 3–7, 2–5 in Ivy League play to finish in a tie for sixth place.

Armenian Evangelical Church, Elâzığ: The historical Armenian Evangelical Church (Turkish: "Ermeni Protestan Kilisesi" , Armenian: Հայաստանեայց Աւետարանական Եկեղեցի ) is an Armenian Evangelical church located in the centre of the Turkish town of Elâzığ (Mamuretül-Aziz), next to Kharpert.  It was built in the 19th century and constituted the headquarters of this Church for Elazig.  After the Armenian Genocide, the church was used as the "Arpaci" Powder Industry Fabrique, then as a playground for children, and marketplace and shelter for animals.  Despite its Armenian identity it was described as an "historical Assyrian church" by the Turkish authorities in 1973.  In 2007, the Turkish state announced it will turn the church into a hospital, but as of 2014 no change has been made.  Because of its location in the centre of Elazig, it is used as parking lot for cars.

Pete Mangurian: Peter K. Mangurian born June 17, 1955 is an American football coach and former player.  He was most recently the Head Football Coach at Columbia University, a position he had held from December 2011 to December 2014.  Mangurian has been a long time assistant coach in the National Football League as tight end, offensive line and offensive coordinator.  He has coached in two Super Bowls and two Pro Bowls and numerous playoff appearances during his tenure as an NFL coach.  He also was the Head Football Coach at Cornell University from 1998 to 2000, compiling a record of 16–14.

John Bilezikjian: John Bilezikjian (February 1, 1948 – January 19, 2015) was an Armenian Los Angeles-based musician and composer.  Most renowned as an oud master, he also played the violin, mandolin and dumbek.  He was also a traditional and contemporary singer singing in Armenian, but also in Turkish, Assyrian/Syriac, English and known for his contributions to world music as a solo act and in collaborations with renowned artists.  He established his own record company, Dantz Records in Laguna Hills, California making many recordings, and appearing in tens of film soundtracks.

Taw Mim Semkath: Taw Mim Semkath (Syriac: ܬܡܣ "T.M.S.", originally ܒܝܬ ܝܬܡܐ ܕܐܬܘܪܝܐ ܒܩܝܠܝܩܝܐ "Beth Yatme d-Othuroye b-Qiliqiya"), also known as Assyrian National School Association (ANSA) after its founding organisation, is an Assyrian school and orphanage that opened in Adana in 1919 for orphaned Assyrian children who survived the Assyrian genocide.  The Assyrian National School Association, established in Stirling, New Jersey in 1899 by Assyrian immigrants from Diyarbakir who fled the massacre in 1895, founded the school with help from the French High Commissioner.  The Syriac Orthodox bishop Yuhanon Dolabani was an important figure at the school, contributing a lot with teaching and organizing.  In 1921, the school was closed by the Turkish authorities and moved to Beirut, Lebanon, where it is still running.

Ashur Yousif: Ashur Yousif (born Abraham Yusef), (Syriac: ܐܫܘܪ ܝܘܣܦ ܐܦܢܕܝ) (1858 Harput, Ottoman Empire - June 23, 1915 Diyarbekir, Ottoman Empire) was a professor and an ethnic Assyrian intellectual prior to World War I and the Assyrian Genocide.  He was Protestant, as was his wife - Arshaluys Oghkasian, daughter of an Armenian Protestant minister.  He studied (but did not graduate) at the Central Turkey College in Antep, and later became professor of Classical Armenian language at the Euphrates College in Harput.  In 1909, Ashur started publishing a Turkish-language newspaper named "Murshid Athuriyion" ("the spiritual guide of the Assyrians").  He also composed poems in Armenian and Turkish.

Assyrian cuisine: Assyrian cuisine is the cuisine of the indigenous ethnic Assyrian people, Eastern Aramaic speaking Syriac Christians of northern Iraq, north eastern Syria, north western Iran and south eastern Turkey.  Assyrian cuisine is very similar to other Middle Eastern cuisines such as Greek cuisine, Lebanese cuisine, Turkish cuisine, Israeli cuisine, Armenian cuisine and Persian cuisine, with most dishes being similar to the cuisines of the area in which those Assyrians live/originate from.  It is rich in grains, meat, tomato, herbs, spices, cheese and potato.  Alcohol, in particular Wheat Beer, Organic Wine and Arak is also consumed

Christian militias in Syria: A number of Christian militias have formed in Syria since the start of the Syrian Civil War in 2011.  The militias are composed largely of fighters from the various Syriac, Assyrian, Arab and Armenian Christian communities in Syria, and are also found amongst Assyrian communities in neighbouring northern Iraq.  Before the war, as much as 10% of the population was Assyrian, Syriac-Aramean, Armenian or Arab Christian, and together they formed one of the largest Christian minorities in the middle east.  In the early days of the civil war, some Christian communities were armed by the Syrian Government and Kurds to defend themselves against what were seen as threatening sectarian Sunni Islamic rebels.

Question: Which Amercain based professional also sang in Armenian, Turkish, and Assyrian, Pete Mangurian or John Bilezikjian? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who sang in the specified languages."
    },
    "profession": {
      "type": "string",
      "description": "The primary profession of the identified person."
    },
    "sang_in_armenian": {
      "type": "boolean",
      "description": "Indicates if the person sang in Armenian."
    },
    "sang_in_turkish": {
      "type": "boolean",
      "description": "Indicates if the person sang in Turkish."
    },
    "sang_in_assyrian": {
      "type": "boolean",
      "description": "Indicates if the person sang in Assyrian."
    },
    "other_singing_languages": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other languages the person was known to sing in, if any."
    }
  },
  "required": [
    "person_name",
    "profession",
    "sang_in_armenian",
    "sang_in_turkish",
    "sang_in_assyrian"
  ],
  "additionalProperties": false
}
