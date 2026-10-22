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
Never Be Alone: Never Be Alone is an upcoming Philippine television drama series to be broadcast by GMA Network starring Jennylyn Mercado, Krystal Reyes, Frank Magalona and Angelu de Leon.  It is set to premiere on 2018 on GMA Afternoon Prime block.

My Faithful Husband: My Faithful Husband is a 2015 Philippine romantic drama series directed by Joyce E. Bernal, starring Dennis Trillo and Jennylyn Mercado along with Mikael Daez.  The drama series premiered on GMA Network and worldwide via GMA Pinoy TV on August 10, 2015.  "My Faithful Husband" succeeds "The Rich Man's Daughter" on the network's Telebabad primetime block.  The drama series also serves as the reunion project for the loveteam of Trillo and Mercado after the success of "Gumapang Ka Sa Lusak" for 5 years.  The show ended on November 13, 2015 on its 14-week run with the total of 70 episodes overall it will be replaced by "Little Nanay" on "Beautiful Strangers" timeslot.

My Love from the Star (2017 TV series): My Love from the Star is a 2017 Philippine romantic fantasy television series that premiered on GMA Network on May 29, 2017.  Based on the hit Korean drama of the same name, it was directed by Bb.  Joyce Bernal.  The series starred Jennylyn Mercado and Gil Cuerva, premiering on GMA Network's "Telebabad" primetime block and also worldwide via GMA Pinoy TV, replacing "Destined to Be Yours".  The series ended its 11-week run on August 11, 2017 with a total of 55 episodes.  It was replaced by "Mulawin vs. Ravena" on its timeslot.

The Prenup: The Prenup is a 2015 Filipino romantic comedy film starring Jennylyn Mercado and Sam Milby.  It is written and directed by Jun Lana.  It was released on October 14, 2015 by Regal Entertainment.

Second Chances (2015 TV series): Second Chances is a 2015 Philippine television drama series broadcast by GMA Network.  Starring Jennylyn Mercado, Camille Prats, Raymart Santiago and Rafael Rosell, it premiered on January 12, 2015 replacing "Hiram na Alaala" on the network's GMA Telebabad block, and also aired worldwide via GMA Pinoy TV.  The show concluded on May 8, 2015 on its 17-week run with the total of 83 episodes overall it will be replaced by "The Rich Man's Daughter" on its timeslot.  Starting on April 19, 2016 it currently re-airs on GMA Life TV worldwide.

List of My Love from the Star episodes: My Love from the Star is a Philippine romantic drama series based on the hit Korean drama of the same name broadcast by GMA Network starring Jennylyn Mercado and model-turned-actor Gil Cuerva.  It premiered on May 29, 2017 on GMA Telebabad primetime block and aired worldwide via GMA Pinoy TV.

English Only, Please: English Only, Please is a 2014 Filipino romantic comedy film directed by Dan Villegas and starring Jennylyn Mercado and Derek Ramsay.  Produced by Quantum Films, in association with MJM Productions, Tuko Film Productions and Buchi Boy Films it is an official entry to the 40th Metro Manila Film Festival.

Jennylyn Mercado: Jennylyn Anne Pineda Mercado (born May 15, 1987) is a Filipino actress, singer, and songwriter.  She was the winner of the first season of the reality talent competition "StarStruck".  Mercado garnered acclaim at a young age for her acting performances on television and film.  She is known for starring in multiple box office successes, namely "English Only, Please" (2014), "The Prenup" (2015), "Walang Forever" (2015), and "Just the 3 of Us" (2016).  She has released three albums from GMA Records and Viva Records which have several popular singles such as "Sa Aking Panaginip", "Moments Of Love" collaboration with Janno Gibbs, "Maybe This Time" and "Kahit Sandali".  In 2017, she is set to topbill the Philippine remake of "My Love from the Star".

My Love from the Star: My Love from the Star (; literally "You Who Came from the Stars") is a South Korean television series starring Jun Ji-hyun, Kim Soo-hyun, Park Hae-jin and Yoo In-na in lead.  Written by Park Ji-eun, it is a romantic fantasy story about an alien who landed on Earth in the Joseon Dynasty and, 400 years later, falls in love with a top actress in the modern era.  It aired on SBS from December 18, 2013 to February 27, 2014 on Wednesdays and Thursdays at 22:00 for 21 episodes; the production company extended the original 20-episode run with one episode, due to high viewers' demand.

Rhodora X: Rhodora X is a 2014 Philippine psychological suspense television series broadcast by GMA Network starring Jennylyn Mercado, Mark Herras, Yasmien Kurdi & Mark Anthony Fernandez, with Glydel Mercado, Boots Anson-Roa and Gardo Versoza.  It premiered on January 27, 2014 on the network's primetime block and worldwide via GMA Pinoy TV on January 28, 2014.  The series centers on Rhodora, a woman suffering from Dissociative Identity Disorder and how the situation affects all the people around her especially her sister, Angela.  The series ended on May 30, 2014 and was replaced by "Ang Dalawang Mrs. Real" on its timeslot and completed 18 weeks with a total of 88 episodes.

Question: Which South Korean television series will be remade into a Philippine movie starring Jennylyn Mercado?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "original_south_korean_series_title": {
      "type": "string",
      "description": "The title of the original South Korean television series."
    },
    "philippine_remake_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the Philippine remake."
        },
        "type": {
          "type": "string",
          "description": "The format of the Philippine remake (e.g., 'television series', 'film')."
        },
        "starring_actress": {
          "type": "string",
          "description": "The main actress starring in the Philippine remake."
        }
      },
      "required": [
        "title",
        "type",
        "starring_actress"
      ],
      "additionalProperties": false
    },
    "answer_series_title": {
      "type": "string",
      "description": "The title of the South Korean series identified as the remake."
    }
  },
  "required": [
    "original_south_korean_series_title",
    "philippine_remake_details",
    "answer_series_title"
  ],
  "additionalProperties": false
}
