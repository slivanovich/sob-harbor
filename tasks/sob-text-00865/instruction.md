{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBack to the Woods (Family Guy): \"Back to the Woods\" is the ninth episode of the sixth season in the Fox animated comedy series \"Family Guy\" that originally aired on February 17, 2008.  The episode follows Peter Griffin as he tries to regain his identity that has been stolen by actor James Woods, who has done so to get revenge at Peter for what he did to him at the end of \"Peter's Got Woods\".\n\nJane's House: Jane's House is a 1994 drama television film starring James Woods, Anne Archer and Melissa Lahlitah Crider.  It was directed by Glenn Jordan, who had previously worked with Woods on the 1986 TV movie \"Promise\" and the 1991 TV movie \"The Boys\".  The film first aired on the CBS network on January 2, 1994.\n\nPeter's Got Woods: \"Peter's Got Woods\" is the eleventh episode and the mid-season premiere of the fourth season of the American animated television series \"Family Guy\".  It originally aired on Fox in the United States on September 11, 2005.  In the episode, Brian offers to help an African-American woman change the name of James Woods Regional High School to Martin Luther King Jr., but his friendship with Peter becomes strained when Peter — who objects to the idea — recruits actor James Woods to sabotage the idea.  James Woods would later return for revenge in the season 6 episode \"Back to the Woods\", and again for \"Brian Griffin's House of Payne\" and would eventually be killed off in the season 9 premiere episode \"And Then There Were Fewer\", but is later revealed to have survived his death in the season 10 episode \"\".\n\nRay Woods: Ray James Woods (February 2, 1895 – October 1965) was an American college basketball standout for Illinois in the 1910s.  A guard, Woods helped lead the Fighting Illini to two Big Ten Conference championships in 1915 and 1917, with the former being an undefeated 16–0 season that resulted in a retroactive national championship.  In all three seasons he played at the school, Woods was named an All-American and was honored as the Helms Foundation National Player of the Year as a senior in 1916–17.  He was Illinois' first-ever All-American in basketball and teamed up with his brother, Ralf (a forward), in guiding the school to their first era of basketball dominance.  Woods was elected to the \"Illini Men's Basketball All-Century Team\" in 2004.\n\nKiller: A Journal of Murder (film): Killer: A Journal of Murder is a 1995 American drama film written and directed by Tim Metcalfe.  It is based on the life of serial killer Carl Panzram, and uses passages from his .  James Woods stars as Panzram and Robert Sean Leonard as Henry Lesser.  Other stars include Ellen Greene as Elizabeth Wyatt, Cara Buono as Esther Lesser, Robert John Burke as R.G. Greiser and Richard Riehle as Warden Quince.  Michael Jeffrey Woods, James Woods' young brother also made an appearance as Harry Sinclair.\n\nJames Woods (footballer): James Woods was an English professional footballer who played as an inside forward.  He joined Burnley in January 1885 and played in several of the club's early friendlies prior to the advent of the Football League in 1888.  Woods made only one league appearance for Burnley, deputising for Scottish forward Pat Gallocher in the 1–5 defeat away at Accrington on 1 December 1888.  He left the club in 1889.\n\nCasino (film): Casino is a 1995 American epic crime drama film directed by Martin Scorsese and starring Robert De Niro, Joe Pesci, and Sharon Stone.  It is based on the non-fiction book \"\" by Nicholas Pileggi, who also co-wrote the screenplay for the film with Scorsese.  The two previously collaborated on the hit film \"Goodfellas\" (1990).\n\nJames Woods: James Howard Woods (born April 18, 1947) is an American actor and producer.  He is known primarily for playing villainous roles, and has appeared in a variety of films, including \"The Way We Were\" (1973), \"The Onion Field\" (1979), \"Videodrome\" (1983), \"Once Upon a Time in America\" (1984), \"Best Seller\" (1987), \"Chaplin\" (1992), \"Casino\" (1995), \"Nixon\" (1995), \"Vampires\" (1998), \"Straw Dogs\" (2011) and \"White House Down\" (2013).  On television, he is known for portraying the titular protagonist of \"Shark\" (2006–2008), and for playing himself on eight episodes of the animated series \"Family Guy\", as well as on one episode of \"The Simpsons\".\n\nThe Boys (1991 film): The Boys (aka The Guys) is a drama/black comedy television film starring James Woods and John Lithgow.  It was directed by Glenn Jordan, who had previously worked with Woods on the 1986 TV movie \"Promise\" and would later work with Woods again in 1994 for the TV drama film \"Jane's House\".  The film first aired on September 15, 1991 on the ABC Network.\n\nMy Name Is Bill W.: My Name Is Bill W. is a 1989 CBS Hallmark Hall of Fame television movie directed by Daniel Petrie, starring James Woods, JoBeth Williams and James Garner.  William G. Borchert, who wrote the film for television, based it on the true story of William Griffith Wilson and Dr. Robert Holbrook Smith, M.D. (the men respectively called \"Bill W.\" and \"Dr. Bob\"), the co-founders of Alcoholics Anonymous.  James Woods won an Emmy for his portrayal of Wilson.\n\nQuestion: Other then James Woods who else played in the movie Casino?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie.\"\n    },\n    \"other_actors\": {\n      \"type\": \"array\",\n      \"description\": \"A list of actors who played in the movie, excluding James Woods.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"release_year\",\n    \"other_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the movie."
      },
      "other_actors": {
        "type": "array",
        "description": "A list of actors who played in the movie, excluding James Woods.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "movie_title",
      "release_year",
      "other_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
