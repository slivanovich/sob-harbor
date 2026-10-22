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
Nerf Herder: Nerf Herder is an American rock band from Santa Barbara, California, formed in 1994 by Parry Gripp (vocals, guitar), Charlie Dennis (bass) and Steve Sherlock (drums).  They describe themselves as a "geek rock" band, and are known for simplistic modern punk-style songs with frequently humorous, juvenile, and pop-culture-referencing lyrics.

Captain Everything!: Captain Everything!  are a punk band from Watford, United Kingdom.  They met at Parmiter's School.  Formed in 1998, the band play high tempo pop-punk, which was branded "Bubblegum Thrash".  Renowned for their heavy touring schedule, they have played all over the UK and Europe, touring with bands such as The Vandals, Capdown, and Nerf Herder.  They have also toured in Russia, Canada and Japan.  They were part of the roster of London punk label Household Name Records.

How to Meet Girls: How to Meet Girls is the follow-up to Nerf Herder's self-titled release.  The album was released in 2000 on Honest Don's Records.  The track "Courtney" was written about Courtney Love, containing humorous references to her life.  Likewise, "Jonathan" is based on the life of Jonathan Richman, and contains references to his lyrics.

Nerf Herder (album): Nerf Herder is the eponymous debut album by Nerf Herder, originally released in November 1996 and produced by Joey Cape and Ryan Greene.

Nerf Herder IV: Nerf Herder IV is the fourth studio album by the rock band Nerf Herder.  It was released in 2008 through Oglio Records.

Linus of Hollywood: Kevin Dotson (born March 4, 1973), better known by his stage name Linus of Hollywood, is an American singer, songwriter, multi-instrumentalist, and record producer.  The stage name comes from his early days in Los Angeles, where he would frequently wear striped shirts similar to the Peanuts character Linus van Pelt.  He is currently a member of Nerf Herder and comedy duo Jarinus.

Oglio Records: Oglio Records is an American record company started in 1993 by Carl Caprioglio.  They are well known for issuing compilations of rare 1980's modern rock and new wave songs, many of which were previously unreleased on CD.  In addition to releasing new material by artists such as BigBang, Nerf Herder and Wesley Willis, the label has also re-released albums by artists such as Brian Wilson and Barnes & Barnes.  Oglio Entertainment also releases comedy CDs by comedians such as Jackie Martling and George Lopez.

Parry Gripp: Parry Gripp (born September 22, 1967 in Santa Barbara, California) is a singer-songwriter who is the lead vocalist and guitarist for the pop punk band Nerf Herder.

Voxtrot: Voxtrot was an indie pop band from Austin, Texas, USA.  Their first recordings were released in 2003 and their final shows were in June 2010.

Justin Fisher (musician): Justin Fisher is an American born bassist most well known for being the bassist in Nerf Herder, touring bassist for The Rentals and lead singer for Psoma.  Fisher also co-founded Rivers Cuomo's first band Avant Garde,

Question: Which is a pop band, Nerf Herder or Voxtrot?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_type": {
      "type": "string",
      "description": "The type of question being answered, related to band genre identification."
    },
    "bands_evaluated": {
      "type": "array",
      "description": "A list of bands considered in the question, with their mentioned genres.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "genres_mentioned": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Genres associated with the band in the context."
          }
        },
        "required": [
          "band_name",
          "genres_mentioned"
        ],
        "additionalProperties": false
      }
    },
    "identified_pop_band": {
      "type": "string",
      "description": "The name of the band identified as a pop band."
    },
    "is_nerf_herder_pop_band": {
      "type": "boolean",
      "description": "Indicates if Nerf Herder is classified as a pop band based on the context."
    },
    "is_voxtrot_pop_band": {
      "type": "boolean",
      "description": "Indicates if Voxtrot is classified as a pop band based on the context."
    }
  },
  "required": [
    "question_type",
    "bands_evaluated",
    "identified_pop_band",
    "is_nerf_herder_pop_band",
    "is_voxtrot_pop_band"
  ],
  "additionalProperties": false
}
