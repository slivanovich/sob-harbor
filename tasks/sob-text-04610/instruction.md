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
The Odd Man: The Odd Man was a police series produced by Granada Television, running over four series between 1960 and 1963.  The character of pompous police Chief Inspector Charles Rose (William Mervyn) at the start of series 3 cemented the show's popularity and "The Odd Man" turned out to be the first in a trilogy lasting most of the 1960s, during which Rose's character slowly developed and became increasingly genial as they progressed.

Klaus J. Behrendt: Klaus J. Behrendt (born February 7, 1960 in Hamm, North Rhine-Westphalia) is a German actor.  Since 1992 he has starred in the Westdeutscher Rundfunk version of the popular television crime series "Tatort"; he also stars in the 2008 film "Die Bienen - Tödliche Bedrohung".

Klaus J. Kohler: Klaus J. Kohler (born 1935 in Karlsruhe) is one of the leading German phoneticians.

Tatort: Tatort ("Crime scene") is a German language police procedural television series that has been running continuously since 1970 with some 30 feature-length episodes per year, which makes it the longest-running German TV drama.  Developed by the German television channel ARD, it is unique in its approach, in that it is jointly produced by all of the station's regional public-service broadcasters whereby every regional station contributes a number of episodes to a common pool.  Therefore, the series is a collection of different police stories where different police teams each solve crimes in their respective city.  Uniqueness in architecture, customs and dialects of the cities is therefore a distinctive part of the series and often the city, not the police force is the real main character of an episode.  The concept of local stations only producing a couple of shows per year has also enabled the shows to be longer (90 minutes) and more fleshed out psychologically than other weekly TV dramas.

Christoph Nunatak: Christoph Nunatak ( ) is a nunatak rising to about 1,300 m , 2.5 nmi east-northeast of Holtet Nunatak in the Lyon Nunataks.  It was mapped by the United States Geological Survey from U.S. Navy aerial photographs taken 1965–68 and Landsat imagery taken 1973–74.  It was named by the Advisory Committee on Antarctic Names in 1987 after Klaus J. Christoph, upper atmospheric physicist at Siple Station, 1970–71.

Tessa Mittelstaedt: Tessa Mittelstaedt (born Ulm, April 1, 1974) is a German actress.  She is best known for playing the role of Franziska Lüttgenjohann in the Westdeutscher Rundfunk iteration of "Tatort", alongside Klaus J. Behrendt and Dietmar Bär.

Muellerilepis: The name is a tribute to German paleontologist Klaus J. Müller (1923-2010).  It is a replacement generic name for "Muellerina" Bardashev et Bardasheva, 2012.  which is preocccupied.

William J. Barry: William John Barry (born 1943 in Ireland) is one of the leading phoneticians in Germany.  He came to Germany in his early years and was mainly educated at the University of Kiel by the renowned German phonetician Klaus J. Kohler.  In 1992 he was appointed to the Chair of Phonetics at Saarland University.  His principal research areas were speech synthesis, rhythm and segmental structures, the application of linguistics to questions of pronunciation learning, speech-language pathology and speech technology in general.

Harbor Command: Harbor Command is an American police series that was syndicated from October 11, 1957, to July 4, 1958.  The series stars Wendell Corey as Captain Ralph Baxter, an officer of the Harbor Police of a large coastal city (the city is unnamed, but much of the series was filmed in San Francisco and San Diego).  The series was produced by Ziv Television Programs, with the assistance of the law enforcement arms of Harbor and Port Authorities across the country.  Captain Richard Storm, of the Port of San Diego's Harbor Police, was credited as the technical adviser for the series.

Paul Moriarty (actor): Paul Moriarty (born 19 May 1946) is a British actor.  He is best known for playing Det. Sgt. Jake Barrett in the ITV police series "The Gentle Touch" (1980–84) and George Palmer in the BBC soap opera "EastEnders" (1996–98).  Known for having a strong cockney accent, Moriarty has often been cast in police or criminal roles and has played police officers in ten different television shows throughout his career.

Question: Klaus J. Behrendt starred in a police series which was developed by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "series": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the television series."
        },
        "genre": {
          "type": "string",
          "description": "The genre or type of the series."
        },
        "developer": {
          "type": "string",
          "description": "The entity that developed the series."
        }
      },
      "required": [
        "title",
        "genre",
        "developer"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The developer of the police series the actor starred in."
    }
  },
  "required": [
    "actor",
    "series",
    "answer"
  ],
  "additionalProperties": false
}
