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
The Sainte Catherines: The Sainte Catherines are a six-piece punk-rock band who formed in Montreal, Quebec, Canada in 1999.  The group's name comes from "Rue Sainte-Catherine", one of Montreal's main streets.  Their third record, "The Art of Arrogance" was released on local label Dare to Care Records in 2003 and on the German label Yo-Yo Records.  In 2006, the band released its fourth LP, titled "Dancing for Decadence".  The album was released in the United States by Fat Wreck Chords.  The Sainte Catherines are the first band from Quebec to be signed to Fat Wreck.  In August 2006, The Sainte Catherines played their 500th show.  They also released split 7" records with Fifth Hour Hero and Whiskey Sunday.  In 2008, The Sainte Catherines won a GAMIQ Award for punk album of the year.

Boize (band): Boize was a Canadian heavy metal and glam metal band based in Montreal, Quebec.  The band was formed in the spring of 1989 in Laval, Quebec when vocalist Perry Blainey responded to an advertisement placed in the Montreal Gazette newspaper by bassist and keyboardist Stéphane Fania and guitarist Robert Kourie.  Boize was associated with record label Aquarius Records and was managed by Canadian musician star and recording studio owner Bill Hill, under his music production company and management agency Bill Hill Productions.  The band also had a brief association with South American heavy metal legend Alvacast, when singer Carlos "Charly" Lopez joined Boize as new vocalist in the fall of 1992.

Pat the White: Pat The White (Patrick Leblanc) is an award-winning artist from the Gaspé region of Quebec.  Leblanc was born on July 21, 1975.  He grew up in the town of Carleton-sur-Mer, Quebec.  He started playing guitar at a young age.  It was his uncle who taught him the basics.  In 1997, Leblanc left his home and worked for a while in Banff, Alberta.  It was there that Leblanc discovered his biggest musical influence, The Allman Brothers Band.  In 1999 he relocated to Quebec City and formed "The Pat The White Band".  Since 1999, Leblanc has been playing festivals in and around Quebec.  Festivals include the Mont Tremblant Blues Festival, the Montreal Jazz Festival, the Maximum Blues Festival, the "Woodstock en Beauce" Festival and the Sun Flower Gospel & Blues Festival in Clarksdale, Mississippi, U.S.

Despised Icon: Despised Icon is a Canadian deathcore band from Montreal, Quebec.  Formed in 2002, the band is notable for its use of dual lead vocalists; Alex Erian takes use of a mid-range growl technique while Steve Marois uses deep growling vocals, fry vocals and pig squeals.  In April 2010, the band announced that they would be disbanding and from there, began a farewell tour held across several countries.  Their final six shows were held in Quebec City, Toronto and Montreal during December of that year.  In early 2014, it was announced that the band would reform and play several more shows in the spring.

Iron Fist (album): Iron Fist is the fifth studio album by the band Motörhead, and was released 17 April 1982, on Bronze Records.  It would be the last of the 'classic' line up of Kilmister, Clarke and Taylor.  "Iron Fist" peaked at No. 6 on the UK album charts.  It was preceded by the release of the title track "Iron Fist" as a single on 3 April, which peaked in the UK singles chart at #29.

Kiss with a Fist: "Kiss with a Fist" is the debut single by indie rock band Florence and the Machine, taken from their debut studio album "Lungs" (2009).  The single was released through Moshi Moshi Records on 9 June 2008 in the UK and was then released four months later on 6 October 2008 through IAMSOUND Records in the US.  The B-side to "Kiss with a Fist" is a cover version of the Cold War Kids song "Hospital Beds".

Black Mirror (song): "Black Mirror" is the first single by Canadian indie rock band Arcade Fire in the US from their second album "Neon Bible" (while "Keep the Car Running" is the first in the UK).

Arcade Fire: Arcade Fire are a Canadian indie rock band based in Montreal, Quebec, consisting of husband and wife Win Butler and Régine Chassagne, along with Win's younger brother William Butler, Richard Reed Parry, Tim Kingsbury and Jeremy Gara.  The band's current touring line-up also includes former core member Sarah Neufeld, percussionist, Tiwill Duprate, and saxophonist, Stuart Bogie.

Honoré Mercier Bridge: The Honoré Mercier Bridge in Quebec, Canada, connects the Montreal borough of LaSalle on the Island of Montreal with the Mohawk reserve of Kahnawake, Quebec and the suburb of Châteauguay on the south shore of the Saint Lawrence River.  It is the most direct southerly route from the island of Montreal toward the US border.  It carries Route 138, originally Route 4.  It is 1.361 km in length and contains four steel trusses on its first section.  The height of the bridge varies from 12.44 m to 33.38 m with the highest sections located over the St. Lawrence Seaway.  The bridge is named after former premier of Quebec Honoré Mercier.

Jean Sébastien Lavoie: Jean Sébastien Lavoie (born July 15, 1978, in Montreal, Quebec) is a French Canadian singer who had his big break on the first edition of the francophonic hit music show based out of Paris called Nouvelle Star (patterned after the other Idol formats).  Jean Sébastien was the only contestant from Quebec to make it into the top ten, as the show chose to no longer include Quebec in the audition process after the first season.  It has been speculated that it was Lavoie's hailing from Quebec that might have been what prevented him from winning Nouvelle Star due to Quebec's geographical isolation from other francophonic territories, as well as its small population as a voting proportion.  Jean Sébastien received his biggest accolodates from the audience and panel of judges after performing Queen's "We Are the Champions," and after finishing third in the competition Lavoie released his own version of the song as his first single.  Lavoie's version of Queen's "We Are the Champions" cracked the top ten in ringtone sales across Europe in 2004.  Jean Sébastien has recorded two albums since Nouvelle Star which were both produced by BMG France, and still calls Montreal home

Question: What band from Montreal, Quebec had had the had their fist single in the US?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "origin_city": {
      "type": "string",
      "description": "The city where the band is based."
    },
    "origin_province": {
      "type": "string",
      "description": "The province where the band is based."
    },
    "first_us_single": {
      "type": "string",
      "description": "The title of the band's first single released in the US."
    },
    "associated_album": {
      "type": "string",
      "description": "The album from which the first US single was taken."
    }
  },
  "required": [
    "band_name",
    "origin_city",
    "origin_province",
    "first_us_single",
    "associated_album"
  ],
  "additionalProperties": false
}
