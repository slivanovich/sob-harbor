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
Macklemore: Benjamin Hammond Haggerty (born June 19, 1983), known by his stage name Macklemore ( ), and formerly Professor Mack Lemore, is an American rapper from Seattle, Washington.  He has collaborated with producer Ryan Lewis as Macklemore & Ryan Lewis.  Since 2000, he has independently released one mixtape, three EPs, and four albums.

Brad Pitt's Cousin: "Brad Pitt's Cousin" is a song by American hip hop duo Macklemore & Ryan Lewis featuring American rapper Xperience (XP) from their third studio album "This Unruly Mess I've Made" (2016).  The song was released as promotional single on April 12, 2016 as the third single only in Australia and New Zealand.  The song was not released in the United States or Europe.

Hollis (singer): Hollis Wong-Wear, known mononymously as Hollis, is an American singer-songwriter and creative producer.  She is best known for featuring on "White Walls", a song by Macklemore and Ryan Lewis, which also featured Schoolboy Q.  Hollis is also a spoken-word artist.  Her major debut was on Macklemore & Ryan Lewis' debut album, "The Heist".  This was followed by the single "White Walls" in which she did the vocals for Macklemore and Ryan Lewis.  This song peaked at number 15 on the Billboard Hot 100 chart.

This Unruly Mess I've Made: This Unruly Mess I've Made is the second studio album by American hip hop duo Macklemore & Ryan Lewis.  It was released on February 26, 2016, by Macklemore LLC and Alternative Distribution Alliance.  The album was supported by three singles: "Downtown" featuring Eric Nally, Melle Mel, Kool Moe Dee and Grandmaster Caz and "Dance Off" featuring Idris Elba and Anderson Paak, along with "White Privilege II" featuring Jamila Woods, which was released as the album's promotional single.

White Privilege II: "White Privilege II" is a song by American hip hop duo Macklemore & Ryan Lewis from their second album "This Unruly Mess I've Made" (2016).  The song, a sequel to Macklemore's solo song "White Privilege" from his first album "The Language of My World" (2005), discusses white privilege and the social movement associated with Black Lives Matter.  According to the duo, "this song is the outcome of an ongoing dialogue with musicians, activists, and teachers within our community in Seattle and beyond.  Their work and engagement was essential to the creative process."  The song's lyrics span around nine minutes and 1300 words.  One of the project's collaborators is Chicago singer Jamila Woods, whose voice is featured on the track.  "White Privilege II" was released as promotional single on January 22, 2016.

Dance Off: "Dance Off" is a song by American hip hop duo Macklemore & Ryan Lewis featuring British actor and musician Idris Elba and American recording artist Anderson . Paak from their second studio album "This Unruly Mess I've Made" (2016).  The song was officially released on February 25, 2016 as the second single only in Australia, New Zealand and selected countries of Europe.  The song was not released in the United States.

Ben Abraham (musician): Ben Abraham is an Australian folk singer and songwriter from Melbourne.  Ben is notable for collaborating with top artists such as: Kesha, Macklemore & Ryan Lewis, Demi Lovato and Sara Bareilles.  His powerful hit song "Praying" by Kesha (which he co-wrote with Kesha and Ryan Lewis) has created an impactful buzz with tastemakers worldwide.

Macklemore &amp; Ryan Lewis: Macklemore & Ryan Lewis are an American hip hop duo, formed in 2008, from Seattle, Washington.  The duo is composed of Ben Haggerty, a rapper who goes by the stage name of Macklemore, and Ryan Lewis, a record producer, DJ, and professional photographer, who met the former at a photo shoot and they have significantly collaborated ever since.  In 2009, they released their first collaborative effort, an EP titled "VS. EP".  They have since followed up with "VS. Redux" (2010), the Grammy Award-winning album "The Heist" (2012) and "This Unruly Mess I've Made" (2016).

Downtown (Macklemore &amp; Ryan Lewis song): "Downtown" is a song by American hip hop duo Macklemore & Ryan Lewis featuring Eric Nally, Melle Mel, Kool Moe Dee, and Grandmaster Caz.  The song was officially released on August 27, 2015 as the lead single from their second studio album "This Unruly Mess I've Made" (2016).  A music video for the song was uploaded to Ryan Lewis' own YouTube channel on the day of the song's release.

Ryan Lewis: Ryan S. Lewis (born March 25, 1988) is an American DJ, musician, record producer, videographer, photographer, graphic designer, music video director, and rapper.  Along with producing his own album titled "Instrumentals", Lewis produced the albums "The VS. EP" (2009), "The Heist" (2012), and "This Unruly Mess I've Made" (2016) as part of the duo Macklemore & Ryan Lewis.  In 2006, Lewis befriended rapper Macklemore on Myspace and soon after became the behind-the-scenes partner of a successful duo, producing, recording, engineering and mixing all of the duo's music, as well as directing the music videos for "Same Love", "Thrift Shop", "And We Danced", "Otherside (Remix)", "Can't Hold Us", "Irish Celebration", "My Oh My", "Victory Lap", "Downtown" "Brad Pitt's Cousin" and "White Walls" and designing promotional graphics.

Question: What is the birth name of Ryan Lewis's partner on "This Unruly Mess I've Made"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "partner_stage_name": {
      "type": "string",
      "description": "The stage name of Ryan Lewis's partner."
    },
    "partner_birth_name": {
      "type": "string",
      "description": "The birth name of Ryan Lewis's partner."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album mentioned in the question."
    }
  },
  "required": [
    "partner_stage_name",
    "partner_birth_name",
    "album_name"
  ],
  "additionalProperties": false
}
