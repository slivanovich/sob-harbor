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
Cyborg 2: Cyborg 2, released in some countries as Glass Shadow, is a 1993 American science fiction action film directed by Michael Schroeder and starring Elias Koteas, Angelina Jolie, Billy Drago, Karen Sheperd and Jack Palance.  It is an unrelated sequel to the 1989 film "Cyborg", although footage from the original is used in a dream sequence.  It was also Jolie's film debut in a starring role (she had previously made an earlier film, "Lookin' to Get Out", as a child actress).  It was followed by the 1995 direct-to-video release "".

In the Land of Blood and Honey: In the Land of Blood and Honey is a 2011 American war film written, produced, and directed by Angelina Jolie and starring Zana Marjanović, Goran Kostić, and Rade Šerbedžija.  The film, Jolie's first commercial release as a director, depicts a love story set against the background of the Bosnian War.  It opened in the United States on December 23, 2011, in a limited theatrical release.

Jolie (name): Jolie is a female given name of French origin and its meaning is "pretty".  It is pronounced "zhoh-LEE" or "joh-LEE".  The name has also become popular after American actress Angelina Jolie used it as her surname (it is really her middle name).  It can be also spelled as "Jolee", "Joli", or "Jo'Le".

Angelina Jolie: Angelina Jolie Pitt ( ; née Voight; born June 4, 1975) is an American actress, filmmaker, and humanitarian.  She has received an Academy Award, two Screen Actors Guild Awards, and three Golden Globe Awards, and has been cited as Hollywood's highest-paid actress.  Jolie made her screen debut as a child alongside her father, Jon Voight, in "Lookin' to Get Out" (1982).  Her film career began in earnest a decade later with the low-budget production "Cyborg 2" (1993), followed by her first leading role in a major film, "Hackers" (1995).  She starred in the critically acclaimed biographical cable films "George Wallace" (1997) and "Gia" (1998), and won an Academy Award for Best Supporting Actress for her performance in the drama "Girl, Interrupted" (1999).

James Haven: James Haven (born James Haven Voight; May 11, 1973) is an American actor and producer.  He is the son of actors Jon Voight and Marcheline Bertrand, and the older brother of actress Angelina Jolie.

Malka Older: Malka Older is an author and humanitarian worker.  She was named Senior Fellow for Technology and Risk at the Carnegie Council for Ethics in International Affairs for 2015, and she has more than eight years of experience in humanitarian aid and development.

Moira Kelly (humanitarian): Moira Therese Kelly {'1': ", '2': ", '3': ", '4': "} (born 31 January 1964) is an Australian humanitarian worker.  In 2001, she was awarded the Order of Australia in recognition of her humanitarian service to both the Australian and international communities.  In 2012, Kelly received the Victorian of the Year award and in 2003 and 2004, she was nominated for the Australian of the Year awards.

Angelina Jolie filmography: Angelina Jolie is an American actress and filmmaker.  As a child, she made her screen debut in the 1982 comedy film "Lookin' to Get Out", acting alongside her father Jon Voight.  Eleven years later she appeared in her next feature, the low-budget film "Cyborg 2", a commercial failure.  She then starred as a teenage hacker in the 1995 science fiction thriller "Hackers", which went on to be a cult film despite performing poorly at the box-office.  Jolie's career prospects improved with a supporting role in the made-for-television film "George Wallace" (1997), for which she received the Golden Globe Award for Best Supporting Actress – Television Film.  She made her breakthrough the following year in HBO's television film "Gia" (1998).  For her performance in the title role of fashion model Gia Carangi, she won the Golden Globe Award for Best Actress – Television Film.

Aptostichus angelinajolieae: The Angelina Jolie trapdoor spider ("Aptostichus angelinajolieae", often misspelled "angelinajoleae") is a species of Euctenizidae, nocturnal arthropods who seize their prey after leaping out of their burrows and inject it with venom.  It was described by the Auburn University professor Jason Bond in 2008, who named it after the American actress Angelina Jolie in recognition of her work on the United Nations High Commission for Refugees.  It was one of only seven described species of "Aptostichus" until 2012, when it was joined by Bono's Joshua Tree trapdoor spider and 32 other species.

Marcheline Bertrand: Marcia Lynne "Marcheline" Bertrand (May 9, 1950 – January 27, 2007) was an American actress and humanitarian worker.  She was the former wife of actor Jon Voight and the mother of actors Angelina Jolie and James Haven.

Question: Which parent of Angelina Jolie and James Haven also worked as a Humanitarian Worker?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "parent_name": {
      "type": "string",
      "description": "The name of the parent who is also a humanitarian worker."
    },
    "children_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the children of the identified parent."
    },
    "parent_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The professions of the identified parent."
    }
  },
  "required": [
    "parent_name",
    "children_names",
    "parent_professions"
  ],
  "additionalProperties": false
}
