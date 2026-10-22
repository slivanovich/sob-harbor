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
No Use for a Name: No Use for a Name (sometimes abbreviated NUFAN or No Use) was a punk rock band from San Jose, California, United States formed in 1986 by Chris Dodge (guitar), Steve Papoutsis (bass guitar) and Rory Koff (drums).  The band's sound evolved considerably through its career, starting off as a Bay Area-influenced punk band, moving on to a much heavier metallic-tinted sound to finally taking on a much lighter brand of melodic punk as the years passed.  After Tony Sly's death on July 31, 2012, the remaining members chose to disband.

The Songs of Tony Sly: A Tribute: The Songs of Tony Sly: A Tribute is an album in tribute to No Use for a Name frontman Tony Sly who died unexpectedly in July 2012.  It was put together by Sly's friend Fat Mike who put the album out on his label, Fat Wreck Chords, with all profits from the album benefiting the Tony Sly Memorial Fund.  The album is made up of artists doing their own takes on No Use for a Name and Tony Sly songs.

Park Subin: Park Su-bin (born February 12, 1994), better known by the mononym Subin, is a South Korean singer, songwriter and television host.  She is best known as a member of South Korean girl group Dal Shabet.

Klenovnik, Serbia: Klenovnik () is a village in the municipality of Kostolac, city of Požarevac, Serbia.  According to the 2002 census, the village has a population of 904 people.  It derives its name from Klen, a type of deciduous tree.  Legend has it that the area was covered with a Klen forest, which was petrified, and resulted in a large deposit of coal.  The thermo-electric power plant Kostolac is near Klenovnik, and is largely powered by the coal extracted from the nearby open-surface mines.  Population of Klenovnik mainly shares in two occupations: agriculture and supporting industry for the nearby power plant.  Klenovnik has a small school, grades K-4.  Although it is a very small village it has city water, sewer, and steam heating.  Population is ethnically mainly Serbian.

Making Friends: Making Friends is the fourth studio album by punk rock band No Use for a Name, released in 1997.  It also includes a hidden track cover of the KISS song "Beth".  At the end of "Beth" the band starts to play "Soulmate" but gets interrupted by Tony Sly.

Acoustic Volume Two: Acoustic Volume Two is an acoustic alternative album by punk rock singers Joey Cape and Tony Sly, released on June 19, 2012, through Fat Wreck Chords.  It is the sequel to their 2004 split acoustic album, which was simply titled "Acoustic".

Keep Them Confused: Keep Them Confused the seventh studio album by punk rock band No Use for a Name, released on June 14, 2005.  "For Fiona" was released to radio on June 14, 2005.  A video for "For Fiona", a track about lead singer Tony Sly's daughter, has been released on the aforementioned record label.  The band went on a tour of Europe in April and May 2006 alongside Lawrence Arms.

Tony Sly: Anthony James Sly (November 4, 1970 – July 31, 2012) was an American singer, songwriter and guitarist, best known as the front man of the punk rock band No Use for a Name.  In his later years he also gained attention for his acoustic solo work, with two acoustic split albums he released with Lagwagon front man Joey Cape and two solo albums.

American Deutsch Bag: American Deutsch Bag is an EP by Teenage Bottlerocket.  It was released on November 26, 2013 on Fat Wreck Chords.  It was recorded at The Blasting Room with Andrew Berlin.  The EP features one original song and two covers.  One of the covers is a pop punk version of the German song "Ich bin Auslander und Spreche Nicht Gut Deutsch".  The other, "Via Munich" is originally by Tony Sly and was recorded for "".

Scorpios: Scorpios is an American indie rock band, working as a side project of several punk rock band members.  The original band members were Joey Cape, Tony Sly, Jon Snodgrass, and Brian Wahlstrom.

Question: What two occupations did Park Subin and Tony Sly have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the individuals whose occupations are being compared."
    },
    "common_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of occupations shared by both individuals."
    },
    "number_of_common_occupations": {
      "type": "integer",
      "description": "The count of common occupations found."
    }
  },
  "required": [
    "person_names",
    "common_occupations",
    "number_of_common_occupations"
  ],
  "additionalProperties": false
}
