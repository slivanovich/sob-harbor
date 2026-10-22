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
Modern Greek: Modern Greek (Νέα Ελληνικά ] or Νεοελληνική Γλώσσα ] "Neo-Hellenic", historically and colloquially also known as Ρωμαίικα "Romaic" or "Roman", and Γραικικά "Greek") refers to the dialects and varieties of the Greek language spoken in the modern era.

Kreuzberg: Kreuzberg (   ), a part of the combined Friedrichshain-Kreuzberg borough located south of Mitte since 2001, is one of the best-known areas of Berlin.  Kreuzberg, colloquially also known as X-Berg, is often described as consisting of two distinctive parts: the "SO 36", home to many immigrants; and "SW 61", roughly coterminous with the old postal codes for the two areas in West Berlin.  Kreuzberg has emerged from its history as one of the poorest quarters in Berlin in the late 1970s, during which it was an isolated section of West Berlin to one of Berlin's cultural centers in the middle of the now reunified city, known around the world for its alternative scene and counterculture.

Niamey railway station: Niamey (French: "Gare de Niamey" ), colloquially also known as "Niamey Hippodrome", is the main railway station of the city of Niamey, the capital of Niger.  Located near the Niamey Racecourse ("Hippodrome de Niamey"), in Niamey IV borough, is the first station opened in Niger and is part of AfricaRail project.

Vienna International Centre: The Vienna International Centre (VIC) is the campus and building complex hosting the United Nations Office at Vienna (UNOV; in German: Büro der Vereinten Nationen in Wien).  It is colloquially also known as UNO City.

Ennis Friary: Ennis Friary (colloquially also known as Ennis Abbey) was a Franciscan friary in the town of Ennis, County Clare, Ireland.  It was established in the middle of the 13th century by the ruling O'Brien dynasty who supported it for most of its existence.  Following the suppression of the monasteries in the 16th century, the friary continued to function for a while despite the loss of its lands.  In the early 17th century, the buildings were handed over to the Church of Ireland as a place of worship.  It was used as such until the late 19th century.  After the construction of a new Church of Ireland building, the friary fell into ruin.  Managed by the Office of Public Works since the late 19th century, it was formally returned to the Franciscan Order in 1969.

Joanne Atkinson: Joanne Louise Atkinson (born 4 March 1959), also known by her married name Joanne Palmer, is an English former competitive swimmer who represented Great Britain at the 1976 Summer Olympics.

JoAnne Buth: JoAnne L. Buth (born May 23, 1954) is a former Canadian politician.  She was appointed to the Canadian Senate by Stephen Harper on January 6, 2012 (replacing the retired Sharon Carstairs) and sat as a Conservative representing Manitoba.  She retired from the Senate on August 10, 2014 in order to become CEO of the Canadian International Grains Institute, a group that promotes Canadian field crops.

The Grand Knockout Tournament: The Grand Knockout Tournament (colloquially also known as It's a Royal Knockout) was a one-off charity event which was shown on British television on 19 June 1987, in addition to airing on American TV via the USA Network on 12 August 1987.  It followed the format of "It's a Knockout" (the British version of "Jeux Sans Frontieres"), a slapstick TV gameshow which was broadcast in the UK until 1982.

Conservative Party of Canada: The Conservative Party of Canada (French: "Parti conservateur du Canada" ), colloquially known as the Tories, is a political party in Canada.  It is positioned on the right of the Canadian political spectrum.  The party's leader is Andrew Scheer, who serves as Leader of the Official Opposition.

Joanne Fluke: Joanne Fischmann ("neé" Gibson, born  1943 in Swanville, Minnesota) is an American writer, using the pen name Joanne Fluke.  She is best known for her cozy mystery series surrounding a small-town baker, Hannah Swensen.  Four movies for the Hallmark Channel have been created based on her Hannah Swensen series.  Fluke is also known for making chocolate chip cookies for her readers.  Fluke has written under the pseudonyms John Fischer, R.J. Fischer, Jo Gibson, Chris Hunter, Gina Jackson and Kathyrn Kirkwood.

Question: JoAnne Buth sat for the party in Canada that is colloquially also known by what name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person mentioned in the question."
    },
    "political_party": {
      "type": "string",
      "description": "The name of the political party the person was associated with."
    },
    "party_colloquial_name": {
      "type": "string",
      "description": "The colloquial name for the political party."
    },
    "country": {
      "type": "string",
      "description": "The country where the political party operates."
    }
  },
  "required": [
    "person_name",
    "political_party",
    "party_colloquial_name",
    "country"
  ],
  "additionalProperties": false
}
