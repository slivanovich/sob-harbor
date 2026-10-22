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
David Bergman (American writer): David Bergman (born 1950) is an American writer and English professor at Towson University, in Towson, Maryland part of the University System of Maryland.  He was born in Fitchburg, Massachusetts, grew up in Laurelton, New York, and graduated from Kenyon College (1972) and earned a Ph.D. from Johns Hopkins University (1978).

Chuth Khay: Chuth Khay / ខ្ជិត ខ្យៃ (ហៅ ជុតខៃ) is a Cambodian writer and translator.  He was born in 1940 in Koh Somrong, Cambodia, an island on the Mekong about one hundred kilometers north of the capital.  The youngest son, he was the only one in a family of ten children to attend a Western school.  He pursued primary and secondary studies in Kampong Cham.  While working as a teacher of French, he attended classes at the Royal University of Phnom Penh, and in 1968, received his law degree.  Opposed to the monarchy, he became a legal advisor to the Ministry of Defense after Sihanouk's removal from power in 1970.  From 1973 to 1974 , he served as interim dean of the law school.  In 1973, he published two successful collections of short stories: "Ghouls, Ghosts, and Other Infernal Creatures" and "Widow of Five Husbands".  He also wrote for Soth Polin's newspaper, "Nokor Thom" (នគរធំ), and published his books and translations with its publishing house.  Forced into the countryside by the Khmer Rouge, he miraculously escaped death by pretending to be mute.  Granted refuge in France in 1980 and French citizenship, he took the name Chuth Chance, for receiving a second chance in life.  He worked for several years as a taxi driver, and is now retired and lives near Paris.

Matt Selman: Matthew "Matt" Selman (born September 9, 1971) is an American writer and producer.  Selman grew up in Massachusetts, attended the University of Pennsylvania and was editor-in-chief of student magazine "34th Street Magazine".  After considering a career in journalism, he decided to try to become a television writer.  After two years of failed spec scripts he was eventually hired to write an episode of "Seinfeld" in 1996.  Selman then joined the writing staff of "The Simpsons", where he has remained, rising to the position of executive producer.  He has written numerous episodes of the show, including "Natural Born Kissers", "Behind the Laughter", "Trilogy of Error", "Simpsons Bible Stories" (for which he won an Annie Award), "The Dad Who Knew Too Little" (for which he won a Writers Guild of America Award), and also "The Food Wife".  He also co-wrote the 2007 film adaptation of the show, as well as the video games "", "The Simpsons Hit and Run" and "The Simpsons Game".

Anita Shreve: Anita Shreve (born 1946) is an American writer.  The daughter of an airline pilot and a homemaker, she graduated from Dedham High School in Massachusetts, attended Tufts University and began writing while working as a high school teacher in Reading, Massachusetts.  One of her first published stories, "Past the Island, Drifting", (published in 1975) was awarded an O. Henry Prize in 1976.

Judy Budnitz: Judy Budnitz (born 1973) is an American writer.  She grew up in Atlanta, Georgia, attended Harvard University, was a fellow at Provincetown Fine Arts Work Center, and in 1998 received an MFA in creative writing from New York University.

Husbands and Knives: "Husbands & Knives" is the seventh episode of "The Simpsons"<nowiki>'</nowiki> nineteenth season.  It first aired on the Fox network in the United States on November 18, 2007.  It features guest appearances from Alan Moore, Art Spiegelman, and Dan Clowes as themselves and Jack Black as Milo.  It was written by Matt Selman and directed by Nancy Kruse.  The title is a reference to the Woody Allen film "Husbands and Wives".

Richard Appel: Richard James Appel (born May 21, 1963) is an American writer, producer and former attorney.  Since 2012, he has served as an Executive Producer and co-showrunner of "Family Guy" on Fox.  Growing up in Wilmette, Illinois, Appel developed a love of comedy and dreamed of a career as a comedy writer; he attended Harvard University and wrote for the "Harvard Lampoon".  Following in his mother's footsteps, Appel instead became a lawyer.  After attending law school he started out as a law clerk for Judge John M. Walker, Jr. before becoming a federal attorney, serving as assistant U.S. attorney for the United States District Court for the Southern District of New York for three years.  In 1994, he moved into comedy writing when he was hired for "The Simpsons", writing seven episodes of the show including "Mother Simpson".  He moved on to become showrunner and executive producer of "King of the Hill" before creating the sitcom "A.U.S.A.".  He then worked on "The Bernie Mac Show", "Family Guy" and "American Dad! " before co-creating "The Cleveland Show".  He was married to the writer Mona Simpson.

Daniel Hart Donoghue: Daniel Hart Donoghue (born January 17, 1975) is an American actor, screenwriter and producer.  Donoghue was born in Holyoke, Massachusetts and moved to Lowell, Massachusetts at the age of four where he lived with his parents, Daniel and Kathleen, and one brother, Brian.  He is of Irish descent.  Donoghue attended the University of Massachusetts Amherst and the University of Limerick, Ireland where he studied literature and writing.  In his twenties, Donoghue was an English Teacher on the reservation of the Jicarilla Apache Nation, in Dulce, New Mexico and then at Lowell High School in his hometown of Lowell, Massachusetts.  In his thirties, Donoghue began a career as a stage actor and writer.  His first notable work as a screenwriter was Paradox Lost produced by EDGY Pictures, HDNM Entertainment, and Satyr Entertainment.  In addition to writing the feature screenplay, which is based on Donoghue's award winning short film screenplay originally titled Gunmetal Rose, Donoghue Co-Directed, Produced and played a leading role In Paradox Lost in 2015.

Ethan Gilsdorf: Ethan Gilsdorf is an American writer, poet, editor, critic, teacher and journalist.  He was born in Dover, New Hampshire, and raised in the nearby town of Lee.  He has lived in Northampton and Amherst, Massachusetts; Brattleboro, Vermont; Baton Rouge, Louisiana; Paris, France; and currently lives in Somerville, Massachusetts.  He attended Oyster River High School in Durham, New Hampshire, and received his B.A. from Hampshire College and his MFA from Louisiana State University.

Berge Bulbulian: Berge Bulbulian (born November 10, 1925) is an American writer of Armenian descent.  Born in Mexico, he grew up in the Del Ray area in a farm.  He served in the Navy of the United States during World War II.  He attended Fresno State College.  He continued his studies at UCLA and graduated in 1950 with a B.A. in philosophy.  During the 1970s he was president of a local Fresno grassroots group National Land for People (1974), formerly the Western Water Resources Council.  In 1990 he became an editorial writer for "The Fresno Bee" and started work on "The Fresno Armenians: History of a Diaspora Community" (2000).  a book written by him published in November 2001 and published by the California State University, Fresno Press has been an important scholarly research into the Fresno Armenian community.

Question: Husbands & Knives was written by an AMerican writer and producer who grew up in Massachusetts and attended what university?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "writer_name": {
      "type": "string",
      "description": "The name of the writer of the episode."
    },
    "writer_occupation": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The occupations of the writer."
    },
    "writer_origin_state": {
      "type": "string",
      "description": "The state where the writer grew up."
    },
    "university_attended": {
      "type": "string",
      "description": "The name of the university the writer attended."
    }
  },
  "required": [
    "writer_name",
    "writer_occupation",
    "writer_origin_state",
    "university_attended"
  ],
  "additionalProperties": false
}
