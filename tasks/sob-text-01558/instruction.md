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
Cassandra Cass: Cassandra Cass (born 1977/1978) is an American actress and performer and reality-television star.  She is known for being a trans woman, and finds that performing in the entertainment world gives validation to her transgender life.

Jeff Hephner: Jeffrey Lane "Jeff" Hephner (born June 22, 1975) is an American actor, known for his recurring role as Matt Ramsey in the third season of the Fox drama "The O.C." (2005-2006) and starring as Morgan Stanley Buffkin in the short-lived CW comedy-drama "Easy Money" (2008-2009).  He had a recurring role as football coach Red Raymond in the short-lived CW drama "Hellcats" and co-starred as Ben Zajac in the Starz political drama "Boss" (2011–2012) with Kelsey Grammer.  In 2015, he starred as John Case in the short-lived TNT action drama "Agent X".  Hephner had a recurring role as firefighter-turned-medical student Jeff Clarke in NBC's "Chicago" franchise in the original drama "Chicago Fire" from 2013 to 2014 and reprised his role in the show's medical drama spin-off "Chicago Med" from 2016 to 2017.

Hilarie Burton: Hilarie Ross Burton (born July 1, 1982) is an American actress and producer.  A former host of MTV's "Total Request Live", she portrayed Peyton Sawyer on the The WB/CW drama "One Tree Hill" for six seasons (2003–09).  Burton gained wider recognition with leading roles in the films "Our Very Own", "Solstice" and "The List".  She starred as Sara Ellis on the USA crime drama "White Collar" (2010–13); and, in 2013, she had a recurring role as Dr. Lauren Boswell on the ABC medical drama "Grey's Anatomy".  In 2014, she appeared in the short-lived ABC drama series "Forever" as Molly Dawes, and a recurring role in the short-lived CBS sci-fi drama series "Extant" as Anna Schaefer in 2015.  In 2016, Burton was cast in a recurring role as DEA Agent Karen Palmer on the Fox action dramedy series "Lethal Weapon".

John Pappas: John Pappas (born November 11, 1951) is an American actor, playwright and former comic who has appeared on television and in film since the 1970s.  Pappas is best known for his recurring role as "Pappas" on the television series Hardball (NBC 1989-1990).  Pappas is also known for his recurring role of Leo Sullivan on the NBC Soap Opera "Days of Our Lives" (NBC1994).  In 2001 Pappas returned to "Days of Our Lives" in another recurring role of a convict named "Buddy".  Pappas is an award-winning actor receiving a 1990 best actor award from the L.A. Weekly, for his performance in Gilbert Girion’s BAD COUNTRY.  He received 2 Drama-Logue awards, one in 1989 and another in 1988.

Jonathan Cheban: Jonathan Cheban (born c. 1974) is a reality-television star and entrepreneur.  He is noted for his recurring role on the show "Keeping Up with the Kardashians" and its spinoffs.

Toby Sheldon: Tobias "Toby" Sheldon (born Tobias Strebel; 1980 – August 21, 2015) was a German songwriter who became a television reality star noted for having paid extraordinary amounts for plastic surgery (he himself estimated the total cost at over $100,000) in order to resemble singer Justin Bieber.  He appeared on the television shows "Botched" on the E! network and "My Strange Addiction" on TLC.  Some experts argued that Sheldon's obsession was a case of body dysmorphia.  This topic was discussed in depth during his appearance alongside Justin Jedlica ("The Human Ken Doll") on the talk show "Bethenny".

Nach Baliye: Nach Baliye ('Nach' means Dance and 'Baliye' means partner or mate) is a dance, reality-television series on the Indian channel Star Plus.  The show is a popular couples dancing contest.  The first and second season aired on Star One and then shifted to Star Plus.

Evan Bass: Evan Bass an American businessperson and reality-television star.  He is the founder and director of several male erectile dysfunction clinics in Tennessee and a principal at MMM, LLC.  Bass was a contestant on the American realty-TV shows "The Bachelorette" and "Bachelor in Paradise".

By Any Means (film): By Any Means is an American thriller directed by Leighton Spence and starring Brooke Burfitt, Thomas Gipson, Jonathan Cheban and Michelle Money.  The film had its first screening in Ireland before a run of international film festivals around the world in 2016.  Gravitas Ventures acquired the distribution rights of the film; which will be released by video on demand and on DVD on June 27, 2017.

John Amos: John Allen Amos Jr. (born December 27, 1939) is an American actor who is best known for his role as James Evans, Sr. on the CBS television series "Good Times" (1974–76).  Amos' other television work includes roles in "The Mary Tyler Moore Show", the miniseries "Roots", for which he received an Emmy nomination, and a recurring role as Admiral Percy Fitzwallace on "The West Wing".  Amos also played the father of Will Smith's character's girlfriend, Lisa Wilkes, in "The Fresh Prince of Bel-Air", and he had a recurring role on "In the House" with LL Cool J, as Coach Sam Wilson.  Amos played the Father of Tommy Strawn (Thomas Mikal Ford) on the long running sitcom, "Martin", as Sgt. Strawn, and another recurring role on "Two and a Half Men" as Chelsea's dad's new lover, Edward Boynton.  Amos also played Major Grant, the US Special forces officer in "Die Hard 2".  Amos has also appeared on Broadway and in numerous films in a career that spans four decades.  He has received nominations for a Primetime Emmy Award and NAACP Image Award.

Question:  By Any Means is an American thriller staring a reality-television star noted for his recurring role on what show?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "starring_reality_tv_star": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the reality-television star who starred in the film."
        },
        "noted_for_show": {
          "type": "string",
          "description": "The name of the reality-television show the star is noted for."
        }
      },
      "required": [
        "name",
        "noted_for_show"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_genre",
    "starring_reality_tv_star"
  ],
  "additionalProperties": false
}
