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
Crossfire (film): Crossfire is a 1947 film noir drama film which deals with the theme of anti-Semitism, as did that year's Academy Award for Best Picture winner, "Gentleman's Agreement".  The film was directed by Edward Dmytryk and the screenplay was written by John Paxton, based on the 1945 novel "The Brick Foxhole" by screenwriter and director Richard Brooks.  The film features Robert Mitchum, Robert Young, Robert Ryan and Gloria Grahame.  It received five Academy Award nominations, including Ryan for Best Supporting Actor and Gloria Grahame for Best Supporting Actress.  It was the first B movie to receive a best picture nomination.

Tony Award for Best Featured Actress in a Play: The Best Performance by a Featured Actress in a Play is an honor presented at the Tony Awards, a ceremony established in 1947 as the Antoinette Perry Awards for Excellence in Theatre, to actresses for quality supporting roles in a Broadway play.  The awards are named after Antoinette Perry, an American actress who died in 1946.  Honors in several categories are presented at the ceremony annually by the Tony Award Productions, a joint venture of The Broadway League and the American Theatre Wing, to "honor the best performances and stage productions of the previous year."  Originally called the Tony Award for Actress, Supporting or Featured (Dramatic), it was later changed to its current title in 1976.  Before 1956, nominees' names were not made public.  The change was made by the awards committee to "have a greater impact on theatregoers".

All the Way to the Ocean: All the Way to the Ocean is a 2016 computer animated short film based on the children's book of the same name by Joel Harper.  The screenplay was written by Joel Harper, Pete Michels, and Doug Rowell.  The film was directed by Doug Rowell and produced by Joel Harper.  The film is narrated by American actress Marcia Cross and features the song With My Own Two Hands by Ben Harper (brother of) Joel Harper.  This is an alternate version of the original song featuring Jack Johnson and is also featured on the Curious George film soundtrack "Sing-A-Longs and Lullabies for the Film Curious George".  The lyrics focus on how changes in the world can come about when a single person decides to take action.  The song's popularity in Europe was such that Ben Harper was awarded French "Rolling Stone Magazine"'s "Artist of the Year" (Artiste De L'Année) in 2003.  The film also features music by Joel Harper and Burning Spear with their collaboration on the song The Time is Now.  The film stars voice-overs by actress and activist Amy Smart and Australian musician Xavier Rudd.

Lainie Kazan: Lainie Kazan (born May 15, 1940) is an American actress and singer.  She was nominated for the 1988 Primetime Emmy Award for Outstanding Guest Actress in a Drama Series for "St. Elsewhere", and the 1993 Tony Award for Best Featured Actress in a Musical for "My Favorite Year".  She had previously received a Golden Globe Award nomination for the film version of "My Favorite Year" (1982).  Her other film appearances include "The Delta Force" (1986), "Harry and the Hendersons" (1987), "Beaches" (1988), "My Big Fat Greek Wedding" (2002) and "My Big Fat Greek Wedding 2" (2016).

Jennifer Ehle: Jennifer Anne Ehle ( ; born December 29, 1969) is an American actress.  She won the BAFTA TV Award for Best Actress for her role as Elizabeth Bennet in the 1995 BBC miniseries "Pride and Prejudice".  For her work on Broadway, she won the 2000 Tony Award for Best Actress in a Play for "The Real Thing", and the 2007 Tony Award for Best Featured Actress in a Play for "The Coast of Utopia".  She is the daughter of English actress Rosemary Harris and American author John Ehle.

Jacqueline White: Jacqueline Jane White (born November 27, 1922) is a former American film actress.  She's probably best remembered appearing in the films noir "Crossfire" and "The Narrow Margin".

Gloria Grahame: Gloria Grahame (November 28, 1923 – October 5, 1981) was an American stage, film and television actress.

Saycon Sengbloh: Saycon Sengbloh (born October 23, 1977) is an American actress and singer.  She was nominated for a Tony Award for Best Featured Actress in a Play and won a Drama Desk Award for Outstanding Featured Actress in a Play for her performance in Danai Gurira' play "Eclipsed" in 2016.

Blythe Danner: Blythe Katherine Danner (born February 3, 1943) is an American actress.  She won two Primetime Emmy Awards for Best Supporting Actress in a Drama Series for her role as Izzy Huffstodt on "Huff" (2004–2006), and a Tony Award for Best Featured Actress in a Play for her performance in "Butterflies Are Free" (1969–1972).  Danner was nominated for two Primetime Emmy Awards for Outstanding Guest Actress in a Comedy Series for portraying Marilyn Truman on "Will & Grace" (2001–2006), and the Primetime Emmy Award for Outstanding Lead Actress in a Miniseries or a Movie for her roles in "We Were the Mulvaneys" (2002) and "Back When We Were Grownups" (2004).  For the latter, she was also nominated for the Golden Globe Award for Best Actress – Miniseries or Television Film.

Melody Parra: Melody Marie Tavitian-Parra is an American actress and model.  Born and raised in Los Angeles, California, Parra demonstrated a talent for acting early on.  She began acting in school plays at the age of 6 and continued throughout high school where she won the school's Best Actress Gold Medal, the Musical Theatre Director's Dream Actress Award, and the Best Film Actress Tommy at John Marshall High in Los Feliz.  She made her professional stage debut during her senior year in "What's Shakein?"  (2009) at the Greek Theatre in the play's lead role.  In 2009, Parra was admitted to UCLA with a full merit scholarship.  While pursuing a dual BA, Parra joined the university's prestigious ACT III Theatre Ensemble where she played lead and large supporting roles in classics such as "Othello", "Oedipus Rex", "Macbeth", and "The Fall".  In 2012 she graduated UCLA at the age of 20, receiving her BA in English Literature and Spanish.  She made her feature film debut the following year cast in the lead role of Stella in the indie film drama "City of Quartz" (2013).  The film premiered at the BLOW-UP Arthouse International Film Festival.  That same year she was cast in the comedy "With this Ring" (2013) where she played a supporting role in both the play and its on-screen adaptation.  Parra's other films include the crime drama "Here in the East" (2014), "Fronteras" (2015), "Ouroboros" (2015), and "Edge" (2015).  Both "Here in the East" and "Edge" won Best Film in the 2015 Hollywood Reel Independent Film Festival and the 2015 San Diego Film Festival, respectively.

Question: In what year was the American actress who was featured in the film Crossfire born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "actress_name": {
      "type": "string",
      "description": "The name of the American actress featured in the film."
    },
    "actress_nationality": {
      "type": "string",
      "description": "The nationality of the actress."
    },
    "actress_birth_year": {
      "type": "integer",
      "description": "The birth year of the actress."
    }
  },
  "required": [
    "film_title",
    "actress_name",
    "actress_nationality",
    "actress_birth_year"
  ],
  "additionalProperties": false
}
