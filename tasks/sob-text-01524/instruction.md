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
Green Lantern (Six Flags Great Adventure): Green Lantern is a steel stand-up roller coaster located at Six Flags Great Adventure in Jackson Township, New Jersey.  "Green Lantern" stands 155 ft tall and features a top speed of 63 mph .  The 4155 ft ride features five inversions and a duration of approximately 2⁄ minutes.  The ride was manufactured by Swiss firm Bolliger & Mabillard.  Green Lantern is fairly similar to the former Mantis, stand-up coaster at Cedar Point, but is taller, faster, and features one more inversion.

The Riddler's Revenge: The Riddler's Revenge is a stand-up roller coaster at Six Flags Magic Mountain.  Manufactured by Bolliger & Mabillard, the ride opened in 1998 as the park's eleventh roller coaster, setting world records among stand-up coasters for height, speed, drop length, track length and number of inversions.  The previous record holder was Chang at Six Flags Kentucky Kingdom which opened a year earlier.  Located in the Movie Town area of the park, The Riddler's Revenge was also the park's single biggest investment at a cost of $14 million.  It stands 156 ft tall and features a top speed of 65 mph .  The 4370 ft coaster also features six inversions and a ride duration of approximately three minutes.

War of the Green Lanterns: "War of the Green Lanterns" is a ten-issue American comic book crossover storyline published by DC Comics that spans across the "Green Lantern", "Green Lantern Corps", and "Green Lantern: Emerald Warriors" series.  It was written by each series' writer, Geoff Johns, Tony Bedard, and Peter Tomasi respectively, and drawn by Doug Mahnke, Tyler Kirkham, and Fernando Pasarin.

Green Lantern Corps: Recharge: " Green Lantern Corps: Recharge " was a five-issue, monthly comic book limited series that was published by DC Comics from November 2005 to March 2006.  The series was written by Geoff Johns and Dave Gibbons and illustrated by Patrick Gleason.  The series starred several members of the Green Lantern Corps, a fictional intergalactic police force in the DC Universe, and was one of two follow-ups (the other being a fourth volume of "Green Lantern", with Hal Jordan as the main character) to the mini-series " ", which had been published earlier in 2005.  It is notable for featuring the first appearances of Soranik Natu, Vath Sarn and Isamot Kol, members of the Green Lantern Corps that would serve as recurring characters in future Green Lanterns storylines written by Johns and other writers.

Tomar-Tu: Tomar-Tu is a fictional character, a Green Lantern featured in comic books published by DC Comics.  He is a tall, well-muscled humanoid alien with reddish-orange skin and a partially bald head.  Other distinguishing features include a fish fin running down the center of his head, lupine ears and a bird‘s beak for a mouth.  He first appeared in "Green Lantern" (vol.  3) #4 story titled "Among My Souvenirs".  He became a Green Lantern in "Green Lantern" (vol.  3) #24 (May 1992) in a story titled "The Decision".  He was created by Gerard Jones.

Green Lantern (comic book): Green Lantern is an ongoing American comic book series featuring the DC Comics heroes of the same name.  The character's first incarnation, Alan Scott, appeared in "All-American Comics" #16 (July 1940), and was later spun off into the first volume of "Green Lantern" in 1941.  That series was canceled in 1949 after 38 issues.  When the Silver Age Green Lantern, Hal Jordan, was introduced, the character starred in a new volume of "Green Lantern" starting in 1960 and has been the lead protagonist of the Green Lantern mythos for the majority of the last fifty years.

Green Lantern Corps: The Green Lantern Corps is the name of a fictional intergalactic military/police force appearing in comics published by DC Comics.  They patrol the farthest reaches of the DC Universe at the behest of the Guardians, a race of immortals residing on the planet Oa.  According to DC continuity, the Green Lantern Corps has been in existence for three billion years, surviving multiple conflicts both internal and foreign.  Currently operating divided as pairs amongst the 3600 “sectors” of the universe, there are 7202 members (known commonly as Green Lanterns), two lanterns for every sector except sector 2814 which has 4 members.  Each Green Lantern is given a power ring, a weapon granting the use of incredible abilities that are directed by the wearer's own willpower.

The Green Ghost Project: The Green Ghost Project is a collaborative album by American hip hop recording artist Styles P and American record producer DJ Green Lantern.  It was released on February 2, 2010 via DJ Green Lantern's label Invasion Records.  The album features guest appearances from M.O.P., N.O.R.E., Uncle Murda and Junior Reid, as well as Style P's D-Block cohorts Jadakiss and Sheek Louch, among others.  The album's production was handled by DJ Green Lantern, Dame Grease, The Alchemist, Buckwild, Dutchez Beatz, Statik Selektah, Vinny Idol and Poobs.

Simon Baz: Simon Baz is a fictional comic book superhero appearing in books published by DC Comics, usually in those starring the Green Lantern Corps, an extraterrestrial police force of which Simon is a member.  Created by writer Geoff Johns and artist Doug Mahnke, Simon Baz is the first Middle-Eastern and Muslim member of the Green Lantern Corps.  The character made his debut in 2012 following DC's 2011 company-wide relaunch as part of its "Green Lantern" story arc "Rise of the Third Army", in which he replaces Silver Age hero Hal Jordan as the Green Lantern of Earth's sector.

Green Lantern Coaster: Green Lantern Coaster is a steel roller coaster at Warner Bros.  Movie World on the Gold Coast, Queensland, Australia.  The ride is themed after DC Comics' Green Lantern and is located within the park's DC Comics superhero hub.  The ride is an El Loco roller coaster manufactured by S&S Worldwide, characterised by a tight circuit featuring a beyond-vertical drop and an outward banked turn.  It holds the record for the steepest drop of any roller coaster in the Southern Hemisphere, and the second steepest in the world.  "Green Lantern Coaster" officially opened on 23 December 2011.

Question: What Company manufactured The Riddler's Revenge and the Green Lantern?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "manufacturer_name": {
      "type": "string",
      "description": "The name of the company that manufactured the roller coasters."
    },
    "coasters_manufactured": {
      "type": "array",
      "description": "A list of roller coaster names manufactured by the company.",
      "items": {
        "type": "string"
      }
    },
    "total_coasters_identified": {
      "type": "integer",
      "description": "The total number of roller coasters identified as manufactured by the company."
    }
  },
  "required": [
    "manufacturer_name",
    "coasters_manufactured",
    "total_coasters_identified"
  ],
  "additionalProperties": false
}
