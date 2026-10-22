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
Florida Doesn't Suck: Florida Doesn't Suck is a split extended play by Floridian indie outfits, Fake Problems and You Blew It! .

It's Great to Be Alive (album): It's Great to Be Alive is the second full-length album from indie-punk band Fake Problems.  It was released February 17, 2009 and is their first for Side One Dummy since joining the label in November 2008.

Antarctigo Vespucci: Antarctigo Vespucci is an indie rock band composed of Chris Farren of Fake Problems and Jeff Rosenstock of Bomb the Music Industry.

Shiny: Shiny was a fake music genre that was made up by the YouTuber and Music Artist Andrew Huang.  His fans liked the idea of this fake genre so much that they started making songs in the genre.  The music of this genre is made using video game samples and have a low bass frequency.

The Knew: The Knew is an American rock and roll band from Denver, CO consisting of Jacob Hansen (guitars, vocals), Tim Rynders (bass), Tyler Breuer (guitars), and Andy Thomas (drums).  The group takes influences from such acts as The Rolling Stones, The Clash, Dillinger Four, The Replacements, and My Morning Jacket.  The Knew has shared the stage with numerous national acts such as Cold War Kids, Deer Tick, Titus Andronicus, Afghan Whigs, Fake Problems, Manchester Orchestra, Slim Cessna's Auto Club and has appeared at such festivals as South by Southwest, CMJ Music Marathon, Mile High Music Festival and the Monolith Festival.  The band is renowned for their high energy performances and being front row boys.

Fake Problems: Fake Problems is a four-piece indie rock from Naples, Florida.  They released their first full-length album, "How Far Our Bodies Go", on Sabot Productions on April 27, 2007.  Their second record, "It's Great to Be Alive", was released through Side One Dummy Records on February 17, 2009.  Their third record "Real Ghosts Caught On Tape" was released September 21, 2010, also on Sideonedummy.  They are currently on an indefinite hiatus.

Later Days: The band was formed by lead singer Mike Wassef in 2001 in Naples, FL.  For the 3 years, they released numerous demos and played shows throughout South Florida, many with good friends and contemporaries Fake Problems.  This period culminated with the release of "I've Got My Fingers Crossed, But I'm Not Holding My Breath" in 2003, which was recorded at Skylab Studios in Gainesville, FL and Produced by Maharamzeez and John Faratzis

Chris Farren (punk musician): Chris Farren (born April 29, 1986) is an American musician known for his work in the bands Fake Problems and Antarctigo Vespucci, as well as solo work.  He released an album of all-original Christmas Songs titled "Like A Gift From God Or Whatever" in 2014.  In 2016, Farren released his debut solo album, "Can't Die", through SideOneDummy Records.

Monoral: Monoral is a Japanese alternative rock band signed to Sony Music Japan.  The band consists of Anis Shimada on lead vocals and guitar and Ali Morizumi on bass and guitar.

Real Ghosts Caught on Tape: Real Ghosts Caught On Tape is the third full-length album from the rock band Fake Problems.  It released on September 21, 2010 and is their second release for Side One Dummy since joining the label in November 2008.  The song Soulless was used in an Android Application commercial.

Question: Fake Problems and Monoral, play which mutual genre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "bands_analyzed": {
      "type": "array",
      "description": "Details of the bands whose genres are being compared.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "genres_from_context": {
            "type": "array",
            "description": "List of genres explicitly mentioned for the band in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "band_name",
          "genres_from_context"
        ],
        "additionalProperties": false
      }
    },
    "common_genre": {
      "type": "string",
      "description": "The mutual genre identified between the bands."
    },
    "genre_derivation_method": {
      "type": "string",
      "description": "Describes how the common genre was derived (e.g., 'direct_match', 'parent_genre_identification', 'combination')."
    }
  },
  "required": [
    "bands_analyzed",
    "common_genre",
    "genre_derivation_method"
  ],
  "additionalProperties": false
}
