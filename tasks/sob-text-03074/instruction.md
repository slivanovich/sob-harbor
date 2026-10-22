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
Peter Sarstedt: Peter Eardley Sarstedt (10 December 1941 – 8 January 2017), briefly billed early in his career as Peter Lincoln, was a British singer, instrumentalist and award-winning songwriter.  He was the brother of musicians Eden Kane and Clive "Robin" Sarstedt.

Lindsay Lohan filmography: Lindsay Lohan is an American actress and singer-songwriter who began her acting career as a child actor in the late-1990s.  At age 11, Lohan made her motion picture debut in Disney's commercially and critically successful 1998 remake of "The Parent Trap".  She continued her acting career by appearing in a number of Disney films, including "Life-Size" (2000), "Get a Clue" (2002), "Freaky Friday" (2003), "Confessions of a Teenage Drama Queen" (2004) and "" (2005), along with her first non-Disney film "Mean Girls" (2004), which became a massive success by grossing over $129 million and later becoming a cult classic film.  Lohan also did smaller, more mature roles in independent movies, receiving positive reviews on her acting, including Robert Altman's "A Prairie Home Companion" (2005), Emilio Estevez's "Bobby" (2006) and Jarrett Schaefer's "Chapter 27" (2007).  Between 2006 and 2007, Lohan continued her career by starring in films like "Just My Luck" (2006), "Georgia Rule" (2007), and "I Know Who Killed Me" (2007).  Lohan's career had faced many interruptions from legal and personal troubles during the mid to late 2000s and 2010s, but she has still been able to appear in 26 films (including 6 as a personality), 12 television appearances, 1 play and 5 music videos.

Abraham Hayward (architect): Abraham Haywood (1692–1747) was an architect who was born at Whitchurch, Shropshire and is likely to have come to Lincoln around 1720 to work for Francis Smith of Warwick on the construction of St Peter at Arches Church, Lincoln.  In 1736 he built the town house of the Disney family, Disney Place in Eastgate Street, Lincoln and in 1744 the Lincoln Assembly Rooms in the Bail, Lincoln.  He also built a house for himself on the east side of St Peter at Arches‘ graveyard on the site of the Lincoln Taylor’s Hall.  Abraham Hayward’s younger brother John Hayward(1708-78), a mason by trade, also accompanied him to Lincoln.  After Abraham’s death, he presumably continued the business and in 1753 rebuilt St Mary’s bridge in Lincoln.  John Hayward’s grandson, William Hayward became surveyor to Lincoln Cathedral.

David Newell (actor, born 1905): David Newell was primarily known as an American character actor, whose acting career spanned from the very beginning of the sound film era through the middle of the 1950s.  He made his film debut in a featured role in "The Hole in the Wall", a 1929 film starring Edward G. Robinson and Claudette Colbert.  Early in his career he had many featured roles, in such films as: RKO's "The Runaway Bride" in 1929, starring Mary Astor; 1931's "Ten Cents a Dance", starring Barbara Stanwyck and directed by Lionel Barrymore; and "White Heat" in 1934.  He would occasionally receive a starring role, as in 1930's "Just Like Heaven", which co-starred Anita Louise.  However, by the mid-1930s he was being relegated to mostly smaller supporting roles.  Some of the more notable films he appeared in include: "A Star is Born" (1937), which stars Janet Gaynor and Fredric March; "Blondie" (1938); the Bette Davis vehicle, "Dark Victory" (1939); "Day-Time Wife" (1939), starring Tyrone Power and Linda Darnell; "It's a Wonderful World" (1939), with James Stewart and Claudette Colbert; "Rings on Her Fingers" (1942), starring Henry Fonda and Gene Tierney; the Danny Kaye and Dinah Shore film, "Up in Arms" (1944), which also stars Dana Andrews; 1947's "Killer McCoy" with Mickey Rooney, Brian Donlevy, and Ann Blyth; "Homecoming" (1948), starring Clark Gable, Lana Turner, and Anne Baxter; "That Wonderful Urge" (1949), starring Tyrone Power and Gene Tierney; "David and Bathsheba" (1951), starring Gregory Peck and Susan Hayward; and Cecil B. DeMille's 1952 blockbuster, "The Greatest Show on Earth".  During his 25-year acting career, he appeared in over 110 films.  His final appearance in film was in 1954's "The Eddie Cantor Story", in which he had a small supporting role.

