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
The Hit (1984 film): The Hit is a 1984 British road crime film directed by Stephen Frears and starring John Hurt, Terence Stamp, Laura del Sol and Tim Roth.  The film was Stamp's first starring role in over a decade and Roth won an Evening Standard award as an apprentice hit man.

James E. Roberts: James E. Roberts (November 30, 1930 - July 6, 2006) was a noted American civil engineer.  He was recognized with industry and government awards for his leadership in bridge engineering, especially in the area of seismic retrofit.  He was the state bridge engineer at Caltrans during the Loma Prieta earthquake and Northridge earthquake.  His public service career lasted more than 50 years in the US Army, US Army Reserves and Caltrans.  Roberts career spanned over 50 years and covered some of the most active years for engineering experienced in California from the design and construction heyday of the 50’s and 60’s to his leadership during the reconstruction efforts and seismic retrofitting programs created after two significant California earthquakes the 1989 Loma Prieta earthquake and the 1994 Northridge earthquake.

John Hurt: Sir John Vincent Hurt, {'1': ", '2': ", '3': ", '4': "} (22 January 1940 – 25 January 2017) was an English actor whose screen and stage career spanned more than 50 years.  Hurt was regarded as one of Britain's finest actors; director David Lynch described him as "simply the greatest actor in the world".

Glenn Ford: Gwyllyn Samuel Newton "Glenn" Ford (May 1, 1916 – August 30, 2006) was a Canadian-born actor who held dual Canadian and American citizenship.  His career lasted more than 50 years.  Although he played many different roles, Ford was best known for playing ordinary men in unusual circumstances.  He was most prominent during Hollywood's Golden Age.

Dubliners 50 Years Anniversary Tour: The Dubliners 50th Anniversary Tour was a tour in 2012 by The Dubliners celebrating 50 years.  The group was awarded a lifetime achievement award by BBC Radio 2 in February.  However, in April, founding member and tenor banjo player Barney McKenna died.  Banjo player Gerry O'Connor filled his place until the end of the tour.  In November the group released the album "50 Years" charting in the Irish Top 10.  John Sheahan after 48 years decided he could no longer continue with the band due to the death of Barney McKenna.  In December the group played its final concerts at Vicar Street and were joined on stage by Jim McCann.  The band met with President Michael Higgins in the presidential palace in Dublin.  The group appeared on BBC's "Jools Holland Annual Hootenanny" on New Year's Eve.  With the exception of John Sheahan, the rest of the group continues touring as The Dublin Legends - Spirit of the Dubliners.

Timo Salminen: Timo Salminen (11 July 1952 in Helsinki) is a Finnish cinematographer best known for his artistic work in Aki Kaurismäki's films.  Salminen's father Ville Salminen was a famed Finnish film actor, director, writer and producer whose career began in the 1930s and lasted until the 1980s.  His older step brother Ville-Veikko Salminen was a comedic actor whose career also lasted over 50 years.

Oscar Handlin: Oscar Handlin (September 29, 1915 – September 20, 2011) was an American historian.  As a professor of history at Harvard University for over 50 years, he directed 80 PhD dissertations and helped promote social and ethnic history, virtually inventing the field of immigration history in the 1950s.  Handlin won the 1952 Pulitzer Prize for History for "The Uprooted" (1951).  Handlin's 1965 testimony before Congress was said to "have played an important role" in passage of the Immigration and Nationality Act of 1965 that abolished the discriminatory immigration quota system in the U.S.

Naga Story: The Other Side of Silence: Naga Story: The Other Side of Silence is a 2003 documentary film by Indian film maker Gopal Menon.  The film provides an introduction to the history of the Struggle by Naga people in North- East frontier of the Indian subcontinent, and documents the human rights abuses suffered by the Naga people in more than 50 years of the existence of Independent India.  The Naga political struggle is one of the oldest nationality movements in South Asia, continuing till present times.  This film, which took 5 years to complete, is the first comprehensive film about the Naga struggle for identity, peace, and justice.

Eden Is West: Eden Is West (French: "Eden à l'ouest" ) is a 2009 film by Greek-French director Costa-Gavras about an illegal immigrant called Elias who tries to get to Paris.  The original title in Greek is “Paradissos sti Dysi” (“Paradise in West”) and since it is a Greek-French production, the also original French title is “Eden à l'ouest'.  The nationality of the central hero is not disclosed because Gavras wants to make a point about the odysseys of the illegal immigrants of any nationality, since he himself was an immigrant 50 years ago in France, before he became a well known director.  His hero seems to tolerate the sea, the cold of snowy mountains and the hunger, the rapists and robbers he meets, the cops that are after him all the time, the racists who push him aside, the fellow immigrants who steal his clothes and in the best case the women who see him as a lover they could also take advantage of.  His only comfort is his dream of Paris and, in the complexity of human condition, the good within the evil and vice versa.

Ralph Richardson, roles and awards: Sir Ralph Richardson (1902–1983) was an English actor who appeared on radio, film, television and stage.  Described by "The Guardian" as "indisputably our most poetic actor", and by the director David Ayliff as "a natural actor ... [who] couldn't stop being a perfect actor", Richardson's career lasted over 50 years.  He was—in the words of his biographer, Sheridan Morley—one "of the three great actor knights of the mid-twentieth century", alongside Laurence Olivier and John Gielgud.

Question: What nationality was the actor who played in The Hit and had a career that lasted more than 50 years?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film the actor played in."
    },
    "career_duration_years": {
      "type": "integer",
      "description": "The duration of the actor's career in years."
    },
    "career_duration_description": {
      "type": "string",
      "description": "A textual description of the actor's career duration from the context."
    }
  },
  "required": [
    "actor_name",
    "nationality",
    "film_title",
    "career_duration_years",
    "career_duration_description"
  ],
  "additionalProperties": false
}
