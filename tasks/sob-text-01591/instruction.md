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
Canadian name: Canadian naming conventions vary based on whether one is Aboriginal Canadian, English Canadian or French Canadian.

Mary Longman: Mary Longman (born 1964 in Fort Qu'Appelle, Saskatchewan) is a Canadian artist.  She is of Saulteaux heritage from the Gordon First Nation.  Her Aboriginal name is Aski-Piyesiwiskwew.  She is known for her sculptures, drawings, and paintings, which examine political, cultural, spiritual and environmental issues related to the experiences of Aboriginal people and colonialism, including the Sixties Scoop and residential schools.

Kwakiutl (statue): Kwakiutl (or variously KwaKiutl) is a totem sculpture by Aboriginal Canadian artist Simon Charlie, which has caused controversy for its nudity over multiple decades of display in Chinguacousy Township, and later Brampton, both near Toronto in Ontario, Canada.  Charlie, also known as Hwunumetse', later received the Order of Canada.  The 9-foot-tall cedar wood sculpture is best known for its exposed male genitals.

Carmen Robertson: Carmen L. Robertson is a writer and scholar of art history and indigenous peoples.  She was born in Fort Qu'Appelle, Saskatchewan, of Lakota and Scottish ancestry.  She is an associate professor at the University of Regina, where she has taught since 2006.  Before she came to the University of Regina, she was the Indian Fine Arts department head at the First Nations University of Canada.  A number of Robertson's writings focus on the Aboriginal Canadian artist Norval Morrisseau.  She is also past president of the Native Heritage Foundation of Canada.

Loretta Todd: Loretta Todd is a Métis Cree Canadian director, producer, activist, storyteller, and writer.  She belongs to what has been classified as the second wave of aboriginal Canadian film directors, and has been internationally recognized for her non-fiction work, which strives to express the lived experienced of aboriginal peoples and communities through their own voices.

Contact from the Underworld of Redboy: Contact from the Underworld of Redboy is an album by Robbie Robertson that was released in 1998 by Capitol Records.  The album is composed of music inspired by Aboriginal Canadian music (including traditional Aboriginal Canadian songs and chants) as well as modern rock, trip hop, and electronica, often integrated together, and features many guest artists.

Canadian Aboriginal syllabics: Canadian Aboriginal syllabic writing, or simply syllabics, is a family of abugidas (consonant-based alphabets) used to write a number of Aboriginal Canadian languages of the Algonquian, Inuit, and (formerly) Athabaskan language families.  They are valued for their distinctiveness from the Latin script of the dominant languages and for the ease with which literacy can be achieved; indeed, by the late 19th century the Cree had achieved what may have been one of the highest rates of literacy in the world.

Blake Debassige: Blake Debassige is a Native Canadian artist of the M'Chigeeng First Nation, born at West Bay on Manitoulin Island in Ontario on June 22, 1956.  A leading member of the "second generation" of Ojibwa artists influenced by Norval Morrisseau, Debassige has broadened the stylistic and thematic range of this group.  Debassige's paintings and graphics frequently investigate traditional Anishabek teachings about the nature of cosmic order, the cycles of the seasons, the interdependence of animal, plant and human life and the common principles at work in the world's great spiritual systems.  He frequently relates these themes to highly contemporary problems such as the destruction of the environment, the alienation of native youth and family dysfunction.

Norval Morrisseau: Norval Morrisseau, CM (March 14, 1932 – December 4, 2007), also known as Copper Thunderbird, was an Aboriginal Canadian artist.  Known as the "Picasso of the North", Morrisseau created works depicting the legends of his people, the cultural and political tensions between native Canadian and European traditions, his existential struggles, and his deep spirituality and mysticism.  His style is characterized by thick black outlines and bright colors.  He founded the Woodlands School of Canadian art and was a prominent member of the “Indian Group of Seven”.

Gordon Tootoosis: Gordon Tootoosis CM (October 25, 1941 – July 5, 2011) was an Aboriginal Canadian actor.  He was of Cree and Stoney descent.  Tootoosis was a descendant of Yellow Mud Blanket, brother of the famous Cree leader Pitikwahanapiwiyin.  He was acclaimed for his commitment to preserving his culture and to telling his people's stories.  He served as a founding member of the board of directors of the Saskatchewan Native Theatre Company.  Tootoosis offered encouragement, support and training to aspiring Aboriginal actors.  He served as a leading Cree activist both as a social worker and as a band chief.  In "Open Season" and "Boog and Elliot's Midnight Bun Run", Tootoosis was the voice of Sheriff Gordy.

Question: Who is the Aboriginal Canadian artist of the M'Chigeeng?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the Aboriginal Canadian artist."
    },
    "first_nation_affiliation": {
      "type": "string",
      "description": "The First Nation the artist belongs to."
    },
    "artist_type": {
      "type": "string",
      "description": "A general description of the artist's identity or category."
    },
    "birth_year": {
      "type": "integer",
      "description": "The year the artist was born."
    },
    "birth_location": {
      "type": "string",
      "description": "The specific location where the artist was born."
    },
    "influenced_by_artists": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of other artists who influenced this artist."
    }
  },
  "required": [
    "artist_name",
    "first_nation_affiliation",
    "artist_type",
    "birth_year",
    "birth_location",
    "influenced_by_artists"
  ],
  "additionalProperties": false
}
