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
Saltwater (Julian Lennon song): "Saltwater" is a 1991 song performed by English singer, songwriter, and musician Julian Lennon.  It was written by Mark Spiro, Leslie Spiro and Julian Lennon.  Originally released on the album "Help Yourself", the single peaked at #6 in the UK in October 1991, and topped the Australian ARIA singles chart for four weeks in March 1992.  "Saltwater" was the 14th highest-selling single of 1992 in Australia, where it was certified platinum.

Cynthia Lennon: Cynthia Lennon (née Powell; 10 September 1939 – 1 April 2015) was the first wife of English musician John Lennon and mother of Julian Lennon.  She grew up in the middle-class section of Hoylake, on the Wirral Peninsula in North West England.  At the age of 12, she was accepted into the Junior Art School, and was later enrolled in the Liverpool College of Art.  John Lennon also attended the college; a meeting with Powell in a calligraphy class led to their relationship.

John Lennon Peace Monument: The John Lennon Peace Monument, also known as the European Peace Monument, is a peace monument entitled Peace & Harmony in Liverpool, England, dedicated to the memory of John Lennon.  "Peace & Harmony" was unveiled by Julian and Cynthia Lennon at a ceremony in Chavasse Park, Liverpool, on Saturday 9 October 2010 to celebrate what would have been John Lennon's 70th birthday.  The monument is now on the waterfront adjacent to ACC Liverpool at Kings Dock.

Manorhaus, Ruthin: Manorhaus is currently a boutique restaurant with rooms and is also an art gallery.  It was owned by John Lennon's first wife, Cynthia Lennon, and their son, Julian Lennon, attended Ruthin School.  Manorhaus has 8 rooms, each decorated with a different theme and interior design by local artists.  It also has a gym, sauna, steam room and also a well-stocked library available to guests.

Someday (Julian Lennon song): "Someday" is a song by Julian Lennon, released exclusively on iTunes on 8 April 2013, Lennon's birthday.  The track is also to appear as a bonus track on the international release of 2011's "Everything Changes".

Lucy (Julian Lennon song): "Lucy" is a song written and performed by Julian Lennon, James Scott Cook and Todd Meagher.  Recorded and mixed by Jason Stone in NYC.  The song, is a sort of follow-up to The Beatles' "Lucy in the Sky with Diamonds", originally inspired by a drawing by a then four-year-old Lennon given to his father.  The drawing was inspired by Lucy Vodden, a child friend of Lennon, and this song is dedicated to her. <ref name="CBS 12/15"> </ref>

Monument of the Holy Mother of God (Haskovo): The Monument of the Holy Mother of God (Bulgarian: Монумент „Света Богородица“, "Monument „Sveta Bogoroditsa“" ) is a monument in Haskovo, a city in southeastern Bulgaria.  The monument is dedicated to Mary, the mother of Jesus and was unveiled in 2003.  Standing at a total height of 31 m (of which the statue itself is 14 m ), the monument has been certified by the Guinness Book of World Records as the tallest statue of the Virgin Mary with the Infant Jesus in the world.  However, despite certification Guinness Book of Records, this statue does not exceed height at Monument Lady of Peace in Trujillo, Venezuela.

Too Late for Goodbyes: "Too Late for Goodbyes" is the first single (second in the U.S.) from Julian Lennon's 1984 album "Valotte".  It featured the harmonica of Jean "Toots" Thielemans, and it was a top-10 hit in the UK and U.S., reaching No. 6 in the UK Singles Chart in November 1984, and No. 5 on the "Billboard" Hot 100 singles chart in late March 1985.  B-side "Big Mama" has been described by Lennon as "semi-hard rock".

Julian Lennon: John Charles Julian Lennon (born 8 April 1963) is an English musician and photographer.  Lennon is the child of John Lennon and his first wife, Cynthia.

Mr. Jordan: Mr. Jordan is the third studio album by singer-songwriter Julian Lennon.  It was Lennon's first album in three years after taking a hiatus from the music industry.

Question: The mother of Julian Lennon unveiled what monument in Liverpool, England? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "monument_name": {
      "type": "string",
      "description": "The name of the monument."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the monument is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the monument is located."
        }
      },
      "required": [
        "city",
        "country"
      ],
      "additionalProperties": false
    },
    "unveilers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The individuals who unveiled the monument."
    },
    "unveiling_date": {
      "type": "string",
      "description": "The date the monument was unveiled."
    },
    "dedicated_to": {
      "type": "string",
      "description": "The person or entity to whom the monument is dedicated."
    }
  },
  "required": [
    "monument_name",
    "location",
    "unveilers",
    "unveiling_date",
    "dedicated_to"
  ],
  "additionalProperties": false
}