Morris Carnovsky: Morris Carnovsky (September 5, 1897 – September 1, 1992) was an American stage and film actor.  He was one of the founders of the Group Theatre (1931-1940) in New York City and had a thriving acting career both on Broadway and in films until, in the early 1950s, professional colleagues told the House Un-American Activities Committee that Carnovsky had been a Communist Party member.  He was blacklisted and worked less frequently for a few years, but then re-established his acting career, taking on many Shakespearean roles at the Stratford Shakespeare Festival and performing the title roles in college campus productions of "King Lear" and "The Merchant of Venice".  Carnovsky's nephew is veteran character actor and longtime "Pathmark Guy" James Karen.

Carlos Ponce: Carlos Ponce (born September 4, 1972) is a Puerto Rican actor, singer, composer and television personality.  Ponce began his acting career by participating in Spanish language soap operas for Televisa and Telemundo.  Ponce continued to expand his acting career by participating in various American television series.  He did not limit himself solely to a career in television.  Ponce, who is also a singer, is also active in the American movie industry as a character actor.

Joe Brooks (actor): Joe Brooks (December 14, 1923 – December 5, 2007), born John Joseph Brooks, Jr., was an American character actor best known for portraying Trooper Vanderbilt, the near-sighted soldier, in "F Troop".  He was born and died in Los Angeles, CA and began his acting career after graduating from high school and had his first speaking part in the 1944 John Wayne film, "The Fighting Seabees."  During World War II Brooks put his acting career on hold and served his country fighting in the South Pacific.  He then returned to California and continued to act mainly as an extra and in bit parts until he was called to audition for the role of Vanderbilt.  His career spanned some 22 movies and numerous television appearances over 40 years.  His other credits include the films "East Of Eden" (1955), "Tall Man Riding" (1955), "The Young Lions" (1958), "Born Reckless" (1958), "Flaming Star" (1960), "Robin and the 7 Hoods" (1964), "Pursuit" (1972), "The Bad News Bears" (1976), "Gremlins" (1984), and "Eye of the Tiger" (1986), and the TV shows "Rawhide", "The Six Million Dollar Man", "Bewitched", "The Munsters", and "Cheyenne".

Simon Baker: Simon Baker (born 30 July 1969) is an Australian actor and director.  In his television acting career, he is known for his lead roles in the CBS television series "The Mentalist" (as Patrick Jane) and "The Guardian" (as Nicholas Fallin).  In his film acting career, he is best known for his roles as Max Rourke in the remake of the Japanese horror film "The Ring Two", Riley Denbo in "Land of the Dead" and Christian Thompson in the film adaptation of "The Devil Wears Prada".

Saskia Hampele: Saskia Hampele is an Australian actress.  She began her acting career in 1997 when she appeared in "The Gift".  Hampele worked as a counselor at The Reach Foundation and the Royal Children's Hospital, while pursuing her acting career.  She appeared in the 2008 mockumentary "Mark Loves Sharon" and the two feature films "Arctic Blast" and "Blame" in 2010.  The following year, Hampele made a guest appearance in "City Homicide" and began starring in an online series called "Shutterbugs".  Hampele appeared in the film "6 Plots", and joined the cast of soap opera "Neighbours" as Georgia Brooks in 2012.  She left the show in 2015.

Eden Kane: Eden Kane is the stage name of Richard Graham Sarstedt (born 29 March 1940), and is an English pop singer best known as a former teen idol in the 1960s.  He has also recorded under his birth name and with his backing group the Downbeats.  He is the older brother of musicians Peter Sarstedt and Clive Sarstedt, whom he has collaborated with on numerous Sarstedt Brothers albums.  He had success in the early 1960s as a pop star appealing to a teenage audience with hits including "Well I Ask You" which was a UK No.1 hit in 1961, before moving to the United States, where he began an acting career.

Question: Which of Peter Lincoln's brothers had an acting career?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "brother_name": {
      "type": "string",
      "description": "The name of Peter Lincoln's brother who had an acting career."
    },
    "relationship_to_peter_lincoln": {
      "type": "string",
      "description": "The relationship of the identified person to Peter Lincoln."
    },
    "acting_career_started_location": {
      "type": "string",
      "description": "The location where the acting career began."
    }
  },
  "required": [
    "brother_name",
    "relationship_to_peter_lincoln",
    "acting_career_started_location"
  ],
  "additionalProperties": false
}
