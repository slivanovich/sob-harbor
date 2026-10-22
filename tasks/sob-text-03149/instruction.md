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
Honkytonk Man: Honkytonk Man is a 1982 American musical drama film set in the Great Depression.  Clint Eastwood, who produced and directed, stars with his son, Kyle Eastwood.  Clancy Carlile's screenplay is based on his novel of the same name.  This was Marty Robbins' last appearance before he died.  The story of Eastwood's character, Red Stovall is loosely based on the life of Jimmie Rodgers.

High Plains Drifter: High Plains Drifter is a 1973 American Western film directed by and starring Clint Eastwood, written by Ernest Tidyman, and produced by Robert Daley for Malpaso Company and Universal Pictures.  Eastwood plays a mysterious, prepotent stranger, meting out justice in a corrupt frontier mining town.  The film was influenced by the work of Eastwood's two major collaborators, film directors Sergio Leone and Don Siegel.

The Rookie (1990 film): The Rookie is a 1990 American buddy cop film directed by Clint Eastwood and produced by Howard G. Kazanjian, Steven Siebert and David Valdes.  It was written from a screenplay conceived by Boaz Yakin and Scott Spiegel.  The film stars Charlie Sheen, Clint Eastwood, Raúl Juliá, Sônia Braga, Lara Flynn Boyle, and Tom Skerritt.  Eastwood plays a veteran police officer teamed up with a younger detective played by Sheen ("the rookie"), whose intent is to take down a German crime lord in downtown Los Angeles following months of investigation into an exotic car theft ring.

Mystic River (film): Mystic River is a 2003 American mystery crime drama film directed and scored by Clint Eastwood.  It stars Sean Penn, Tim Robbins, Kevin Bacon, Laurence Fishburne, Marcia Gay Harden, and Laura Linney.  The screenplay by Brian Helgeland was based on the novel "Mystic River" by Dennis Lehane.  The film was produced by Robert Lorenz, Judie G. Hoyt and Eastwood.  It is the first film on which Eastwood was credited as composer of the score.

Unforgiven: Unforgiven is a 1992 American revisionist Western film produced and directed by Clint Eastwood and written by David Webb Peoples.  The film portrays William Munny, an aging outlaw and killer who takes on one more job years after he had turned to farming.  The film stars Eastwood in the lead role, with Gene Hackman, Morgan Freeman and Richard Harris.  Eastwood stated that the film would be his last Western for fear of repeating himself or imitating someone else's work.

Mrs. Schlorer's: Mrs. Schlorer's was the brand name for mayonnaise and numerous other food condiments originally manufactured by the Schlorer Delicatessen Company in Philadelphia, PA.  Mrs. Schlorer's Mayonnaise is credited as being the first mayonnaise put in jars and sold commercially in 1907.  The first products trademarked by the Schlorer Delicatessen Company were Mrs. Schlorer's Mayonnaise and Mrs. Schlorer's Olivenaise in 1917.

Francesca Eastwood: Francesca Ruth Fisher-Eastwood (born August 7, 1993) is an American actress, model, television personality and socialite.  She is known for starring in "Mrs. Eastwood & Company", the E! reality series that she shares with her family.

Mrs. Wiggins: "Mrs. Wiggins" (also known as "Mr. Tudball and Mrs. Wiggins") is a series of comedy sketches featured on "The Carol Burnett Show", with one installment airing on "Carol Burnett & Company".  "The Carol Burnett Show" introduced the skit series during its ninth season in 1975–76 and continued to air new installments of the skit for the remainder of its 11-season run, through its final season in 1977–78.  However, the final installment of "Mrs. Wiggins" would not air until August 18, 1979, on a different four-week summer series titled "Carol Burnett & Company".  This was the only installment of "Mrs. Wiggins" that did not air on "The Carol Burnett Show" which had completed its run almost a year and a half earlier on March 29, 1978.  Altogether, there were 19 installments of "Mrs. Wiggins" sketches.

Mrs. Eastwood &amp; Company: Mrs. Eastwood & Company is an American reality documentary television series that premiered May 20, 2012, on E!.  The show chronicled the lives of Dina Eastwood, the then wife of actor/director Clint Eastwood, and their daughters, Francesca and Morgan.  Mrs. Eastwood manages the six-person a cappella group Overtone, who also live with the Eastwoods in their Carmel-by-the-Sea, California, mansion.

Tieks: Tieks is an American footwear brand founded in 2008.  The company is headquartered in Los Angeles and sells its shoes, known as “Tieks,” exclusively through its website.  Tieks feature a split-sole design, allowing the shoes to fold in half.  Tieks have been worn by many celebrities including Oprah Winfrey, Alessandra Ambrosio, Francesca Eastwood, Hailee Steinfeld, Tina Fey, Candace Cameron Bure and Chelsea Clinton.

Question: What celebrity wears Tieks and stars in "Mrs. Eastwood & Company"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "celebrity_name": {
      "type": "string",
      "description": "The name of the celebrity who meets the criteria."
    },
    "tv_show_starred_in": {
      "type": "string",
      "description": "The name of the TV show the celebrity starred in."
    },
    "shoe_brand_worn": {
      "type": "string",
      "description": "The name of the shoe brand the celebrity wears."
    }
  },
  "required": [
    "celebrity_name",
    "tv_show_starred_in",
    "shoe_brand_worn"
  ],
  "additionalProperties": false
}
