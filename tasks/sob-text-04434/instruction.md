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
Ramon Ayala (accordion player): Ramon Ayala is an accordion player from Hidalgo, Texas, who currently resides in the Rio Grande Valley.  He is the son of Pedro Ayala.  His progressive style and technique has earned him the 2009 Accordion Player of the Year Award from the South Texas Conjunto Association.  In 2009 he celebrated his 45th career anniversary.

Fritz Tschannen: Fritz Tschannen (13 May 1920 – 23 March 2011) was a Swiss accordion player and former ski jumper who competed at the 1948 Winter Olympics in St. Moritz.  Born in Saint-Imier, he received his first accordion at the age of five and gave his first solo concert three years later.  By the age of 18 he was working as an accordion teacher, in addition to ski jumping out of Skiclub Adelboden.  He joined the Swiss National Team in 1945 and attended the Winter Olympic Games three years later, where he placed ninth in a field of forty-nine competitors in the men's normal hill event.  That same year he became the Swiss national ski jumping champion and set a new world record with a jump of 120 metres.

Mixer dance: A mixer dance, dance mixer or simply mixer is a kind of participation dance in a social dance setting that involves changing partners as an integral part.  Mixing can be built into the dance choreography or can be structured to occur more randomly.  Mixers allow dancers to meet new partners and allow beginners to dance with more advanced dancers.  Some people may take advantage of mixers to assess dance skills of other persons without fear of being stuck with a poor match for an entire dance.

Kevin Naquin: Kevin Naquin is a Cajun accordion player in south Louisiana from Ossun, Louisiana.  Naquin is the lead singer and accordion player in the Cajun band Kevin Naquin and the Ossun Playboys.  In 2000, he won the CFMA - 2000 Album of the Year with his album "Pour La Premiere Fois" and CFMA - 2000 Song of the Year.  He has recorded with Swallow Records and Bayou Groove Productions.

Finbarr Dwyer: Finbarr Dwyer (often misspelled as "Finbar Dwyer") (20 September 1946 – 8 February 2014) was a traditional Irish accordion player from the famed Dwyer musical family.  He was born in Castletownbere, Co.  Cork on 20 September 1946, began playing accordion at the age of three, and began composing at the age of nine.  Both of his parents played accordion and his father also played fiddle.  His brothers Richard and Michael (died 1996) likewise played accordion, while his brother John, born in 1933, played fiddle.  In 1969 he won the All-England accordion title.  He died on 8 February 2014, in Mallow, Co.  Cork, Ireland.

Chicken Dance: The "Chicken Dance", also known as the Birdie Song or the Chicken Song, is an oom-pah song and its associated fad dance is now a contemporary dance throughout the Western world.  The song was composed by accordion (Handharmonika) player Werner Thomas from Davos, Switzerland, in the 1950s.

Hokey cokey: The hokey cokey (United Kingdom), hokey pokey (United States, Ireland, Canada, Australia, the Caribbean, Israel), or hokey tokey (New Zealand), is a participation dance with a distinctive accompanying tune and lyric structure.  It is well known in English-speaking countries.  It originates in a British folk dance, with variants attested as early as 1826.  The song and accompanying dance peaked in popularity as a music hall song and novelty dance in the mid-1940s in Britain and Ireland.  The song became a chart hit twice in the 1980s.  The first hit was by The Snowmen, which peaked at UK No. 18 in 1981.

Participation dance: Participation dance (also group-participation dance or audience participation dance) is a major class of dance that encourages dancing in a group.  It includes social games based on dancing, for example at weddings, festivals and other social gatherings.  Some have simple words to be sung to the music, which may act as a reminder of the steps - one example is the Hokey-cokey.  Some consist of a few simple steps learned either from simple instructions given by a leader or from watching others.  Examples are Electric Slide, Macarena, YMCA, and the Chicken Dance.

Erotic dance: An erotic dance is a dance that provides erotic entertainment and whose objective is the stimulation of erotic or sexual thoughts or actions in viewers.  Erotic dance is one of several major dance categories based on purpose, such as ceremonial dance, competitive dance, participation dance, performance dance and social dance.

Sonny Brogan: Sonny (Patrick Joseph) Brogan (4 July 1906 – 1 January 1965) was an Irish accordion player from the 1930s to the 1960s, and was one of Ireland's most popular traditional musicians.  He was one of the earliest advocates of the two-row B/C button accordion in traditional music, and popularised it the 1950s and 60s.  He originally played on a single-keyed Hohner melodeon, and later the two-row Paolo Soprani (pictured) which he used until he died.  Sonny's Paolo Soprani was one of the rarest, the grey model, made in 1948, when the company still made them by hand.  Offaly-born button box player Paddy O'Brien currently has Sonny's accordion.

Question: Participation dance is a class of dance that encourages dancing in a group such as a song composed by what accordion player in the 1950's?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "accordion_player_name": {
      "type": "string",
      "description": "The name of the accordion player who composed the song."
    },
    "song_composed": {
      "type": "string",
      "description": "The name of the song composed by the accordion player."
    },
    "composition_decade": {
      "type": "string",
      "description": "The decade in which the song was composed."
    },
    "dance_type": {
      "type": "string",
      "description": "The type of dance associated with the song."
    },
    "player_origin": {
      "type": "string",
      "description": "The origin city and country of the accordion player."
    }
  },
  "required": [
    "accordion_player_name",
    "song_composed",
    "composition_decade",
    "dance_type",
    "player_origin"
  ],
  "additionalProperties": false
}
