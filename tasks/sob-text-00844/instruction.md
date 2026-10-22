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
Demolition (2015 film): Demolition is a 2015 USA drama film directed by Jean-Marc Vallée and written by Bryan Sipe.  The film stars Jake Gyllenhaal, Naomi Watts, Chris Cooper, and Judah Lewis.  The film opened the 2015 Toronto International Film Festival and was theatrically released on April 8, 2016, by Fox Searchlight Pictures.

Yves Bélanger (cinematographer): Yves Bélanger (born July 7, 1960) is a Canadian cinematographer.  He has worked on films by directors such as Alain Desrochers and Xavier Dolan, and he is a frequent collaborator of Jean-Marc Vallée.  In 2016, he received a Canadian Screen Award for Best Cinematography for his work in "Brooklyn".

2015 Toronto International Film Festival: The 40th annual Toronto International Film Festival was held from 10 to 20 September 2015.  On 28 July 2015 the first wave of films to be screened at the Festival was announced.  Jean-Marc Vallée's "Demolition" starring Jake Gyllenhaal and Naomi Watts was the opening night film; "Mr. Right" by Paco Cabezas was the closing night film.

François Boulay: François Boulay is a Canadian film and television screenwriter, best known as cowriter with Jean-Marc Vallée of the 2005 film "C.R.A.Z.Y." and as a writer for the Quebec television drama series "Providence".

Wild (2014 film): Wild is a 2014 American biographical survival drama film directed by Jean-Marc Vallée.  The screenplay by Nick Hornby is based on Cheryl Strayed's 2012 memoir "".  The film stars Reese Witherspoon as Strayed, alongside Laura Dern (as Strayed's mother), with Thomas Sadoski, Michiel Huisman and Gaby Hoffmann among several others in supporting roles.  The film premiered at the Telluride Film Festival on August 29, 2014, and was released theatrically on December 3, 2014, in North America.

Hugh Hudson: Hugh Hudson (born 25 August 1936) is an English film director.  He was among a generation of British directors who would begin their career making documentaries and television commercials before going on to have success in films.  Hudson directed the 1981 Academy Award and BAFTA Award Best Picture "Chariots of Fire", a film ranked 19th in the British Film Institute's list of Top 100 British films.

Martin Pensa: Martin Pensa is a film editor.  Pensa and fellow film editor Jean-Marc Vallée (as John Mac McMurphy) were nominated for the Academy Award for Best Film Editing for the 2013 film "Dallas Buyers Club".

Jean-Marc Vallée: Jean-Marc Vallée (born March 9, 1963) film director, screenwriter, and film editor from Québec, Canada.  After studying film at the Université du Québec à Montréal, Vallée went on to make a number of acclaimed short films, including "Stéréotypes" (1991), "Les Fleurs magiques" (1995), and "Les Mots magiques" (1998).

List of accolades received by The Young Victoria: "The Young Victoria" is a 2009 period drama film directed by Jean-Marc Vallée and written by Julian Fellowes.  It centered on the early life and reign of Queen Victoria, including her relationship with her husband, Prince Albert.  The film starred Emily Blunt and Rupert Friend among a large ensemble cast.  Martin Scorsese, Graham King, and Sarah, Duchess of York served as its producers.  A GK Films production, "The Young Victoria" was distributed by Momentum Pictures in the United Kingdom and by Apparition in the United States.  Its world premiere was held on 5 February 2009 at the 59th Berlin International Film Festival while its UK premiere was held in London's Leicester Square on 3 March.  The film was screened throughout 2009 and early 2010 at film festivals in Toronto, Sudbury, Ontario, Chicago, Hamptons, New York, Vermont, San Francisco, Denver, and San Joaquin, California.  "The Young Victoria"' s theatrical release occurred on 6 March 2009 in the UK; it was released in a limited capacity in the US on 18 December 2009, and opened nationwide on Christmas Day.  It earned a worldwide gross of $27,409,889.

C.R.A.Z.Y.: C.R.A.Z.Y. is a 2005 French-language Canadian coming-of-age drama film directed by Jean-Marc Vallée and co-written by Vallée and François Boulay.  It tells the story of Zac, a young gay man dealing with homophobia while growing up with four brothers and a conservative father in Quebec during the 1960s and 1970s.  The film employs an extensive soundtrack, featuring artists such as Pink Floyd, Patsy Cline and The Rolling Stones.

Question: Are Hugh Hudson and Jean-Marc Vallée both film directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_directors": {
      "type": "boolean",
      "description": "True if both individuals are film directors, false otherwise."
    },
    "directors_involved": {
      "type": "array",
      "description": "Details about the individuals mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_film_director": {
            "type": "boolean",
            "description": "True if the context confirms this individual is a film director."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the individual."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the individual, if available."
          }
        },
        "required": [
          "name",
          "is_film_director",
          "nationality",
          "birth_date"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the answer based on the provided context."
    }
  },
  "required": [
    "are_both_directors",
    "directors_involved",
    "reasoning"
  ],
  "additionalProperties": false
}
