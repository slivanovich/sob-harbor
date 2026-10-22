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
Saint-Étienne-en-Dévoluy cable car disaster: The Saint-Étienne-en-Dévoluy cable car disaster occurred on 1 July 1999 in Saint-Étienne-en-Dévoluy, France, when a gondola which was being operated on a privately owned aerial tramway detached from the cable it was traveling on, and fell into the valley below.  The accident killed all twenty people on board.  The death toll was equivalent to that of another cable car accident in Italy which occurred one year previously.  The disaster remains the deadliest cable car accident in France, and one of the deadliest such incidents anywhere in the world.

Noël Emmanuel Limage: Noël Emmanuel Limage (died January 20, 2007) was a Haitian senator with the Lespwa party.  In the 2006 election, he won a seat representing Artibonite in the senate, but was killed in a car accident near Gonaïves less than a year after taking office.  He was driving his car on a rural road when he swerved to avoid a cow and crashed into a ravine.  He was taken to a hospital, where he died of head injuries.  Two passengers in the car survived the accident; Limage's wife suffered a broken leg and a bodyguard escaped uninjured.

Nocton rail accident: The Nocton rail accident was a rail accident that happened on 28 February 2002 after a vehicle smashed through a wall and fell onto the tracks.  The driver, who was trapped in his van, was talking to emergency services on his mobile phone when he was killed by a two-carriage Sprinter train (156409).  The front carriage of the train was derailed, remaining upright.  14 occupants of the train were injured.  The incident happened exactly a year to the day after the similar Great Heck rail crash.

Utah Utes women's soccer: Utah Utes women's soccer represents the University of Utah in the Pac-12 Conference of NCAA Division I soccer.  The team is coached by Rich Manning.  The team plays its home games at Ute Soccer Field.

1996 Kamianske tram accident: The 1996 Kamianske tram accident occurred on 2 July 1996, in Kamianske, Dnipropetrovsk Oblast, Ukraine, when an overcrowded tram derailed during the evening rush hour, and crashed into a concrete wall.  An investigation by the local railway department discovered that the brakes on the tram car failed as it was going down a hill.  The derailment and subsequent crash killed a total of 34 people, and left over 100 others injured.  The incident was the deadliest tram accident in the Ukraine, and one of the deadliest tram disasters anywhere in the world, surpassing the 1954 Zagreb tram accident which killed 19 people.

Buckle Up For Chi: Buckle Up For Chi or BUFC was founded in November 2013 to honor the memory of the late Chi Cheng (Deftones Bassist, Father, Son, Brother) by promoting seat belt awareness.  Chi's own life was cut tragically short after he was involved in a car accident in late 2008 in which he was not wearing a seat belt.  The accident left him in a coma on life support for a few days after the accident.  After surgery to replace part of his skull flap that had been removed early in his hospitalization to help reduce swelling caused by the accident Chi showed slow improvement and was able to be upgraded to being in a semi conscious state.  He was then able to open his eyes and track movement around the room.  He was also able to eventually gain movement in his hands, make vocal sounds and to move his legs on command.  His progress was not without setbacks though as he was in and out of the hospital with infections.  Throughout this time his family and friends kept a wider group of supporters and the general public updated through oneloveforchi.com with the latest news and fundraising efforts to help pay the medical bills.  Chi's health insurance refused to pay for most of the treatments.  Chi's mother Jeanne Cheng posted the news of Chi's death by heart failure on oneloveforchi.com on April 13, 2013.  Chi left behind his mother, a brother, a sister, his son and his former wife.  He also left behind a fan base who cherished him as a Grammy winning bass player and spoken word poet.  http://www.nme.com/news/deftones/74021

Fast Mail (Southern Railway): The Fast Mail was a Southern Railway steam train that on September 27, 1903, derailed at Stillhouse Trestle in Danville, Virginia.  The train consisted of two postal cars, one express car, and one baggage car.  The accident inspired the famous railroad ballad - Wreck of the Old 97.  As mentioned in the song, the old 97's locomotive (#1102) did make it to Spencer, North Carolina.  It was hauled to the Southern Railway Spencer Shops where it was repaired and placed back into regular service for many years afterwards.

1993 NBA draft: The 1993 NBA draft took place on June 30, 1993, in Auburn Hills, Michigan.  The draft had some talented players at the top, but injuries and personal problems hurt many of them.  Anfernee Hardaway, Allan Houston, and Jamal Mashburn all looked like possible Hall of Famers until their careers were cut short by injuries.  Isaiah Rider and Vin Baker showed great potential but were plagued by personal problems.  Bobby Hurley's career was derailed by a car accident in December of his rookie year.  The mid-to-late first round (starting with pick 13) was littered with players that failed to make any significant impact, with the exception of three-time NBA champion Sam Cassell.  One of the NBA best all-time wing defensive players, three-time champion Bruce Bowen, went un-drafted.

Rich Manning: Richard Alan Manning (born June 23, 1970) is a retired American professional basketball player who was selected by the Atlanta Hawks in the second round (40th pick overall) of the 1993 NBA draft.  A 6'11" power forward-center born in Tacoma, Washington, Manning played two years in the NBA, for the Vancouver Grizzlies (1995–1996) and the Los Angeles Clippers (1997).  He played collegiately at both Syracuse University and the University of Washington, after having attended Center High School in Antelope, California.

Derrick Thomas: Derrick Vincent Thomas (January 1, 1967February 8, 2000), nicknamed D.T., was an American football linebacker and defensive end for the Kansas City Chiefs of the National Football League (NFL).  He played his entire 11-year career for the Chiefs after being drafted fourth overall in the 1989 NFL Draft.  Thomas, a member of the class of 2009 Pro Football Hall of Fame, was a premier football player throughout the 1990s and is considered one of the best pass rushers of all time.  In 1990 against the Seattle Seahawks, he set an NFL record with seven sacks in a single game.  On February 8, 2000, Thomas died from a massive blood clot that developed in his paralyzed legs and traveled to his lungs, causing a pulmonary embolism.  His paralysis was the result of severe injuries sustained in a car accident weeks earlier.  Thomas was inducted posthumously into the College Football Hall of Fame in 2014 and the Pro Football Hall of Fame in 2009

Question: Which player's career, drafted in the same year as Rich Manning, was derailed by a car accident?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player whose career was derailed."
    },
    "draft_year": {
      "type": "integer",
      "description": "The year the player was drafted."
    },
    "cause_of_derailment": {
      "type": "string",
      "description": "The specific event that derailed the player's career."
    },
    "impact_on_career": {
      "type": "string",
      "description": "Description of how the event affected the player's career."
    },
    "related_player_draft_year": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the related player (Rich Manning)."
        },
        "draft_year": {
          "type": "integer",
          "description": "The draft year of the related player."
        }
      },
      "required": [
        "name",
        "draft_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "draft_year",
    "cause_of_derailment",
    "impact_on_career",
    "related_player_draft_year"
  ],
  "additionalProperties": false
}
