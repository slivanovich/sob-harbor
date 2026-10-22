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
Brat Pack (duo): The Brat Pack was a vocal duo hailing from New Jersey, USA.  Its members were Patrick Donovan (born July 26, 1958 in Passaic, New Jersey) and Ray Ray Frazier.  Donovan had been guitarist for House/Gospel artist CeCe Rogers and Curtis Hairston.  Ray Ray was keyboard player and vocalist in local NYC bands.

Twenty One Pilots: Twenty One Pilots (stylized as TWENTY ØNE PILØTS, and formerly as twenty | one | pilots) is an American musical duo originating from Columbus, Ohio.  The band was formed in 2009 by lead vocalist Tyler Joseph along with former members Nick Thomas and Chris Salih, who left in 2011, and currently consists of Joseph and drummer Josh Dun.  The duo rose to fame in the mid-2010s after several years of touring and independent releases.

Koishii &amp; Hush: Koishii & Hush (Simon Langford & Alex Sowyrda) are a dance music production duo hailing from England and Canada.

Lane Boy: "Lane Boy" is a song written and recorded by American musical duo Twenty One Pilots, for their fourth studio album, "Blurryface".  "Lane Boy" was released on YouTube worldwide on May 4, 2015, being released as a single on Google Play Store on the same day.  The music video was released on July 20, 2015.

Sá &amp; Guarabyra: Sá & Guarabyra, formerly Sá, Rodrix & Guarabyra, is a Brazilian folk rock duo hailing from Rio de Janeiro.  They are famous for mixing rock music with traditional Brazilian "caipira" music, in a style they would call "rural rock".

Say Lou Lou: Say Lou Lou (formerly Saint Lou Lou) are a twin sister musical duo hailing from Australia and Sweden.  Miranda Anna and Elektra June Kilbey-Jansson (born 7 June 1991) are the daughters of Steve Kilbey, the lead singer of Australian alternative band The Church and Karin Jansson, ex-girlfriend and recording partner of Kilbey (and before then a member of Swedish new wave band Pink Champagne).  They grew up in both Australia and Sweden.

Lemaitre (band): Lemaitre (pronounced ] ) is a Norwegian indie electronic duo hailing from Oslo.  The duo consists of members Ketil Jansen and Ulrik Denizou Lund, who met originally as schoolmates in Lillehammer, in southeastern Norway.  Jansen and Lund came together to form Lemaitre on 20 June 2010.  Lemaitre is currently based in Los Angeles, California.

Havnatt: Havnatt is a dark folk/neofolk musical duo hailing from Oslo, Norway.  The members, Cecilie Langlie and Tom Simonsen, are members of a number of other Oslo bands including Skumring, Vagrant God and Omit.  They formed Havnatt in the spring of 2006 when they were commissioned by the Skagestad family to turn three poems by the late Norwegian author Tormod Skagestad into music.  The three poems were Myrulla, Havnatt and Prammen from the collection of poems entitled Havdøgn.

Gene &amp; Debbe: Gene and Debbe were a pseudo-pop/country duo hailing from Nashville, Tennessee.

Soul Position: Soul Position is an American alternative hip hop duo hailing from Columbus, Ohio.  It consists of DJ/producer RJD2 and rapper Blueprint.  The duo has released two albums and one EP on Rhymesayers Entertainment.

Question: Lane Boy was written by the musical duo hailing from which Ohio city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_information": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the song."
        },
        "written_by_duo_name": {
          "type": "string",
          "description": "The name of the musical duo that wrote the song."
        }
      },
      "required": [
        "title",
        "written_by_duo_name"
      ],
      "additionalProperties": false
    },
    "musical_duo_origin": {
      "type": "object",
      "properties": {
        "duo_name": {
          "type": "string",
          "description": "The name of the musical duo."
        },
        "origin_city": {
          "type": "string",
          "description": "The city from which the musical duo originates."
        },
        "origin_state": {
          "type": "string",
          "description": "The state from which the musical duo originates."
        },
        "origin_country": {
          "type": "string",
          "description": "The country from which the musical duo originates."
        }
      },
      "required": [
        "duo_name",
        "origin_city",
        "origin_state",
        "origin_country"
      ],
      "additionalProperties": false
    },
    "answer_city": {
      "type": "string",
      "description": "The city that is the answer to the question."
    }
  },
  "required": [
    "song_information",
    "musical_duo_origin",
    "answer_city"
  ],
  "additionalProperties": false
}
